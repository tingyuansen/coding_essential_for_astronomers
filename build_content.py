#!/usr/bin/env python3
"""Build the reader content from the rendered lecture pages.

The site renders notebooks client-side (see docs/reader.html + docs/assets/render.js),
exactly like the companion *Agents for Astronomy* book. Because this repository only
keeps the executed HTML of each lecture, this script reconstructs a notebook-style
JSON per lecture from that HTML:

  * markdown cells  -> kept as already-rendered HTML (lossless LaTeX, math stays as
                       raw $..$ / $$..$$ and is typeset by KaTeX in the browser)
  * code cells      -> original source text (re-highlighted by highlight.js)
  * outputs         -> stream / image / html-table / text, in notebook output schema

It also emits docs/assets/book-data.js (the table-of-contents manifest).

Run:  python3 build_content.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).parent.resolve()
DOCS = ROOT / "docs"
# Executed lecture HTML (the build source; kept out of the published docs/ tree).
LECTURES_HTML = ROOT / "build_src" / "lectures"
CONTENT = DOCS / "content"
ASSETS = DOCS / "assets"

AUTHOR = "Yuan-Sen Ting"
AFFIL = "The Ohio State University"

# ---------------------------------------------------------------- manifest ----
# n, slug, clean title, optional quiz, optional data file. Slides are inferred.
LECTURES = [
    (1,  "lecture01-welcome-and-setting-up",                          "Welcome & Setting Up", None, None),
    (2,  "lecture02-variables-and-collections",                       "Variables & Collections", "https://www.playlab.ai/project/cmef7fyyr049hjo0unode4jfp", None),
    (3,  "lecture03-control-flow-and-file-operations",               "Control Flow & File Operations", "https://www.playlab.ai/project/cmej5um0y0bp6jx0uipjwrc4e", None),
    (4,  "lecture04-numerical-computing",                             "Numerical Computing", "https://www.playlab.ai/project/cmeaywmuo015rlc0uegalyjtm", None),
    (5,  "lecture05-functions-and-object-oriented-programming",      "Functions & Object-Oriented Programming", "https://www.playlab.ai/project/cmex8qs8d06fole0uiw8yk4vf", None),
    (6,  "lecture06-data-visualization",                             "Data Visualization", "https://www.playlab.ai/project/cmf1ur1ba0k6yje0vdb875ll8", None),
    (7,  "lecture07-llm-api-basics",                                 "LLM API Basics", "https://www.playlab.ai/project/cmfichs6103zjl50u67eq8opb", None),
    (8,  "lecture08-llm-function-tools-and-rag",                     "LLM Function Tools & RAG", "https://www.playlab.ai/project/cmfokigx40oqwow0uauvk1z3p", None),
    (9,  "lecture09-github",                                         "Git & GitHub", "https://www.playlab.ai/project/cmf1uyhie0knkhn0uml9sls1c", None),
    (10, "lecture10-streamlit",                                      "Streamlit", "https://www.playlab.ai/project/cmfud0fvx0fscnv0udkrqfvj5", None),
    (11, "lecture11-pandas-basics",                                  "Pandas Basics", "https://www.playlab.ai/project/cmgd0wbkp0vjsp80ufo2go2u8", "data_gaia_dr3.csv"),
    (12, "lecture12-advanced-pandas",                                "Advanced Pandas", "https://www.playlab.ai/project/cmgiohn0d0n1gk50ucl7r4v9t", "data_gaia_dr3.csv"),
    (13, "lecture13-astroquery-astropy-units-coordinates",          "Astroquery, Units & Coordinates", "https://www.playlab.ai/project/cmgpnfltg6uapjy0u7fjnxgis", None),
    (14, "lecture14-astropy-time-observationplanning-fits",         "Astropy Time, Observation Planning & FITS", "https://www.playlab.ai/project/cmgwref9m0wacm00uvr5c2yjk", None),
    (15, "lecture15-skyfield-ephemerides",                          "Skyfield Ephemerides", "https://www.playlab.ai/project/cmh2j60nb5xl5lk0uxe5b1nw4", None),
    (16, "lecture16-scipy-interpolation-differentiation-integration", "SciPy: Interpolation, Differentiation & Integration", "https://www.playlab.ai/project/cmh74ex6l1if9kx0u2uw4x0yz", None),
    (17, "lecture17-scipy-random-variable-measurement-uncertainty", "Random Variables & Measurement Uncertainty", "https://www.playlab.ai/project/cmhcp30770ahqke0vq42ccwpu", None),
    (18, "lecture18-scipy-optimization-curve-fitting",             "Optimization & Curve Fitting", "https://www.playlab.ai/project/cmhiiv7ls03l2h90ut83lwe1l", None),
    (19, "lecture19-time-series-fitting-exoplanet-transits",       "Time-Series Fitting: Exoplanet Transits", "https://www.playlab.ai/project/cmi59odci73i6ij0uekbuv79q", None),
    (20, "lecture20-image-fitting-point-sources-photometry",       "Image Fitting & Photometry", "https://www.playlab.ai/project/cmi9phbrm6obsgu0u4pp3sn6n", None),
    (21, "lecture21-spectroscopic-fitting",                        "Spectroscopic Fitting", "https://www.playlab.ai/project/cmidyngxn0dbmiy0u6mlyyhq0", None),
    (22, "lecture22-model-context-protocol",                       "Model Context Protocol", None, None),
]

# Parts list lectures by their ORIGINAL number, in reading order. MCP (orig 22)
# is taught right after Lecture 8, so the whole sequence is renumbered 1..22 for
# display; the original numbers are kept only to locate slides / quizzes / files.
PARTS = [
    ("Part I",   "Python Foundations",
     "From a clean environment to numerical computing, modular code, and publication-quality figures.",
     [1, 2, 3, 4, 5, 6]),
    ("Part II",  "AI Tools & Collaboration",
     "Talking to language models through their APIs, giving them tools and the Model Context Protocol, and shipping work with Git and Streamlit.",
     [7, 8, 22, 9, 10]),
    ("Part III", "Astronomical Data",
     "Catalogs and DataFrames, archive queries, units and coordinates, time systems, and ephemerides.",
     [11, 12, 13, 14, 15]),
    ("Part IV",  "Modeling & Fitting",
     "Interpolation and calculus, measurement uncertainty, and curve fitting across light curves, images, and spectra.",
     [16, 17, 18, 19, 20, 21]),
]

# one-line summaries for the table of contents
SUMMARY = {
    1: "Course orientation, environment setup, and AI-supported coding.",
    2: "Core Python syntax, data structures, and debugging patterns.",
    3: "Control flow, file handling, and automation for data workflows.",
    4: "NumPy arrays, vectorisation, and numerical best practices.",
    5: "Function design, modular code, and object-oriented programming.",
    6: "Matplotlib workflows, visual diagnostics, and plotting techniques.",
    7: "LLM API authentication, structured prompting, and cost-aware use.",
    8: "Function calling, retrieval-augmented generation, and vector search.",
    9: "Git and GitHub fundamentals, documentation, and Pages publishing.",
    10: "Streamlit interfaces, state management, and deploying research tools.",
    11: "Pandas DataFrames, catalog operations, and data manipulation.",
    12: "GroupBy, merges, pivot tables, and advanced Pandas transformations.",
    13: "Astroquery archive access, Astropy units, coordinates, cross-matching.",
    14: "Astropy Time, observation planning, visibility, and FITS files.",
    15: "Skyfield ephemerides, planetary positions, and rise/set/transit.",
    16: "SciPy interpolation, differentiation, and integration.",
    17: "Statistics, random variables, uncertainty, and error propagation.",
    18: "SciPy optimization, curve fitting, and parameter estimation.",
    19: "Time-series analysis and exoplanet transit light-curve fitting.",
    20: "Image fitting, point spread functions, and photometry.",
    21: "Spectroscopic fitting, equivalent widths, and line profiles.",
    22: "Model Context Protocol: building AI tools and external integrations.",
}

# Display (reading-order) number for each ORIGINAL lecture number, derived from
# the order lectures appear in PARTS. All prose still refers to lectures by their
# original numbers; _remap_refs() rewrites those references to display numbers so
# the renumbered sequence reads consistently.
DISPLAY_NUM: dict[int, int] = {}
_pos = 0
for _name, _title, _blurb, _orig_list in PARTS:
    for _orig in _orig_list:
        _pos += 1
        DISPLAY_NUM[_orig] = _pos

_REF_RE = re.compile(r"([Ll]ectures?)([\s ]+)(\d+)((?:\s*[–-]\s*)(\d+))?")


def _remap_refs(html: str) -> str:
    """Rewrite 'Lecture N' / 'Lectures A-B' references to display numbers."""
    def sub(m: re.Match) -> str:
        word, sep, a = m.group(1), m.group(2), int(m.group(3))
        a2 = DISPLAY_NUM.get(a, a)
        tail = m.group(4)
        if tail:
            b = m.group(5)
            b2 = DISPLAY_NUM.get(int(b), int(b))
            dash_part = tail[: tail.rfind(b)]
            return f"{word}{sep}{a2}{dash_part}{b2}"
        return f"{word}{sep}{a2}"
    return _REF_RE.sub(sub, html)


# --------------------------------------------------------------- helpers ------
def _clean_heading_anchors(soup_fragment) -> None:
    """Drop nbconvert anchor links and ids on headings (render.js re-slugs them)."""
    for a in soup_fragment.select("a.anchor-link"):
        a.decompose()
    for h in soup_fragment.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if h.has_attr("id"):
            del h["id"]


def _markdown_html(cell) -> str:
    rendered = cell.select_one(".jp-RenderedMarkdown")
    if rendered is None:
        return ""
    _clean_heading_anchors(rendered)
    return rendered.decode_contents().strip()


def _code_source(cell) -> str:
    pre = cell.select_one(".jp-InputArea .highlight pre")
    if pre is None:
        return ""
    return pre.get_text().rstrip("\n")


def _extract_outputs(cell) -> list[dict]:
    outputs: list[dict] = []
    wrapper = cell.select_one(".jp-Cell-outputWrapper")
    if wrapper is None:
        return outputs
    for child in wrapper.select(".jp-OutputArea-child"):
        out = child.select_one(".jp-OutputArea-output")
        if out is None:
            continue
        is_exec = "jp-OutputArea-executeResult" in (child.get("class") or [])
        mime = out.get("data-mime-type") or ""

        img = out.select_one("img")
        if img is not None and img.get("src", "").startswith("data:"):
            src = img["src"]
            head, _, data = src.partition(",")
            m = re.search(r"image/(png|jpeg|svg\+xml)", head)
            key = f"image/{m.group(1)}" if m else "image/png"
            outputs.append({
                "output_type": "display_data",
                "data": {key: data},
                "metadata": {},
            })
            continue

        table = out.select_one("table")
        if table is not None:
            outputs.append({
                "output_type": "execute_result",
                "data": {"text/html": out.decode_contents().strip()},
                "metadata": {},
                "execution_count": None,
            })
            continue

        text = out.get_text()
        if "stderr" in mime or "error" in mime:
            outputs.append({"output_type": "stream", "name": "stderr", "text": text})
        elif is_exec:
            outputs.append({
                "output_type": "execute_result",
                "data": {"text/plain": text},
                "metadata": {},
                "execution_count": None,
            })
        else:
            outputs.append({"output_type": "stream", "name": "stdout", "text": text})

    # Merge consecutive stream outputs of the same name (Jupyter concatenates
    # these; nbconvert can split progress bars into many fragments).
    merged: list[dict] = []
    for o in outputs:
        if (o["output_type"] == "stream" and merged
                and merged[-1]["output_type"] == "stream"
                and merged[-1]["name"] == o["name"]):
            merged[-1]["text"] += o["text"]
        else:
            merged.append(o)
    return merged


def convert(path: Path) -> dict:
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")

    # Drop the very first H1 (the lecture title — the reader header supplies it).
    first_h1 = soup.select_one(".jp-RenderedMarkdown h1")
    if first_h1 is not None:
        first_h1.decompose()

    cells: list[dict] = []
    md_buffer: list[str] = []

    def flush_md():
        if md_buffer:
            html = "\n".join(s for s in md_buffer if s).strip()
            if html:
                cells.append({"cell_type": "markdown_html", "html": html})
            md_buffer.clear()

    # Top-level cells appear in document order under <body>.
    for cell in soup.select(".jp-Cell"):
        classes = cell.get("class") or []
        if "jp-MarkdownCell" in classes:
            md_buffer.append(_remap_refs(_markdown_html(cell)))
        elif "jp-CodeCell" in classes:
            flush_md()
            source = _code_source(cell)
            outputs = _extract_outputs(cell)
            if source.strip() == "" and not outputs:
                continue
            cells.append({
                "cell_type": "code",
                "source": source,
                "execution_count": None,
                "outputs": outputs,
            })
    flush_md()
    return {"cells": cells}


# --------------------------------------------------------------- book-data ----
def build_book_data() -> str:
    by_n = {n: (slug, title, quiz, data) for (n, slug, title, quiz, data) in LECTURES}
    parts_js = []
    for name, title, blurb, rng in PARTS:
        chapters = []
        for n in rng:
            slug, title_c, quiz, data = by_n[n]
            entry = {
                "n": DISPLAY_NUM[n],          # reading-order (display) number
                "orig": n,                    # original lecture number (file identity)
                "slug": slug,
                "type": "ipynb",
                "title": title_c,
                "lecturer": AUTHOR,
                "affil": AFFIL,
                "summary": SUMMARY.get(n, ""),
                "slides": f"slides/Lecture{n}_Slides/",
            }
            if quiz:
                entry["quiz"] = quiz
            if data:
                entry["data"] = data
            chapters.append(entry)
        parts_js.append({"name": name, "title": title, "blurb": blurb, "chapters": chapters})

    book = {
        "title": "Coding Essentials for Astronomers",
        "series": "Python, scientific computing & AI for the physical sciences",
        "subtitle": "",
        "parts": parts_js,
    }
    body = json.dumps(book, indent=2, ensure_ascii=False)
    return (
        "/* Course manifest — parts, lectures, author, content files.\n"
        "   Generated by build_content.py — do not edit by hand. */\n"
        f"window.BOOK = {body};\n\n"
        "// Flat list for navigation\n"
        "window.BOOK.flat = window.BOOK.parts.flatMap(p => p.chapters.map(c => ({ ...c, part: p })));\n"
        "window.BOOK.byN = Object.fromEntries(window.BOOK.flat.map(c => [c.n, c]));\n"
    )


def main() -> None:
    CONTENT.mkdir(parents=True, exist_ok=True)
    for n, slug, title, quiz, data in LECTURES:
        src = LECTURES_HTML / f"{slug}.html"
        if not src.exists():
            print(f"!! missing {src.name}")
            continue
        nb = convert(src)
        out = CONTENT / f"{slug}.json"
        out.write_text(json.dumps(nb, ensure_ascii=False), encoding="utf-8")
        ncode = sum(1 for c in nb["cells"] if c["cell_type"] == "code")
        nmd = sum(1 for c in nb["cells"] if c["cell_type"] == "markdown_html")
        print(f"  {slug}: {nmd} md + {ncode} code -> {out.stat().st_size//1024} KB")

    (ASSETS / "book-data.js").write_text(build_book_data(), encoding="utf-8")
    print(f"Wrote {len(LECTURES)} content files + book-data.js")


if __name__ == "__main__":
    main()

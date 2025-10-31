#!/usr/bin/env python3
"""Build static lecture site from Jupyter notebooks."""
from __future__ import annotations

import ast
import datetime as _dt
import html
import io
import json
import re
import shutil
import traceback
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = Path(__file__).parent.resolve()
DOCS_DIR = ROOT / "docs"
LECTURES_DIR = DOCS_DIR / "lectures"
ASSETS_DIR = DOCS_DIR / "assets"

NOTEBOOK_PATTERN = re.compile(r"^Lecture(\d+)_([A-Za-z0-9_\-]+)_(\d{8})$")

LECTURE_SUMMARIES = {
    1: (
        "Course orientation, environment setup, and expectations for AI-supported coding."
    ),
    2: (
        "Core Python syntax, data structures, and essential debugging patterns for research scripts."
    ),
    3: (
        "Control flow design, file handling, and automation techniques for data-driven workflows."
    ),
    4: (
        "NumPy arrays, vectorisation, and numerical best practices for large astronomical datasets."
    ),
    5: (
        "Function design, modular organisation, and foundations of object-oriented programming."
    ),
    6: (
        "Matplotlib workflows, visual diagnostics, and interactive plotting techniques."
    ),
    7: (
        "LLM API authentication, structured prompting, and cost-aware usage patterns."
    ),
    8: (
        "Function calling, retrieval-augmented generation, and vector search integrations."
    ),
    9: (
        "Git and GitHub fundamentals, documentation standards, and GitHub Pages publishing."
    ),
    10: (
        "Streamlit interface design, state management, and deployment of interactive research tools."
    ),
    11: (
        "Pandas DataFrames, catalog operations, and data manipulation for astronomical analysis."
    ),
    12: (
        "GroupBy operations, merging catalogs, pivot tables, and advanced Pandas transformations."
    ),
    13: (
        "Astroquery database access, Astropy units and coordinates, and catalog cross-matching."
    ),
    14: (
        "Astropy Time systems, observation planning, visibility calculations, and FITS file handling."
    ),
    15: (
        "SkyField ephemerides, precise planetary positions, and rise/set/transit calculations."
    ),
    16: (
        "SciPy interpolation, differentiation, and integration for astronomical time-series data."
    ),
    17: (
        "Statistical analysis, measurement uncertainty, random variables, and error propagation."
    ),
}

QUIZ_LINKS = {
    2: "https://www.playlab.ai/project/cmef7fyyr049hjo0unode4jfp",
    3: "https://www.playlab.ai/project/cmej5um0y0bp6jx0uipjwrc4e",
    4: "https://www.playlab.ai/project/cmeaywmuo015rlc0uegalyjtm",
    5: "https://www.playlab.ai/project/cmex8qs8d06fole0uiw8yk4vf",
    6: "https://www.playlab.ai/project/cmf1ur1ba0k6yje0vdb875ll8",
    7: "https://www.playlab.ai/project/cmfichs6103zjl50u67eq8opb",
    8: "https://www.playlab.ai/project/cmfokigx40oqwow0uauvk1z3p",
    9: "https://www.playlab.ai/project/cmf1uyhie0knkhn0uml9sls1c",
    10: "https://www.playlab.ai/project/cmfud0fvx0fscnv0udkrqfvj5",
    11: "https://www.playlab.ai/project/cmgd0wbkp0vjsp80ufo2go2u8",
    12: "https://www.playlab.ai/project/cmgiohn0d0n1gk50ucl7r4v9t",
    13: "https://www.playlab.ai/project/cmgpnfltg6uapjy0u7fjnxgis",
}


def _format_title(raw: str) -> str:
    words = raw.replace("_", " ").strip()
    words = re.sub(r"\s+", " ", words)
    title = words.title()
    replacements = {
        "Llm": "LLM",
        "Llms": "LLMs",
        "Api": "API",
        "Rag": "RAG",
        "Oop": "OOP",
        "Numpy": "NumPy",
        "Github": "GitHub",
    }
    for needle, replacement in replacements.items():
        title = re.sub(rf"\b{needle}\b", replacement, title)
    return title


def _format_date(date_str: str) -> str:
    dt = _dt.datetime.strptime(date_str, "%Y%m%d").date()
    return dt.strftime("%b %Y")


def _slugify(number: int, raw: str) -> str:
    base = f"lecture{number:02d}-" + raw.lower().replace("_", "-")
    slug = re.sub(r"[^a-z0-9\-]+", "-", base)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def _first_markdown_excerpt(nb) -> str:
    for cell in nb.cells:
        if cell.get("cell_type") == "markdown":
            text = cell.get("source", "").strip()
            if not text:
                continue
            text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
            text = re.sub(r"`([^`]*)`", r"\1", text)
            text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
            text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
            text = re.sub(r"[#*_>]", "", text)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) > 180:
                text = text[:177].rsplit(" ", 1)[0] + "…"
            return text
    return ""


def _scrub_course_details(html: str) -> str:
    patterns = [
        r"<p>\s*<em>\s*Tutorial by.*?</em>\s*</p>",
        r"<p>\s*<em>\s*Astron 1221:.*?</em>\s*</p>",
        r"<p>[^<]*Astron 1221[^<]*</p>",
    ]
    for pattern in patterns:
        html = re.sub(pattern, "", html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(
        r"<p[^>]*>[^<]*Astron 1221[^<]*</p>\s*",
        "",
        html,
        flags=re.IGNORECASE,
    )
    html = re.sub(
        r"<p[^>]*>.*?Astron 1221.*?</p>\s*",
        "",
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    html = re.sub(
        r"\*Astron 1221:[^\n]*\*\s*",
        "",
        html,
        flags=re.IGNORECASE,
    )
    return html


def _execute_notebook(path: Path) -> nbformat.NotebookNode:
    nb = nbformat.read(path, as_version=4)
    executor = ExecutePreprocessor(timeout=600, kernel_name="python3", allow_errors=True)
    try:
        executor.preprocess(nb, {"metadata": {"path": str(path.parent)}})
    except Exception as exc:  # noqa: BLE001 - ensure build continues
        print(f"Warning: failed to execute {path.name}: {exc}")
    _fill_missing_outputs(nb)
    return nb


def _should_skip_cell(source: str, missing_aliases: dict[str, str]) -> bool:
    stripped = source.lstrip()
    if stripped.startswith("%%") or stripped.startswith("%") or stripped.startswith("!"):
        return True
    skip_tokens = ("input(", "getpass(")
    if any(token in source for token in skip_tokens):
        return True
    for alias in missing_aliases:
        if re.search(rf"\b{re.escape(alias)}\b", source):
            return True
    return False


def _run_python_cell(
    source: str,
    env: dict[str, object],
    exec_count: int,
) -> tuple[list[nbformat.NotebookNode], int, str | None]:
    outputs: list[nbformat.NotebookNode] = []
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    value_captured = False
    expr_value = None
    missing_module: str | None = None

    try:
        module = ast.parse(source, mode="exec")
        last_expr = None
        if module.body and isinstance(module.body[-1], ast.Expr):
            last_expr = ast.Expression(module.body[-1].value)
            module.body = module.body[:-1]
        code_obj = compile(module, filename="<notebook>", mode="exec")
        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            exec(code_obj, env)
            if last_expr is not None:
                expr_value = eval(compile(last_expr, filename="<notebook>", mode="eval"), env)
                value_captured = True
    except SyntaxError:
        return [], exec_count, "__skip__"
    except ModuleNotFoundError as exc:
        missing_module = exc.name
        outputs.append(
            nbformat.v4.new_output(
                "stream",
                name="stdout",
                text=(
                    f"⚠️ Output not rendered: Python module '{exc.name}' is missing. "
                    "Run this notebook locally after installing dependencies.\n"
                ),
            )
        )
    except ImportError as exc:
        missing_module = getattr(exc, "name", None) or str(exc).split(" ")[0]
        outputs.append(
            nbformat.v4.new_output(
                "stream",
                name="stdout",
                text=(
                    "⚠️ Output not rendered: required dependency could not be loaded. "
                    "Run this notebook locally to view results.\n"
                ),
            )
        )
    except NameError as exc:
        missing_module = "__halt__"
        outputs.append(
            nbformat.v4.new_output(
                "stream",
                name="stdout",
                text=(
                    "⚠️ Output not rendered: prior setup step did not run, so "
                    f"'{getattr(exc, 'name', str(exc))}' is undefined. "
                    "Execute the notebook in order to view results.\n"
                ),
            )
        )
    except Exception as exc:  # noqa: BLE001
        text = stdout_buffer.getvalue()
        err_text = stderr_buffer.getvalue()
        if text:
            outputs.append(nbformat.v4.new_output("stream", name="stdout", text=text))
        if err_text:
            outputs.append(nbformat.v4.new_output("stream", name="stderr", text=err_text))
        tb_lines = traceback.format_exc().splitlines()
        outputs.append(
            nbformat.v4.new_output(
                "error",
                ename=exc.__class__.__name__,
                evalue=str(exc),
                traceback=tb_lines,
            )
        )
    else:
        text = stdout_buffer.getvalue()
        err_text = stderr_buffer.getvalue()
        if text:
            outputs.append(nbformat.v4.new_output("stream", name="stdout", text=text))
        if err_text:
            outputs.append(nbformat.v4.new_output("stream", name="stderr", text=err_text))
        if value_captured:
            outputs.append(
                nbformat.v4.new_output(
                    "execute_result",
                    data={"text/plain": repr(expr_value)},
                    metadata={},
                    execution_count=exec_count,
                )
            )

    return outputs, exec_count + 1, missing_module


def _extract_import_aliases(source: str) -> dict[str, str]:
    aliases: dict[str, str] = {}
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return aliases
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.asname or alias.name
                aliases[name] = alias.name
        elif isinstance(node, ast.ImportFrom):
            if node.module is None:
                continue
            for alias in node.names:
                name = alias.asname or alias.name
                aliases[name] = node.module
    return aliases


def _fill_missing_outputs(nb: nbformat.NotebookNode) -> None:
    env: dict[str, object] = {"__builtins__": __builtins__}
    exec_count = 1
    missing_aliases: dict[str, str] = {}
    for cell in nb.cells:
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", "")
        if not source.strip():
            continue
        if _should_skip_cell(source, missing_aliases):
            continue
        # Skip cells that were already executed (have execution_count set)
        if cell.get("execution_count") is not None:
            continue
        if cell.get("outputs"):
            continue
        aliases = _extract_import_aliases(source)
        outputs, exec_count, missing_module = _run_python_cell(source, env, exec_count)
        if missing_module:
            if outputs:
                cell["outputs"] = outputs
                cell["execution_count"] = exec_count - 1
            if missing_module == "__halt__" or missing_module == "__skip__":
                break
            for alias, module in aliases.items():
                if module == missing_module:
                    missing_aliases[alias] = module
            missing_aliases[missing_module] = missing_module
            continue
        cell["outputs"] = outputs
        cell["execution_count"] = exec_count - 1


def _inject_header_and_footer(html: str, header_html: str, footer_html: str) -> str:
    # Insert header after the opening <body> tag while preserving existing attributes
    def add_body_class(match):
        prefix, classes = match.groups()
        if "lecture-page" in classes.split():
            new_classes = classes
        else:
            new_classes = "lecture-page " + classes
        return f"<body{prefix}class=\"{new_classes}\""

    html, count = re.subn(r"<body([^>]*)class=\"([^\"]*)\"", add_body_class, html, count=1)
    if count == 0:
        html = html.replace("<body", "<body class=\"lecture-page\"", 1)

    body_start = html.find("<body")
    if body_start != -1:
        body_end = html.find('>', body_start)
        if body_end != -1:
            insert_at = body_end + 1
            html = html[:insert_at] + "\n" + header_html + html[insert_at:]

    html = html.replace("</body>", footer_html + "</body>", 1)

    html = re.sub(
        r'data-jp-theme-light="true"',
        'data-jp-theme-light="false"',
        html,
    )
    html = re.sub(
        r'data-jp-theme-name="[^"]+"',
        'data-jp-theme-name="JupyterLab Dark"',
        html,
    )
    return html


def build() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)
    LECTURES_DIR.mkdir(parents=True, exist_ok=True)

    exporter = HTMLExporter()
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    exporter.template_name = "lab"
    exporter.mathjax_url = (
        "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS_CHTML-full,Safe"
    )
    try:
        exporter.theme = "dark"
    except AttributeError:
        # Older nbconvert without theme support; dark mode handled via CSS.
        pass

    header_html = (
        "<header class=\"site-header\">\n"
        "  <div class=\"container\">\n"
        "    <a class=\"brand\" href=\"../index.html\">Coding Essentials for Astronomers</a>\n"
        "    <nav><a href=\"../index.html\">Back to overview</a></nav>\n"
        "  </div>\n"
        "</header>\n"
    )
    footer_html = (
        "<footer class=\"site-footer\">\n"
        "  <div class=\"container\">\n"
        "    <p>Part of the Coding Essentials for Astronomers lecture series.</p>\n"
        "  </div>\n"
        "</footer>\n"
        "<script>\n"
        "  window.addEventListener('DOMContentLoaded', () => {\n"
        "    if (window.MathJax) {\n"
        "      if (window.MathJax.typesetPromise) {\n"
        "        window.MathJax.typesetPromise();\n"
        "      } else if (window.MathJax.Hub) {\n"
        "        window.MathJax.Hub.Queue(['Typeset', window.MathJax.Hub]);\n"
        "      }\n"
        "    }\n"
        "  });\n"
        "</script>\n"
    )

    lectures = []
    for notebook_path in sorted(ROOT.glob("Lecture*.ipynb")):
        match = NOTEBOOK_PATTERN.match(notebook_path.stem)
        if not match:
            print(f"Skipping unrecognised notebook name: {notebook_path.name}")
            continue
        number = int(match.group(1))
        raw_title = match.group(2)
        raw_date = match.group(3)
        display_title = f"Lecture {number}: {_format_title(raw_title)}"
        display_date = _format_date(raw_date)
        slug = _slugify(number, raw_title)
        lecture_rel_path = Path("lectures") / f"{slug}.html"
        output_path = LECTURES_DIR / lecture_rel_path.name
        page_title = f"{display_title} – Coding Essentials for Astronomers"

        # Skip if HTML file already exists
        if output_path.exists():
            print(f"Skipping {notebook_path.name} - HTML already exists")
            try:
                existing_html = output_path.read_text(encoding="utf-8")
            except OSError:
                existing_html = ""
            else:
                new_title = f"<title>{html.escape(page_title)}</title>"
                refreshed_html = re.sub(
                    r"<title>.*?</title>", new_title, existing_html, count=1
                )
                if refreshed_html != existing_html:
                    output_path.write_text(refreshed_html, encoding="utf-8")

            lecture_entry = {
                "number": number,
                "title": display_title,
                "date": display_date,
                "slug": slug,
                "relative_path": str(lecture_rel_path).replace("\\", "/"),
                "summary": LECTURE_SUMMARIES.get(
                    number, "Hands-on coding walkthrough."
                ),
            }
            quiz_link = QUIZ_LINKS.get(number)
            if quiz_link:
                lecture_entry["quiz_link"] = quiz_link

            lectures.append(lecture_entry)
            continue

        nb = _execute_notebook(notebook_path)
        raw_summary = _first_markdown_excerpt(nb)
        body, resources = exporter.from_notebook_node(nb)

        body = re.sub(
            r"<title>.*?</title>",
            f"<title>{html.escape(page_title)}</title>",
            body,
            count=1,
        )

        head_injection = (
            "<meta charset=\"utf-8\">\n"
            "<link rel=\"stylesheet\" href=\"../assets/styles.css\">\n"
            "<link rel=\"stylesheet\" href=\"../assets/notebook.css\">\n"
            "<script src=\"../assets/copy.js\" defer></script>\n"
        )
        body = body.replace("</title>", "</title>\n" + head_injection, 1)
        body = _inject_header_and_footer(body, header_html, footer_html)
        body = _scrub_course_details(body)

        output_path.write_text(body, encoding="utf-8")

        lecture_entry = {
            "number": number,
            "title": display_title,
            "date": display_date,
            "slug": slug,
            "relative_path": str(lecture_rel_path).replace("\\", "/"),
            "summary": LECTURE_SUMMARIES.get(
                number, raw_summary or "Hands-on coding walkthrough."
            ),
        }
        quiz_link = QUIZ_LINKS.get(number)
        if quiz_link:
            lecture_entry["quiz_link"] = quiz_link

        lectures.append(lecture_entry)

    lectures.sort(key=lambda item: item["number"])  # ensure numeric order
    (DOCS_DIR / "lectures.json").write_text(
        json.dumps(lectures, indent=2), encoding="utf-8"
    )
    print(f"Built {len(lectures)} lecture pages into {LECTURES_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    build()

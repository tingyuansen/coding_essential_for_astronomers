# Coding Essentials for Astronomers

> Foundational Python, scientific computing, and tooling guidance presented as an open textbook for astronomers.

**📖 Read the textbook online:** [https://tingyuansen.github.io/coding_essential_for_astronomers/](https://tingyuansen.github.io/coding_essential_for_astronomers/)

---

## Author

**Yuan-Sen Ting**  
The Ohio State University  
Email: ting.74@osu.edu

---

## About

This repository contains the complete lecture materials for *Coding Essentials for Astronomers*, a comprehensive open textbook covering Python programming, scientific computing, and modern data analysis techniques specifically tailored for astronomical research.

### What's Inside

- **Python programming patterns** applied to observational and simulation workflows
- **Numerical, visualization, and automation techniques** for modern data volumes
- **Data analysis techniques** across all modalities: images, spectra, and time series
- **Best practices** for collaboration, version control, and human-AI co-development

---

## Lecture Contents

| # | Title | Summary |
|---|-------|---------|
| 1 | Welcome & Setting Up | Course orientation, environment setup, and AI-supported coding. |
| 2 | Variables & Collections | Core Python syntax, data structures, and debugging patterns. |
| 3 | Control Flow & File Operations | Control flow, file handling, and automation for data workflows. |
| 4 | Numerical Computing | NumPy arrays, vectorisation, and numerical best practices. |
| 5 | Functions & Object-Oriented Programming | Function design, modular code, and object-oriented programming. |
| 6 | Data Visualization | Matplotlib workflows, visual diagnostics, and plotting techniques. |
| 7 | LLM API Basics | LLM API authentication, structured prompting, and cost-aware use. |
| 8 | LLM Function Tools & RAG | Function calling, retrieval-augmented generation, and vector search. |
| 9 | Model Context Protocol | Model Context Protocol: building AI tools and external integrations. |
| 10 | Git & GitHub | Git and GitHub fundamentals, documentation, and Pages publishing. |
| 11 | Streamlit | Streamlit interfaces, state management, and deploying research tools. |
| 12 | Pandas Basics | Pandas DataFrames, catalog operations, and data manipulation. |
| 13 | Advanced Pandas | GroupBy, merges, pivot tables, and advanced Pandas transformations. |
| 14 | Astroquery, Units & Coordinates | Astroquery archive access, Astropy units, coordinates, cross-matching. |
| 15 | Astropy Time, Observation Planning & FITS | Astropy Time, observation planning, visibility, and FITS files. |
| 16 | Skyfield Ephemerides | Skyfield ephemerides, planetary positions, and rise/set/transit. |
| 17 | SciPy: Interpolation, Differentiation & Integration | SciPy interpolation, differentiation, and integration. |
| 18 | Random Variables & Measurement Uncertainty | Statistics, random variables, uncertainty, and error propagation. |
| 19 | Optimization & Curve Fitting | SciPy optimization, curve fitting, and parameter estimation. |
| 20 | Time-Series Fitting: Exoplanet Transits | Time-series analysis and exoplanet transit light-curve fitting. |
| 21 | Image Fitting & Photometry | Image fitting, point spread functions, and photometry. |
| 22 | Spectroscopic Fitting | Spectroscopic fitting, equivalent widths, and line profiles. |

---

## Repository Structure

The site is a lightweight static reader: a landing page (`index.html`) and a single
client-side reader (`reader.html`) that renders each lecture from JSON — code is
re-highlighted with highlight.js and LaTeX is typeset with KaTeX in the browser.

```
coding_essential_for_astronomers/
├── README.md                 # This file
├── build_content.py          # Builds docs/content/*.json + book-data.js from build_src
├── build_slides.sh           # Builds Slidev decks into docs/slides
├── build_src/
│   └── lectures/             # Executed lecture HTML (build source; not published)
├── docs/                     # GitHub Pages website (published root)
│   ├── index.html            # Landing page (table of contents)
│   ├── reader.html           # Client-side lecture reader
│   ├── assets/
│   │   ├── style.css         # Design system
│   │   ├── render.js         # Notebook + Markdown + LaTeX renderer
│   │   ├── theme.js          # Light / dark toggle
│   │   └── book-data.js      # Generated table-of-contents manifest
│   ├── content/              # Generated per-lecture JSON (one per lecture)
│   ├── slides/               # Built Slidev decks (LectureN_Slides/)
│   ├── data_gaia_dr3.csv     # Sample dataset for the Pandas lectures
│   └── .nojekyll             # Serve assets verbatim on GitHub Pages
└── ...
```

> Build dependency: `build_content.py` only needs `beautifulsoup4` (`pip install beautifulsoup4`).

### Building

```bash
python3 build_content.py   # regenerate docs/content/*.json and docs/assets/book-data.js
./build_slides.sh          # (re)build the Slidev decks into docs/slides
```

To preview locally, serve `docs/` over HTTP (the reader fetches lecture JSON, so
`file://` will not work):

```bash
cd docs && python3 -m http.server 8000   # then open http://localhost:8000
```

---

## License & Usage

This textbook is made available for educational purposes. If you wish to use these lectures in your teaching or research, please **cite and refer to the original materials** rather than creating derivative versions. This ensures students and readers can access the most up-to-date and authoritative content.

---

## AI Collaboration Acknowledgment

This textbook was written in collaboration with **Claude Opus 4, Opus 4.5, Sonnet 4, and Sonnet 4.5**, developed by Anthropic.

While AI assisted with the writing process, **all material has been carefully designed, curated, and reviewed by the author**. The pedagogical structure, topic selection, scientific content, and teaching philosophy reflect the author's expertise developed through years of research and teaching in astrophysics and data science.

---

## How to Cite This Work

If you use this material in your research, teaching, or other work, please cite it appropriately.

### APA Style

> Ting, Y.-S. (2025). *Coding Essentials for Astronomers*. The Ohio State University. https://doi.org/10.5281/zenodo.17850426

### BibTeX

```bibtex
@misc{ting2025coding,
  author       = {Ting, Yuan-Sen},
  title        = {Coding Essentials for Astronomers},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17850426},
  url          = {https://doi.org/10.5281/zenodo.17850426},
  note         = {Open educational resource. Written in collaboration with Claude (Anthropic).}
}
```

---

## Contact

For questions, feedback, or collaboration inquiries, please contact:

**Yuan-Sen Ting**  
Department of Astronomy  
The Ohio State University  
Email: ting.74@osu.edu

---

## Acknowledgments

This work was developed as part of the Astron 1221 course at The Ohio State University. The author thanks the students whose questions and feedback have helped shape this material, and Anthropic for developing the Claude AI models that assisted in the writing process.

---

<p align="center">
  <em>Made with ❤️ for the astronomy community</em>
</p>

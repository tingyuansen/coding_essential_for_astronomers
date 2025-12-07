# Coding Essentials for Astronomers

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

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
| 1 | Welcome and Setting Up | Course orientation, environment setup, and expectations for AI-supported coding. |
| 2 | Variables and Collections | Core Python syntax, data structures, and essential debugging patterns for research scripts. |
| 3 | Control Flow and File Operations | Control flow design, file handling, and automation techniques for data-driven workflows. |
| 4 | Numerical Computing | NumPy arrays, vectorisation, and numerical best practices for large astronomical datasets. |
| 5 | Functions and Object-Oriented Programming | Function design, modular organisation, and foundations of object-oriented programming. |
| 6 | Data Visualization | Matplotlib workflows, visual diagnostics, and interactive plotting techniques. |
| 7 | LLM API Basics | LLM API authentication, structured prompting, and cost-aware usage patterns. |
| 8 | LLM Function Tools and RAG | Function calling, retrieval-augmented generation, and vector search integrations. |
| 9 | GitHub | Git and GitHub fundamentals, documentation standards, and GitHub Pages publishing. |
| 10 | Streamlit | Streamlit interface design, state management, and deployment of interactive research tools. |
| 11 | Pandas Basics | Pandas DataFrames, catalog operations, and data manipulation for astronomical analysis. |
| 12 | Advanced Pandas | GroupBy operations, merging catalogs, pivot tables, and advanced Pandas transformations. |
| 13 | Astroquery, Astropy Units & Coordinates | Astroquery database access, Astropy units and coordinates, and catalog cross-matching. |
| 14 | Astropy Time, Observation Planning, FITS | Astropy Time systems, observation planning, visibility calculations, and FITS file handling. |
| 15 | SkyField Ephemerides | SkyField ephemerides, precise planetary positions, and rise/set/transit calculations. |
| 16 | SciPy Interpolation, Differentiation, Integration | SciPy interpolation, differentiation, and integration for astronomical time-series data. |
| 17 | SciPy Random Variables, Measurement Uncertainty | Statistical analysis, measurement uncertainty, random variables, and error propagation. |
| 18 | SciPy Optimization & Curve Fitting | SciPy optimization techniques, curve fitting methods, and parameter estimation from observational data. |
| 19 | Time Series Fitting & Exoplanet Transits | Time series analysis, exoplanet transit detection, and light curve fitting techniques. |
| 20 | Image Fitting, Point Sources & Photometry | Image fitting, point spread functions, photometry techniques, and PSF fitting for crowded stellar fields. |
| 21 | Spectroscopic Fitting | Spectroscopic fitting, equivalent widths, spectral line profiles, and stellar atmosphere analysis techniques. |
| 22 | Model Context Protocol | Model Context Protocol (MCP), building AI-powered tools, and integrating LLMs with external services. |

---

## Repository Structure

```
coding_essential_for_astronomers/
├── README.md                 # This file
├── build_site.py            # Script to build HTML from notebooks
├── docs/                    # GitHub Pages website
│   ├── index.html          # Main landing page
│   ├── lectures.json       # Lecture metadata
│   ├── assets/             # CSS and JavaScript
│   │   ├── styles.css
│   │   ├── notebook.css
│   │   └── copy.js
│   └── lectures/           # Individual lecture HTML files
│       ├── lecture01-welcome-and-setting-up.html
│       ├── lecture02-variables-and-collections.html
│       └── ... (22 lectures total)
└── rpds/                   # Supporting Python package
```

---

## License & Usage

This textbook is released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

If you wish to use or adapt these lectures, please cite and refer to the original materials (see citation section below).

---

## AI Collaboration Acknowledgment

This textbook was written in collaboration with **Claude Opus 4 and Sonnet 4**, developed by Anthropic.

While AI assisted with the writing process, **all material has been carefully designed, curated, and reviewed by the author**. The pedagogical structure, topic selection, scientific content, and teaching philosophy reflect the author's expertise developed through years of research and teaching in astrophysics and data science.

---

## How to Cite This Work

If you use this material in your research, teaching, or other work, please cite it appropriately.

### APA Style

> Ting, Y.-S. (2025). *Coding Essentials for Astronomers*. The Ohio State University. https://doi.org/10.5281/zenodo.XXXXXXX

### BibTeX

```bibtex
@misc{ting2025coding,
  author       = {Ting, Yuan-Sen},
  title        = {Coding Essentials for Astronomers},
  year         = {2025},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.XXXXXXX},
  url          = {https://doi.org/10.5281/zenodo.XXXXXXX},
  note         = {Open educational resource. Written in collaboration with Claude (Anthropic).}
}
```

### BibTeX (GitHub version)

```bibtex
@misc{ting2025coding_github,
  author       = {Ting, Yuan-Sen},
  title        = {Coding Essentials for Astronomers},
  year         = {2025},
  institution  = {The Ohio State University},
  url          = {https://github.com/tingyuansen/coding_essential_for_astronomers},
  note         = {Open educational resource}
}
```

---

## Keywords

`astronomy` · `astrophysics` · `python` · `scientific-computing` · `data-analysis` · `numpy` · `pandas` · `matplotlib` · `astropy` · `astroquery` · `scipy` · `machine-learning` · `llm` · `open-educational-resource` · `textbook` · `photometry` · `spectroscopy` · `time-series`

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

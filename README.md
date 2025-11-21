# Coding Essentials for Astronomers

Foundational Python, scientific computing, and tooling guidance presented as an open textbook for astronomers.

## About

This repository contains lecture materials for "Coding Essentials for Astronomers," a comprehensive course covering Python programming, scientific computing, and modern data analysis techniques specifically tailored for astronomical research. The course emphasizes practical applications, from basic Python syntax to advanced topics like photometry, spectroscopy, and time-series analysis.

## Author

**Yuan-Sen Ting**  
The Ohio State University

## Contents

The course covers a wide range of topics including:

- Python programming fundamentals
- Numerical computing with NumPy
- Data visualization with Matplotlib
- Data manipulation with Pandas
- Astronomical data access with Astroquery
- Astropy for units, coordinates, and time
- SkyField for ephemeris calculations
- SciPy for interpolation, optimization, and curve fitting
- Time series analysis and exoplanet transit detection
- Image fitting and photometry techniques
- LLM API integration for coding assistance
- Version control with Git and GitHub
- Interactive web applications with Streamlit

## How to Cite This Work

If you use this material in your research, teaching, or other work, please cite it appropriately. Here are suggested citation formats:

### APA Style

Ting, Y.-S. (2025). *Coding Essentials for Astronomers*. The Ohio State University. Available at: [repository URL]

### BibTeX

```bibtex
@misc{ting2025coding,
  author = {Ting, Yuan-Sen},
  title = {Coding Essentials for Astronomers},
  year = {2025},
  institution = {The Ohio State University},
  url = {[repository URL]},
  note = {Open educational resource}
}
```

### LaTeX/BibTeX (Alternative)

```bibtex
@online{ting2025coding,
  author = {Yuan-Sen Ting},
  title = {Coding Essentials for Astronomers},
  year = {2025},
  url = {[repository URL]},
  organization = {The Ohio State University},
  urldate = {2025-11-XX}
}
```

### Plain Text Citation

Ting, Y.-S. (2025). Coding Essentials for Astronomers. The Ohio State University. Retrieved from [repository URL]

## Building the Site

To build the static site from Jupyter notebooks:

```bash
python build_site.py
```

This will:
- Execute all Jupyter notebooks
- Convert them to HTML
- Generate the lecture index
- Create the `docs/lectures.json` metadata file

## Contact

For questions or feedback, please contact Yuan-Sen Ting [ting dot 74 at ohio dot edu] at The Ohio State University.


# Materiallogistik

## Shared foundations

`../lecture-foundations` holds the cross-course standard (branding,
slide/tooling conventions, quizkit guides) and shared scripts. Two of them
need a rendered `_site/` and a one-time `uv add --dev playwright`: the
revealjs slide overflow gate
(`uv run ../lecture-foundations/scripts/check_slide_overflow.py`) and the
slide-deck PDF exporter
(`uv run ../lecture-foundations/scripts/create_pdf.py --dir _site/ --output-dir pdf-slides/`).
Check it before solving a problem that smells course-generic — it may
already be solved there, and generic fixes belong there, not here.

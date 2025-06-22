# LaTeX Research Toolkit

Streamlined LaTeX research workflow with automated compilation and AI-assisted editing support.

## Quick Start

```bash
# Install
pip install -e .

# Compile LaTeX
python -m tools.compile

# Watch for changes
python -m tools.compile --watch
```

## Structure

```
├── latex/
│   ├── main.tex              # Main document with modular section support
│   ├── macros.tex            # Global macros and notation
│   ├── references.bib        # Bibliography database
│   ├── sections/             # Individual sections for focused AI editing
│   │   ├── introduction.tex  # Introduction section
│   │   └── methodology.tex   # Methodology section
│   ├── drafts/               # Unused/experimental content
│   ├── pdfs/                 # Generated PDFs
│   └── auxiliary/            # Build artifacts
├── docs/
│   ├── AI_CONTEXT.md         # AI assistant context and instructions
│   └── TASKS.md              # Research tasks and progress tracking
├── references/               # Reference papers organized by category
│   ├── key_papers/           # Core references
│   ├── related_work/         # Literature review papers
│   ├── methodology/          # Method-specific papers
│   └── background/           # General background
├── code/
│   └── compile.py            # Streamlined compilation script
└── pyproject.toml            # Modern project configuration
```

## AI-Assisted Research Features

### Modular Section Editing
- Edit individual sections in `latex/sections/` for focused AI collaboration
- Use `\input{sections/filename}` in main.tex to include sections
- Allows AI to concentrate on specific parts without context overload

### Reference Management
- Store PDF papers in `references/` directory organized by category
- Match filenames to bibliography keys for easy citation
- AI can reference actual papers during writing

### Project Context
- `docs/AI_CONTEXT.md`: Provides research context for AI assistants
- `docs/TASKS.md`: Track progress and coordinate AI collaboration
- Helps maintain consistency across editing sessions

### Draft Management
- `latex/drafts/`: Store unused content rather than deleting
- Preserve experimental approaches for potential future use
- Keep removed sections accessible

## Usage Patterns

### Standard Workflow
```bash
python -m tools.compile        # Compile once
python -m tools.compile --watch # Auto-recompile on changes
```

### AI Collaboration Workflow
1. Update `docs/AI_CONTEXT.md` with current project status
2. Work on individual sections in `latex/sections/`
3. Move unused content to `latex/drafts/`
4. Update `docs/TASKS.md` with progress

### Development
```bash
pip install -e .[dev]         # Install dev tools
black tools/ && ruff check tools/  # Format and lint
```

## LaTeX Features

- **Bibliography**: biber backend with alphabetic style
- **Math Support**: Full AMS packages + custom macros
- **Modular Structure**: Section-based organization
- **Auto-compilation**: Watch mode for rapid iteration

---

**Optimized for AI-assisted academic research workflows.** 
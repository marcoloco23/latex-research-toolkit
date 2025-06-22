# LaTeX Research Project Manager

A comprehensive, AI-assisted research workflow tool for developing academic papers with automated quality assurance, systematic documentation, and rigorous review processes. This tool provides a professional framework for managing LaTeX research projects from conception to publication.

## 🎯 Project Overview

This repository provides a standardized workflow and toolset for AI-assisted academic research and paper development. It includes automated compilation, quality assurance, review tracking, and collaboration tools designed for researchers working with LaTeX documents.

**Key Features**:
- 🤖 **AI-Assisted Research**: Structured workflows for AI collaboration
- 📝 **Automated LaTeX Management**: Smart compilation and error handling  
- 📊 **Review & Task Tracking**: Systematic peer review implementation
- 🔄 **Quality Assurance**: Automated validation and style checking
- 🚀 **Publication Workflow**: From draft to submission-ready documents

## 📁 Current Project Structure

```
├── docs/                    # Project documentation (empty - ready for setup)
├── latex/                   # LaTeX source files
│   ├── sections/           # Individual section files
│   │   └── section.tex     # Main section file
│   ├── auxiliary/          # Auxiliary files (generated during compilation)
│   ├── drafts/             # Draft versions and experiments
│   ├── pdfs/               # Output directory for compiled PDFs
│   ├── main.tex           # Main document structure
│   ├── references.bib     # Bibliography database
│   └── macros.tex         # Global notation and macros
├── code/                   # Python automation scripts
│   └── render_all_tex.py  # LaTeX compilation automation
├── references/            # Literature repository (PDFs)
├── .todo                  # TODO tracking file
├── .gitignore            # Git ignore patterns for LaTeX projects
├── pyproject.toml        # Python project configuration
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🚀 Quick Start & Document Generation

### Prerequisites
- **LaTeX**: TeX Live 2023+ or MacTeX distribution with full package set
- **Biber**: Bibliography processor (included with modern TeX distributions)
- **Python**: 3.8+ with pip (for automation features)
- **Git**: For version control
- **Cursor**: For AI-assisted editing

### Automated Document Generation

#### Method 1: Using Python Automation (Recommended)
```sh
# Install dependencies
pip install -r requirements.txt

# Automated compilation with error handling
python code/render_all_tex.py

# Output will be in latex/pdfs/main.pdf
# Auxiliary files organized in latex/auxiliary/
```

#### Method 2: Manual LaTeX Compilation
```sh
# Navigate to LaTeX directory
cd latex

# Complete compilation with bibliography processing
pdflatex -interaction=nonstopmode main.tex && biber main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex

# Move files manually if needed
mv main.pdf pdfs/
```

## 🤖 AI-Assisted Research Workflow

### Cursor Integration
This framework is optimized for AI-assisted research in Cursor:

1. **Structured File Organization**: Use section-based files in `latex/sections/` for focused AI interactions
2. **Automated Compilation**: `render_all_tex.py` provides immediate feedback on changes
3. **Clean Output Management**: PDFs and auxiliary files are automatically organized
4. **Documentation Framework**: Ready-to-use `docs/` directory for process documentation

### AI Research Best Practices
```sh
# 1. Section-focused editing
# Work on individual sections in latex/sections/ for better AI context

# 2. Automated validation with immediate feedback
python code/render_all_tex.py

# 3. Track progress
# Use .todo file or create docs/TASKS.md for systematic tracking

# 4. Maintain clean workspace
# All auxiliary files automatically moved to latex/auxiliary/
```

## 🔍 Quality Assurance & Compilation Process

### Automated Compilation Features
The `render_all_tex.py` script provides:
- **Complete LaTeX Chain**: pdflatex → biber → pdflatex → pdflatex
- **Error Handling**: Captures and displays compilation errors
- **File Organization**: Moves PDFs to `pdfs/` and auxiliary files to `auxiliary/`
- **Non-interactive Mode**: Runs without manual intervention

### Manual Quality Checks
```sh
# Compilation validation
python code/render_all_tex.py

# Check output
ls -la latex/pdfs/main.pdf

# Review compilation logs (if needed)
cat latex/auxiliary/main.log | grep -i "warning\|error"
```

### Setting Up Documentation Workflow
```sh
# Create documentation structure (optional)
mkdir -p docs
touch docs/TASKS.md docs/REVIEW.md docs/STYLE_GUIDE.md

# Initialize task tracking
echo "# Research Tasks" > docs/TASKS.md
echo "- [ ] Initial draft completion" >> docs/TASKS.md
echo "- [ ] Literature review" >> docs/TASKS.md
echo "- [ ] Peer review integration" >> docs/TASKS.md
```

## 🛠️ Current Automation

### Core Script: `code/render_all_tex.py`
- **Purpose**: Automated LaTeX compilation with proper bibliography processing
- **Features**:
  - Multi-pass compilation (pdflatex → biber → pdflatex → pdflatex)
  - Error capture and reporting
  - Automatic file organization
  - Support for biblatex/biber workflow
- **Usage**: `python code/render_all_tex.py`
- **Output**: Compiled PDF in `latex/pdfs/`, auxiliary files in `latex/auxiliary/`

### Extending the Automation
You can enhance the workflow by adding:

```python
# Example: Extract TODOs from LaTeX files
def extract_todos(latex_dir):
    """Scan LaTeX files for TODO comments"""
    # Implementation here
    pass

# Example: Validate references
def check_references(bib_file):
    """Validate bibliography entries"""
    # Implementation here
    pass
```

## 🔧 Configuration & Customization

### LaTeX Setup
The current `main.tex` structure supports:
- Bibliography with biber
- Cross-references and citations
- Modular sections via `\input{sections/section.tex}`
- Custom macros from `macros.tex`

### Python Configuration
```python
# requirements.txt contains dependencies
# pyproject.toml ready for additional Python tooling
```

### File Organization
- **Source**: `latex/` directory contains all LaTeX files
- **Output**: `pdfs/` for final documents
- **Auxiliary**: `auxiliary/` keeps workspace clean
- **References**: Dedicated `references/` for literature PDFs

## 🚀 Extending for Full Research Workflow

### Optional Enhancements You Can Add

#### Documentation System
```sh
# Create comprehensive docs structure
mkdir -p docs
echo "# Project Style Guide" > docs/STYLE_GUIDE.md
echo "# Review Process" > docs/REVIEW.md
echo "# Contributing Guidelines" > docs/CONTRIBUTING.md
```

#### Advanced Automation
```python
# Add to code/ directory:
# - extract_todos.py: Scan for TODO comments
# - validate_refs.py: Check bibliography completeness
# - format_check.py: Verify LaTeX formatting
# - build_check.py: Automated quality gates
```

#### Version Control Integration
```sh
# Enhanced .gitignore already included
# Add pre-commit hooks for compilation validation
# Set up automated builds on commits
```

## 🛠️ Troubleshooting

### Common LaTeX Issues
```sh
# Missing packages
sudo tlmgr update --self && sudo tlmgr install <package>

# Bibliography problems  
cd latex && biber --cache  # Clear cache

# Compilation errors
python code/render_all_tex.py  # Check error output
```

### Python Script Issues
```sh
# Dependency problems
pip install -r requirements.txt --upgrade

# Path issues
# Script uses relative paths from code/ directory
```

### File Organization Issues
```sh
# Reset file organization
cd latex
mkdir -p pdfs auxiliary
# Run compilation script to reorganize files
python ../code/render_all_tex.py
```

## 📈 Advanced Features You Can Implement

### CI/CD Pipeline
- Automated compilation on commits
- Quality gate enforcement  
- Publication-ready builds

### Research Management
- TODO extraction and tracking
- Reference validation
- Style guide enforcement
- Multi-format output generation

### AI Integration Enhancements
- Prompt templates for different research tasks
- Automated literature review assistance
- Section-specific AI workflows
- Quality assurance automation

## 📚 Current File Details

### LaTeX Files
- `main.tex`: Main document (11KB, 255 lines)
- `macros.tex`: Global definitions (215B, 3 lines)  
- `references.bib`: Bibliography database (empty, ready for references)
- `sections/section.tex`: Main content section (empty, ready for content)

### Python Scripts
- `render_all_tex.py`: Compilation automation (3.3KB, 111 lines)

### Configuration
- `requirements.txt`: Python dependencies (573B, 20 lines)
- `pyproject.toml`: Python project setup (empty, ready for configuration)
- `.gitignore`: LaTeX-optimized ignore patterns (500B, 55 lines)

---

**This framework provides a clean, automated foundation for LaTeX research projects with AI assistance. The current setup focuses on robust compilation and file organization, ready for extension with additional research workflow tools.** 
# Contributing Guide

## Getting Started

### Prerequisites
- LaTeX distribution (TeX Live or MacTeX)
- Python 3.8+ with required packages
- Git for version control
- Text editor with LaTeX support (recommended: VS Code with LaTeX Workshop)

### Initial Setup
1. Clone the repository
2. Install Python dependencies: `pip install -r requirements.txt`
3. Test LaTeX compilation: `python code/render_all_tex.py`
4. Review the style guide: `docs/STYLE_GUIDE.md`

## Workflow

### For Section Reviews
1. **Pick a section** from `docs/TASKS.md`
2. **Create a branch**: `git checkout -b review/section-name`
3. **Review systematically**:
   - Technical accuracy and mathematical correctness
   - Consistency with style guide
   - Cross-references and citations
   - Integration with other sections
4. **Document findings** in `docs/REVIEW_LOG.md`
5. **Make corrections** following style guide
6. **Test compilation**: Ensure PDF builds without errors
7. **Create pull request** with detailed description of changes

### For New Content
1. **Check `docs/TASKS.md`** for planned additions
2. **Create feature branch**: `git checkout -b feature/description`
3. **Follow style guide** for all new content
4. **Add appropriate labels** and cross-references
5. **Update relevant documentation** if needed
6. **Test thoroughly** before submitting

### For Bug Fixes
1. **Document the issue** clearly
2. **Create bugfix branch**: `git checkout -b fix/issue-description`
3. **Make minimal changes** to address the specific issue
4. **Test compilation** and verify fix
5. **Update REVIEW_LOG.md** with fix details

## Code Standards

### Python Scripts
- **Type hints**: All functions must have complete type annotations
- **Docstrings**: Use Google-style docstrings for all functions and classes
- **Imports**: Group as stdlib, third-party, internal (enforced by ruff)
- **Error handling**: Provide informative error messages
- **CLI interfaces**: Use `argparse` for command-line tools

### LaTeX Code
- **Follow style guide**: See `docs/STYLE_GUIDE.md`
- **Test compilation**: Always verify PDF builds correctly
- **Check references**: Ensure all `\autoref` and `\cite` commands work
- **Use macros**: Define notation in `macros.tex`
- **Comment complex equations**: Add explanatory comments

## Testing and Quality

### Before Committing
- [ ] Run TODO extraction: `python code/extract_todos.py`
- [ ] Test LaTeX compilation: `python code/render_all_tex.py`
- [ ] Check for undefined references in PDF
- [ ] Verify Python scripts pass type checking
- [ ] Update relevant documentation

### Pull Request Checklist
- [ ] Branch is up to date with main
- [ ] All tests pass locally
- [ ] Changes are documented in REVIEW_LOG.md
- [ ] Style guide is followed
- [ ] No merge conflicts
- [ ] Clear description of changes provided

## Review Process

### Self-Review
1. **Read your changes** completely before submitting
2. **Check integration** with existing content
3. **Verify all references** work correctly
4. **Test edge cases** for any scripts modified

### Peer Review
1. **Focus on content quality** and technical accuracy
2. **Check style compliance** against documented standards
3. **Test functionality** by building the PDF
4. **Provide constructive feedback** with specific suggestions

### Review Priorities
1. **Correctness**: Mathematical and physical accuracy
2. **Clarity**: Readability and logical flow
3. **Consistency**: Adherence to style guide
4. **Integration**: How well changes fit with existing content

## Communication

### Issues and Discussions
- **Use GitHub issues** for bugs and feature requests
- **Reference specific sections** or line numbers when reporting problems
- **Provide context** and steps to reproduce issues
- **Tag appropriately** (bug, enhancement, question, etc.)

### Commit Messages
Format: `type(scope): brief description`

Examples:
- `feat(latex): add emergent gravity derivation`
- `fix(build): resolve bibliography compilation error`
- `docs(review): update style guide for math notation`
- `refactor(structure): reorganize sections directory`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Tools and Automation

### Available Scripts
- `code/render_all_tex.py`: Compile all LaTeX documents
- `code/extract_todos.py`: Generate `.todo` file with all outstanding items
- `code/entropy.py`: Utility functions for physics calculations

### GitHub Actions
- **Build verification**: Automatic PDF compilation on all PRs
- **Style checking**: Python code quality enforcement
- **TODO tracking**: Automatic update of `.todo` file

### Recommended Tools
- **LaTeX editing**: VS Code with LaTeX Workshop extension
- **Python development**: VS Code with Python extension
- **PDF viewing**: Built-in preview or Skim (macOS)
- **Git interface**: Command line or GitHub Desktop

---

## Getting Help

- **Style questions**: Refer to `docs/STYLE_GUIDE.md`
- **Task priorities**: Check `docs/TASKS.md`
- **Technical issues**: Create GitHub issue with reproduction steps
- **LaTeX problems**: Check compilation logs in `latex/auxiliary/`

*This guide evolves with the project. Suggest improvements via GitHub issues.* 
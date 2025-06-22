# AI Context & Project Reference

This document provides context for AI assistants working on this research project.

## AI Agent Rules Available

This project includes specialized AI agent instructions in `.cursor/rules/`:
- **researcher.mdc**: Literature review, methodology design, citation management
- **writer.mdc**: Academic writing, structure, clarity optimization  
- **editor.mdc**: Revision, polishing, consistency checking
- **reviewer.mdc**: Critical evaluation, peer review, quality assessment
- **expert.mdc**: Domain expertise, strategic guidance, methodology validation

See `.cursor/rules/README.md` for detailed usage instructions.

## Project Overview

**Research Topic**: [Fill in your research area]
**Main Objective**: [State primary research goal]
**Key Methods**: [List main approaches/methodologies]

## Current Status

- **Phase**: [Planning/Data Collection/Analysis/Writing/Revision]
- **Priority Sections**: [Which sections need immediate attention]
- **Deadlines**: [Important dates]

## Key Concepts & Terminology

| Term | Definition | Usage Notes |
|------|------------|-------------|
| Key Term 1 | Definition | How it's used in this work |
| Key Term 2 | Definition | Special considerations |

## Writing Style & Preferences

- **Voice**: [First person / Third person / Passive]
- **Citation Style**: alphabetic (biblatex)
- **Math Notation**: [Specific conventions used]
- **Abbreviations**: [Project-specific abbreviations]

## Section-Specific Notes

### Introduction
- **Focus**: Problem statement, motivation, contributions
- **Length**: ~2 pages
- **Key Points**: [List main arguments]

### Methodology  
- **Focus**: Experimental design, analysis methods
- **Technical Level**: [Beginner/Intermediate/Advanced]
- **Key Equations**: [Reference important formulas]

### Results
- **Format**: Tables and figures with explanations
- **Statistical Tests**: [Methods used]
- **Significance Threshold**: p < 0.05

## Common Instructions for AI

1. **When editing sections**: Focus on one section at a time using files in `latex/sections/`
2. **For references**: Check `references/` directory for source papers
3. **Citation format**: Use `\cite{key}` with keys from `references.bib`
4. **Math notation**: Follow conventions in `macros.tex`
5. **Unused content**: Move to `latex/drafts/` rather than deleting
6. **Agent Selection**: Use appropriate AI agent from `.cursor/rules/` for specific tasks

## Current Research Questions

1. [Primary research question]
2. [Secondary research question]
3. [Open questions to explore]

## Resources & References

- **Key Papers**: [List 3-5 most important references]
- **Datasets**: [Data sources used]
- **Code Repositories**: [Links to relevant code]

---

*Last Updated*: [Date]
*Next Review*: [Date] 
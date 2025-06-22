# AI Agent Rules for Research Excellence

This directory contains specialized instruction sets for different AI agent roles in academic research. Each agent has specific expertise and responsibilities to optimize research workflow.

## Agent Overview

| Agent | Primary Role | Use When |
|-------|-------------|----------|
| **Researcher** | Literature review, methodology design | Starting new research, literature gaps |
| **Writer** | Academic writing, structure, clarity | Drafting sections, improving flow |
| **Editor** | Revision, polishing, consistency | Final refinement, proofreading |
| **Reviewer** | Critical evaluation, peer review | Quality assessment, feedback |
| **Expert** | Domain expertise, strategic guidance | High-level decisions, methodology validation |

## How to Use Agent Rules

### In Cursor Chat
1. **Select Agent Role**: Reference the appropriate `.mdc` file
2. **Provide Context**: Share relevant project files (`docs/AI_CONTEXT.md`)
3. **Specify Task**: Be clear about what you need from this agent
4. **Follow Guidelines**: The agent will follow its specialized instructions

### Example Usage

#### Starting Literature Review
```
@researcher.mdc
I need help with literature review for my research on [topic]. 
Please check docs/AI_CONTEXT.md for project context and 
help me identify key papers and research gaps.
```

#### Improving Writing Quality
```
@writer.mdc  
Please help improve the introduction section in 
latex/sections/introduction.tex. Focus on clarity 
and logical flow according to academic writing standards.
```

#### Final Manuscript Review
```
@reviewer.mdc
Please provide a comprehensive peer review of my complete 
manuscript. Check all sections for quality, methodology, 
and publication readiness.
```

## Research Workflow Integration

### Phase 1: Research Planning
- **Expert**: Strategic direction and methodology selection
- **Researcher**: Literature review and gap analysis

### Phase 2: Content Development  
- **Writer**: Section drafting and structure
- **Researcher**: Method validation and citation management

### Phase 3: Refinement
- **Editor**: Language improvement and consistency
- **Writer**: Flow optimization and clarity

### Phase 4: Quality Assurance
- **Reviewer**: Critical evaluation and peer review
- **Expert**: Final validation and publication strategy

## Agent-Specific Strengths

### Researcher Agent
- **Best for**: Literature synthesis, methodology design
- **Expertise**: Citation management, research gaps
- **Output**: Comprehensive literature reviews, research plans

### Writer Agent  
- **Best for**: Clear academic writing, section structure
- **Expertise**: Paragraph organization, academic style
- **Output**: Well-structured, readable research text

### Editor Agent
- **Best for**: Language polish, consistency checking
- **Expertise**: Grammar, technical accuracy, formatting
- **Output**: Publication-ready, error-free manuscripts

### Reviewer Agent
- **Best for**: Critical evaluation, quality assessment
- **Expertise**: Peer review standards, constructive feedback
- **Output**: Detailed reviews with improvement suggestions

### Expert Agent
- **Best for**: Strategic guidance, methodological innovation
- **Expertise**: Domain knowledge, publication strategy
- **Output**: High-level insights and research direction

## Collaborative Agent Usage

### Multi-Agent Workflow
1. **Expert** provides strategic direction
2. **Researcher** conducts literature review
3. **Writer** drafts sections
4. **Editor** refines language and style
5. **Reviewer** provides final quality check

### Agent Handoffs
- Pass context between agents using project documentation
- Update `docs/TASKS.md` with progress from each agent
- Use `latex/drafts/` to preserve different agent contributions

## Quality Assurance

### Each Agent Ensures
- **Consistency** with project context (`docs/AI_CONTEXT.md`)
- **Integration** with existing work
- **Progress Tracking** in `docs/TASKS.md`
- **Quality Standards** according to their specialization

### Combined Excellence
When used together, these agents provide:
- Comprehensive research coverage
- Multiple quality checks
- Specialized expertise at each stage
- Consistent, high-quality output

## Tips for Maximum Effectiveness

1. **Match Agent to Task**: Use the right specialist for each job
2. **Provide Context**: Always share `docs/AI_CONTEXT.md`
3. **Sequential Use**: Follow logical workflow progression
4. **Document Progress**: Update `docs/TASKS.md` after each agent
5. **Preserve Work**: Use `latex/drafts/` for version control

---

**Select the right AI agent for each research task to achieve academic excellence.** 
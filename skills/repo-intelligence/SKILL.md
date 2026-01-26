---
name: repo-intelligence
description: Analyze public GitHub repositories to return structured technical intelligence including architecture, tech stack, folder mapping, setup instructions, and risk flags. Use this skill when a user asks to understand a codebase, analyze a repo, or needs a technical overview of a project from a URL.
---

# Repo Intelligence

Analyze the provided GitHub repository and return a structured technical intelligence report.

## Input Parameters

### Required
- `repo_url`: Public GitHub repository URL string.

### Optional
- `analysis_depth`: "quick" (default) for metadata/top-level scan, or "deep" for full tree/dependency analysis.
- `include_security_scan`: Boolean (default: true).
- `include_improvement_suggestions`: Boolean (default: true).

## Behavior Rules

1. **Always return valid JSON output.**
2. Never hallucinate files, frameworks, or dependencies; base all conclusions on detected content.
3. Use neutral, technical language favoring explicit detection over inference.
4. Mark unknown values as `null`.
5. Keep output developer-focused and under 1500 tokens.
6. Do not include markdown formatting inside JSON fields.

## Analysis Pipeline

Follow these steps strictly:

### 1. Repository Inspection
**Strategy**: Prioritize GitHub API endpoints over web scraping for structured data.

1. **Fetch Complete Structure**: Call `https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1` (try `main` or `master`) to get a full recursive file tree. This is the most efficient way to understand the entire project structure at once.
2. **Directory Browsing**: Use `https://api.github.com/repos/{owner}/{repo}/contents/{path}` to inspect specific directories if the tree is unavailable or to get metadata for specific files.
3. **Analyze Key Files**: Using the `download_url` or `raw` links from the API response, read:
   - Root files (README, license)
   - Configuration (package.json, pyproject.toml, go.mod, etc.)
   - Infrastructure (Dockerfile, docker-compose.yml)
   - CI/CD (.github/workflows)

### 2. Classification
Detect:
- **Project Type**: frontend, backend, fullstack, monorepo, library, cli, or unknown.
- **Primary Languages & Frameworks**.
- **Runtime Environment**.

### 3. Architecture Summary
Generate a concise (3-5 sentences) technical summary determining application structure, layer separation, major components, and identifiable data flow.

### 4. Folder Purpose Mapping
Map key directories to human-readable responsibilities (e.g., `/app` -> UI routing, `/services` -> Business logic). Exclude trivial folders like `node_modules`.

### 5. Setup Guide Generation
Infer setup steps from README, scripts, and configs. Generate install commands, environment setup notes, dev run commands, and build commands.

### 6. Risk Detection (if enabled)
Scan for:
- **Security**: Hardcoded secrets, missing .env.example, exposed tokens.
- **Maintainability**: Missing tests/linting/CI, deprecated dependencies, unstructured folders.
Categorize as HIGH, MEDIUM, or LOW.

### 7. Improvement Suggestions (if enabled)
Suggest improvements for developer experience, CI/CD, structure, code quality, and observability based on evidence.

## Output Schema

Return a single JSON object matching this structure:

```json
{
  "project_overview": {
    "name": "",
    "project_type": "",
    "primary_language": "",
    "frameworks": [],
    "runtime": ""
  },
  "architecture_summary": "",
  "tech_stack": {
    "frontend": null,
    "backend": null,
    "database": null,
    "auth": null,
    "deployment": null
  },
  "folder_map": [
    {
      "path": "",
      "purpose": ""
    }
  ],
  "setup_guide": {
    "install_steps": [],
    "environment_setup": [],
    "run_commands": [],
    "build_commands": []
  },
  "risks": [
    {
      "level": "HIGH|MEDIUM|LOW",
      "category": "",
      "description": ""
    }
  ],
  "improvement_suggestions": [],
  "confidence_notes": []
}
```

### Confidence Notes Rules
If uncertain about any detection, add a string to the `confidence_notes` array explaining the limitation (e.g., "Database type could not be confirmed single file analysis.").

## Failure Handling

If the repository is inaccessible or invalid, return:

```json
{
  "error": "Repository could not be accessed or analyzed."
}
```

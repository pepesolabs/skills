# Agent Skills

This repository contains custom skills for AI agents to boost productivity, save time, and improve code quality.

## Skills

- **Repo Intelligence**: Structured technical analysis of GitHub repositories.
- **UI Style Replicator**: Workflow for replicating UI designs from reference images.

## Installation

### For Claude Desktop / Custom Agents

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pepesolabs/skills.git
   ```

2. **Register the Skills**:
   Point your agent configuration to the `skills` directory or specific `SKILL.md` files you want to enable.

### For Plugin-Compatible Agents

This repository includes a `.claude-plugin/marketplace.json` manifest. You can add this repository URL directly to compatible agent configuration files to automatically discover and load the skills.

## Structure

This repository follows the structure required for sharing skills:

- `.claude-plugin/marketplace.json`: Manifest file defining the available skills.
- `skills/`: Directory containing individual skill folders.
  - `skills/[skill-name]/SKILL.md`: The definition file for each skill.

## Usage

These skills are designed to be loaded by Claude or compatible agentic workflows.

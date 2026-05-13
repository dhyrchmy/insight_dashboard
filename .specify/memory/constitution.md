<!-- Sync Impact Report:
Version Change: 0.0.0 → 1.0.0
Added: 5 core principles, Technology Stack section, Development Workflow section
Removed: All template placeholders
Templates: ✅ plan-template.md, spec-template.md, tasks-template.md - all aligned (no constitution-specific references to update)
-->

# Insight Dashboard Constitution

## Core Principles

### I. Statistical Computing
All statistical computations MUST use numpy/scipy libraries; manual implementations of statistical functions are prohibited. This ensures reliable, optimized, and testable statistical operations.

### II. Local-First Resources
Chart.js MUST be bundled locally within the project; CDN dependencies are prohibited. This ensures offline capability and eliminates external dependency risks.

### III. Self-Contained Data
The application MUST auto-generate a sample CSV file containing 1 year of hourly data (timestamp, temperature, humidity, pressure) when no CSV file is provided. This ensures the dashboard works out-of-the-box without manual data preparation.

### IV. Test Coverage Enforcement (NON-NEGOTIABLE)
The statistics module MUST maintain a minimum of 70% test coverage. All statistical functions require comprehensive test coverage before implementation is considered complete.

### V. Atomic Git Workflow
Every git commit MUST represent exactly one task. Multi-feature or multi-task commits are prohibited. This ensures granular traceability and simplifies rollback operations.

## Technology Stack

**Backend**: FastAPI (Python web framework)
**Frontend**: Chart.js (bundled locally)
**Data Processing**: pandas, numpy, scipy

## Development Workflow

**Commit Rules**:
- One task per commit
- Commit message MUST describe the specific task completed
- Tests MUST be committed alongside implementation

**Coverage Requirements**:
- Statistics module: minimum 70% coverage
- Coverage reports MUST be generated and reviewed

**Data Handling**:
- Sample CSV auto-generation for empty/missing data
- CSV format: timestamp, temperature, humidity, pressure

## Governance

All PRs and reviews MUST verify compliance with core principles. The constitution supersedes all other practices; amendments require documentation and approval.

**Version**: 1.0.0 | **Ratified**: 2026-05-13 | **Last Amended**: 2026-05-13
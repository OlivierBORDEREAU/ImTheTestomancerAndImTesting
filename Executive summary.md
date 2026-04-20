# Testomancer – Summary

**Testomancer** is a lightweight, production-ready skill for the Opencode AI agent framework that instantly turns any general-purpose LLM agent into a **senior ISTQB-aligned software testing expert**.

## Problem
AI agents frequently generate tests that are:
- Over-engineered or poorly isolated
- At the wrong level (unit vs integration vs E2E)
- Non-compliant with industry standards

## Solution
Testomancer provides structured, professional testing guidance grounded in three proven frameworks:

| Framework              | Contribution |
|------------------------|--------------|
| **ISTQB**              | Industry-standard terminology and best practices |
| **Testing Pyramid**    | Disciplined distribution (more Unit, fewer E2E) |
| **Karpathy Guidelines**| Test-first mindset, surgical changes, explicit assumptions, verifiable success criteria |

## Key Features
- Real-time codebase analysis and tech-stack detection
- Risk-based testing strategy and prioritization
- Level-specific recommendations with library suggestions
- Ready-to-use code templates and CI/CD guidance
- File Backup Protocol — timestamped backups before any modification (`testomancer/backup/`)

## Business Impact

| Metric              | Expected Improvement                  |
|---------------------|---------------------------------------|
| Test Coverage       | Target >80% on critical paths         |
| Execution Time      | Faster via pyramid discipline         |
| Maintenance         | Lower through simpler, surgical tests |
| Compliance & Quality| Fully ISTQB-aligned outputs           |
| Safety             | Timestamped backups prevent data loss   |

## Roadmap (Open Source)

### Core Integrations
- Playwright-mcp, Appium-mcp, Playwright-cli, rf-mcp

### Test Generation
- Auto-generate tests from Gherkin/OpenAPI/Postman, DB schema validation

### AI-Powered Maintenance
- Auto-fix flaky tests, coverage gap detection, auto-update on code changes

### Reporting & CI/CD
- HTML/JSON reports, GitHub Actions/GitLab CI templates

### Test Data
- Synthetic data generation, fixture management, PII masking

### Quality & Performance
- Duplicate test detection, slow test identification, parallelization

### Specialized Testing
- OWASP security tests, load/performance, accessibility

### Documentation
- Auto-generate test docs, test case export, coverage reports

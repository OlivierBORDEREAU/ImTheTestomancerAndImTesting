# Testomancer – Summary

**Testomancer** is a specialized AI skill that transforms any AI agent (like Opencode) into a senior software testing expert.

---

## Problem

AI agents generate tests that are often:

- Over-engineered or poorly isolated
- Missing the right testing level (unit vs integration vs E2E)
- Non-compliant with industry standards

---

## Solution

Testomancer provides structured **testing strategy and implementation guidance** aligned with:

| Framework | What It Provides |
|----------|-----------------|
| **ISTQB** | Industry-standard terminology (Component → Integration → System → Acceptance Testing) |
| **Testing Pyramid** | Distribution discipline: 70% Unit / 20% Integration / 10% E2E |
| **Karpathy Guidelines** | AI behavior rules: simplicity, surgical changes, explicit assumptions |

---

## Key Features

- **Codebase Analysis** – Detects languages, frameworks, existing coverage
- **Best Practices Audit** – Compliance checking
- **Level Recommendations** – Unit, Integration, Functional, or E2E with justification
- **Library Suggestions** – Framework-specific recommendations (Playwright, Jest, pytest, etc.)
- **Code Templates** – Jumpstart implementation
- **Risk-Based Testing** – Prioritizes high-risk areas (auth, payments, data validation, PII)
- **File Backup Protocol** – Timestamped backups before any modification (`testomancer/backup/`)

---

## Impact

| Metric | Expected Improvement |
|--------|-----------------|
| Test Coverage | Target >80% on critical code |
| Test Execution Time | Faster via pyramid distribution |
| Maintenance | Lower via simpler, surgical tests |
| Compliance | ISTQB-aligned documentation |
| Safety | Timestamped backups prevent data loss |

---

## Roadmap

### Core Integrations
- [ ] Integration with Playwright-mcp for web automation
- [ ] Integration with Appium-mcp for mobile testing
- [ ] Integration with Playwright-cli for browser interactions
- [ ] Integration with rf-mcp for Robot Framework support

### Test Generation
- [ ] Auto-generate functional/E2E tests from test cases (normal or Gherkin)
- [ ] Auto-generate tests from OpenAPI/Swagger specs
- [ ] Generate tests from Postman collections
- [ ] Database schema → data validation tests

### AI-Powered Maintenance
- [ ] Auto-fix flaky tests
- [ ] Detect test coverage gaps
- [ ] Auto-update tests on code changes

### Reporting & CI/CD
- [ ] HTML/JSON test reports
- [ ] GitHub Actions / GitLab CI templates
- [ ] Test execution analytics

### Test Data
- [ ] Synthetic data generation
- [ ] Test fixture management
- [ ] Data masking for PII

### Quality & Performance
- [ ] Duplicate test detection
- [ ] Slow test identification
- [ ] Test parallelization suggestions

### Specialized Testing
- [ ] Basic OWASP security tests
- [ ] Load/performance test templates
- [ ] Accessibility (a11y) test templates

### Documentation
- [ ] Auto-generate test documentation
- [ ] Test case specification export
- [ ] Coverage reports export

---

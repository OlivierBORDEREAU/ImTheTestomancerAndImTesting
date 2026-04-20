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

- [ ] Appsec integration
- [ ] Remote execution via ContinuousTesting (Digital.AI)

---

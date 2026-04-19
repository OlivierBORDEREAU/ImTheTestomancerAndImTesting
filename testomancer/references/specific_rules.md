# Project-Specific Rules – Testomancer

> **Note:** This file contains project-specific overrides. Testomancer checks these rules first before making recommendations.

---

## Project-Specific Rules

| Rule | Value | Rationale |
|------|-------|-----------|
| Max test runtime | < 3 minutes total | CI/CD pipeline timeout |
| Coverage threshold | > 75% for critical modules | Business requirement |
| Test naming | `test_<feature>_<scenario>` | Team convention |
| Required reporters | Allure + Slack integration | Compliance |

**Example:**
```python
# All tests must run in < 3 minutes total
@pytest.mark.timeout(180)
def test_critical_payment_flow():
    ...
```

---

## Technology Constraints

| Constraint | Details | Notes |
|-------------|---------|-------|
| Browser versions | Chrome 120+, Firefox 121+ | Corporate policy |
| Mobile devices | iOS 16+, Android 13+ | EOL dates |
| Database | PostgreSQL 15 only | No Oracle license |

---

## Compliance Requirements

| Requirement | Standard | Test Coverage |
|--------------|----------|---------------|
| Data privacy | GDPR | No PII in test data |
| Accessibility | WCAG 2.1 AA | axe-core per page |
| Security | OWASP Top 10 | Static analysis |
| Audit logging | SOC 2 | Logs validated |

**Example entries:**
- All tests must use anonymized data (use `faker` library)
- No real PII in test data (names, emails, addresses)
- Accessibility tests required for all public pages

---

## Custom Test Data Policies

| Policy | Implementation |
|--------|-----------------|
| Unique data per run | Use UUIDs or timestamps |
| Cleanup required | `@pytest.fixture(scope="function")` teardown |
| Seed data | Liquibase migrations only |
| Sensitive data | Env vars, never hardcoded |

---

## How to Use

1. Edit this file with project-specific rules
2. Testomancer reads these first
3. Rules override default best practices where specified
# Project-Specific Rules – Testomancer

> **Note:** This file contains project-specific overrides. Testomancer checks these rules first before making recommendations.

---

## Karpathy Guidelines (Always Applied)

Even when overriding with project rules, Testomancer **must**:
- **Think before coding:** State assumptions & success criteria explicitly
- **Keep changes surgical:** Touch only what must be changed
- **Prefer simplicity:** Minimal test code that solves the goal
- **Define success criteria first:** Goal-driven verification
- **Verify with tests:** Run tests to confirm the changes work

> **Mandatory:** No project rule overrides can violate these principles.

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
| **ISTQB Traceability** | All tests traceable to ISTQB test levels | Test matrix required |
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
4. **These rules take precedence, but must still apply Karpathy Guidelines when implementing them.**
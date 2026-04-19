# Unit Tests – Testomancer

> **ISTQB Mapping:** Aligns with **Component Testing** in ISTQB terminology.
> **Karpathy Guidelines:** All generated unit test code must strictly follow `karpathy-guidelines.md` — keep tests minimal and surgical. One assertion per test where possible. Define success criteria before writing any test code.

**Definition**  
Tests that verify a single unit of code (function, method, or class) in complete isolation.

**When to Prioritize**  
- Complex business logic  
- Algorithms and calculations  
- Validation rules  
- Any logic that can be tested without external dependencies

**Codebase Analysis for This Level**  
Look for: pure functions, classes with few dependencies, business logic modules.

**Recommended Stack (2026)**

| Language    | Main Framework              | Complementary Tools             | Why Recommended |
|-------------|-----------------------------|----------------------------------|-----------------|
| Python      | pytest + pytest-asyncio     | hypothesis, pytest-cov           | Most powerful & flexible |
| JavaScript/TypeScript | Vitest (preferred) or Jest | Testing Library (for React)      | Speed + native ESM |
| Java        | JUnit 5 + Mockito           | AssertJ                          | Enterprise standard |

**Coverage Targets**

| Scope | Target | Notes |
|-------|--------|-------|
| Critical paths | >80% statement coverage | Business logic, algorithms |
| Critical paths | >80% branch coverage | Decision points |
| All units | >60% overall coverage | Baseline for new projects |
| Edge cases | 100% coverage |Boundary values, nulls |

**Test Doubles Strategy**

| Situation | Use | Avoid |
|-----------|-----|-------|
| External API calls | Mock (e.g., requests-mock) | Real HTTP calls |
| Database queries | Fake (in-memory) | Mocking repository |
| Time/date functions | Stub/Patch | Frozen time |
| Random values | Seeded random | Mocking random |

- **Mock:** Replace external dependency with controlled implementation
- **Fake:** Lightweight in-memory implementation (e.g., SQLite vs PostgreSQL)
- **Stub:** Pre-programmed responses for specific inputs
- **Spy:** Wrap existing object to capture calls

**Property-Based Testing**

| Language | Library | Example |
|----------|--------|---------|
| Python | Hypothesis | `@given(st.integers(min_value=0))` |
| JavaScript/TypeScript | fast-check | `fc.property(fc.integer(), ...)` |
| Java | jqwik | `@Property` annotation |

Example (Python + Hypothesis):
```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers(min_value=0, max_value=100)))
def test_sort_integers(unsorted):
    sorted_list = sort(unsorted)
    assert sorted_list == sorted(unsorted)
    assert len(sorted_list) == len(unsorted)
```

Example (JS + fast-check):
```javascript
import { property, integer } from 'fast-check';

property('sort integers', integer(0, 100).array(), (arr) => {
  const sorted = sort([...arr]);
  return sorted.every((x, i) => i === 0 || sorted[i-1] <= x);
});
```

**Anti-patterns**

- ❌ Testing private methods directly (test via public interface)
- ❌ Over-mocking (replacing everything, losing integration signal)
- ❌ One test for ten assertions (split for clarity)
- ❌ Hardcoded dates/times (use test fixtures)
- ❌ Testing external library behavior (mock the library, not your code)

**Automation Tools**  
- GitHub Actions / GitLab CI / Jenkins  
- Pre-commit hooks + Husky (for JS/TS)  
- Automatic coverage reports + badges

**Prompt Template to Use** (Karpathy-enforced)

Follow Karpathy: think step-by-step, keep changes surgical, verify success criteria first.

Input:
```
"Analyze this module [paste code]. Generate unit tests using [framework]. Cover nominal cases, edge cases, error cases, and property-based tests where applicable. Follow Karpathy: simplicity first, surgical changes only, and include verification steps."
```

Example Input:
```
"Generate unit tests for a Python function that calculates factorial. Use pytest and include property-based tests with Hypothesis."
```

Example Output:
```python
import pytest
from hypothesis import given, strategies as st

def factorial(n):
    if n < 0:
        raise ValueError("Negative input")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Nominal cases
def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_five():
    assert factorial(5) == 120

# Edge cases
def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

# Property-based
@given(st.integers(min_value=2, max_value=20))
def test_factorial_property(n):
    assert factorial(n) == factorial(n - 1) * n
```

**Best Practices** (Karpathy-enforced)

- **State test goal + assumptions explicitly** before each test suite (Karpathy goal-driven)
- **Prefer minimal, clear tests (10 lines instead of 50)** — avoid over-engineering
- **State assumptions explicitly** (e.g., "Assuming `UserRepository` is mocked")
- One assertion per test when possible
- Use AAA (Arrange-Act-Assert) or Given-When-Then naming
- Parameterized tests
- Avoid unnecessary mocks on simple objects
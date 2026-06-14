# Best Practices – Testomancer

> **Goal:** Provide language-specific and cross-cutting testing standards that align with ISTQB principles and modern (2026) practices.

## Universal Rules

- Tests must be **fast, isolated, and deterministic**.
- Follow the Testing Pyramid: ~70% unit, ~20% integration, ~10% E2E.
- Target >80% coverage on critical paths (business logic, security, financial flows).
- Use clear naming: `test_<feature>_<scenario>` or behavior-driven style.
- Never hardcode secrets or sensitive data in tests.

## Python

**Recommended stack:** pytest + pytest-asyncio + hypothesis (property-based)

**Key rules:**
- Use type hints everywhere.
- Prefer Pydantic models over plain dicts.
- Use dependency injection instead of global state.
- Keep fixtures focused and minimal.
- Use `assert` statements (pytest style).

**Good example:**
```python
def test_create_user_valid_data(user_repository):
    user = create_user(UserCreate(email="a@b.com"), user_repository)
    assert user.email == "a@b.com"
```

## TypeScript / React

**Recommended stack:** Vitest + Testing Library + user-event

**Key rules:**
- Enable strict TypeScript.
- Test user behavior, not implementation details.
- Prefer `userEvent` over `fireEvent`.
- Extract complex logic into custom hooks.

## Java (Spring Boot)

**Recommended stack:** JUnit 5 + AssertJ + Testcontainers

**Key rules:**
- Use constructor injection.
- Prefer records for DTOs.
- Use Testcontainers for real dependencies instead of heavy mocking when practical.

## .NET

**Recommended stack:** xUnit + FluentAssertions + WebApplicationFactory / Testcontainers

**Key rules:**
- Use primary constructors and records.
- Avoid `async void`.
- Prefer `async Task` methods.

## Go

**Recommended stack:** Standard testing + testify + table-driven tests

**Key rules:**
- Use `t.Run` for subtests.
- Prefer table-driven tests for multiple cases.
- Keep test files in the same package (`_test.go`).

## High-Risk Areas (Always Prioritize)

- Authentication & authorization
- Payment and financial logic
- Data validation and sanitization
- External API integrations
- User data handling (GDPR, PII)
- Critical business workflows

When analyzing code, flag these areas first.
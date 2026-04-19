# Best Practices Compliance Checks – Testomancer

> **External Standards:** This file aligns with [ISTQB](https://www.istqb.org/) testing best practices and the [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) for security-related tests.

Before recommending tests, audit the codebase against modern language-specific standards (2026).
Highlight violations with examples and suggest fixes.
Overarching Principle: Follow Karpathy Guidelines for all test code suggestions.

---

## Cross-Language Best Practices (All Languages)

| Principle | Description | Reference |
|-----------|-------------|-----------|
| **DRY** | Don't Repeat Yourself – shared test utilities, fixtures | - |
| **Naming** | `test_<feature>_<scenario>` or `it should <behavior>` | ISTQB |
| **CI Reporting** | Allure, ReportPortal, or native CI reporters | - |
| **Security in Tests** | No hardcoded secrets; use env vars or vaults | OWASP |
| **Deterministic** | Tests must be repeatable; avoid time-based race conditions | - |
| **Fast** | Unit tests <100ms; integration <2s | - |

**Extensible Rules**

> **Placeholder for user-specific rules:** Add custom rules in `references/specific_rules.md` (per-project overrides).

---

## Python

**Key Best Practices**
- Follow PEP 8 (use Ruff or Black for formatting)
- Add type hints everywhere (compatible with mypy or pyright)
- Prefer Pydantic models or dataclasses over plain dicts
- Use dependency injection instead of global state
- Proper pytest fixtures (avoid overuse of monkeypatch)
- Async code must use pytest-asyncio

**Example Snippets**

| Good | Bad |
|------|-----|
| `class UserCreate(BaseModel)` typed | `data: dict` plain dict |
| `def create_user(data: UserCreate) -> User` | `def create_user(data)` no hints |
| `from mymodule import DB` injected | Global `db = connect()` |

**Good Practice (Recommended):**
```python
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str
    username: Optional[str] = None

def create_user(user_data: UserCreate, db: Database) -> User:
    # Clear, typed, dependency injected
    ...
```

**Violation Example (to flag):**
```python
def create_user(data):  # Missing type hints
    if not data.get('email'):  # Using plain dict + get()
        raise Error
    # Global db connection used here → bad
```

**Fix Suggestion:** Add type hints, switch to Pydantic, inject DB dependency.

---

## JavaScript / TypeScript (especially with React)

**Key Best Practices**
- Enable strict TypeScript (strict: true in tsconfig)
- Use ESLint + Prettier
- No any type; prefer interfaces or types
- Test components with React Testing Library + user-event (never test implementation details)
- Prefer Vitest in new projects
- Follow React Hooks rules; extract logic into custom hooks

**Example Snippets**

| Good | Bad |
|------|-----|
| `interface Props { onSubmit: (d: Data) => void }` | `Props: any` |
| `userEvent.click()` | `fireEvent.click()` (RTL) |
| Test user behavior | `screen.getByText('hidden')` |
| `Vitest` | Jest (legacy) |

**Good Practice:**
```tsx
// components/UserForm.tsx
import { useState } from 'react';
import { UserFormData } from '@/types';

interface Props {
  onSubmit: (data: UserFormData) => void;
}

export function UserForm({ onSubmit }: Props) {
  const [formData, setFormData] = useState<UserFormData>({...});
  // ...
}
```

**Violation Example:**
```tsx
function UserForm() {
  const [data, setData] = useState<any>({}); // 'any' is forbidden
  // Testing internal state directly instead of user interaction
}
```

**Fix Suggestion:** Add proper interfaces, use userEvent in tests, extract custom hooks.

---

## Java (Spring Boot)

**Key Best Practices**
- Follow Spring recommendations or Google Java Style
- Use records (Java 21+) where possible
- Constructor injection (avoid field injection)
- Proper layering: Controller → Service → Repository
- JUnit 5 + AssertJ (avoid old Hamcrest)
- Use Testcontainers for external services instead of mocks when possible

**Example Snippets**

| Good | Bad |
|------|-----|
| `private final UserRepository repo;` constructor | `@Autowired` field injection |
| `record UserDto(...)` immutable DTO | Plain class with setters |
| AssertJ fluent API | `assertEquals(x, y)` Hamcrest |
| Testcontainers | MockServer for DB |

**Good Practice:**
```java
@Service
@RequiredArgsConstructor
public class UserService {
    private final UserRepository repository; // Constructor injection

    public User createUser(UserCreateDto dto) {
        // ...
    }
}
```

**Violation Example:**
```java
@Service
public class UserService {
    @Autowired
    private UserRepository repository; // Field injection (discouraged)

    public User create(UserCreateDto dto) { ... }
}
```

**Fix Suggestion:** Switch to constructor injection with Lombok @RequiredArgsConstructor or explicit constructor. Use records for DTOs.

---

## .NET (C#)

**Key Best Practices**
- Follow Microsoft .NET coding conventions
- Use records and primary constructors (C# 12+)
- Constructor injection with Microsoft.Extensions.DependencyInjection
- Prefer xUnit.net + FluentAssertions
- Avoid async void; always use async Task
- Use WebApplicationFactory or Testcontainers for integration tests

**Example Snippets**

| Good | Bad |
|------|-----|
| `record UserDto(string Email)` immutable | Class with properties |
| `public async Task<T>` return | `public async void` |
| `FluentAssertions` | `Assert` legacy |
| Primary constructor | Field injection |
| `WebApplicationFactory` | In-memory EF |

**Good Practice:**
```csharp
public record UserCreateDto(string Email, string Password);

public class UserService(ILogger<UserService> logger, IUserRepository repo)
{
    public async Task<User> CreateAsync(UserCreateDto dto)
    {
        // ...
    }
}
```

**Violation Example:**
```csharp
public class UserService
{
    private readonly IUserRepository _repo;

    public UserService(IUserRepository repo)
    {
        _repo = repo;
    }

    public async void Create(UserCreateDto dto) { ... } // async void is dangerous
}
```

**Fix Suggestion:** Use primary constructor syntax, change to async Task, add FluentAssertions in tests.

---

## Go

**Key Best Practices**
- Follow Go code conventions (`go fmt`, `golangci-lint`)
- Use table-driven tests for parameterized cases
- Prefer table-driven `t.Run` subtests
- Use `testify` or `mock` for assertions/mocking
- Use `httpmock` or `httptest` for HTTP testing
- Keep test files in same package with `_test.go` suffix

**Example Snippets**

| Good | Bad |
|------|-----|
| Table-driven subtests | Single monolithic test |
| `t.Run("case name", func(t *testing.T) {...})` | `func TestAll()` with if/else |
| Use `assert` from testify | `t.Fatal` in test body |
| `httptest.NewRecorder()` | Real HTTP calls to localhost |

**Good Practice:**
```go
func TestUserService_Create(t *testing.T) {
    tests := []struct {
        name    string
        input  UserCreateDto
        want   User
        wantErr bool
    }{
        {"valid", UserCreateDto{Email: "a@b.com"}, User{Email: "a@b.com"}, false},
        {"invalid email", UserCreateDto{Email: "invalid"}, User{}, true},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            svc := NewUserService(mockRepo)
            got, err := svc.Create(tt.input)
            if tt.wantErr {
                assert.Error(t, err)
            } else {
                assert.NoError(t, err)
                assert.Equal(t, tt.want.Email, got.Email)
            }
        })
    }
}
```

**Violation Example:**
```go
func TestUserService() {
    // Multiple test cases in one function with if/else
    if err := svc.Create(UserCreateDto{Email: "a@b.com"}); err != nil {
        t.Fatal(err)
    }
    // Hard to read, hard to maintain
}
```

**Fix Suggestion:** Use table-driven tests with `t.Run` for readability and parallel execution.

---

## How to use this file in Testomancer

When you detect a language, quote the relevant section, show a short "Good vs Bad" snippet from the codebase (if possible), and propose concrete fixes.

---

## Custom / Project-Specific Rules

> **Placeholder:** Add per-project overrides in `references/specific_rules.md`. Examples:
> - Specific naming conventions required by the team
> - Custom coverage thresholds (e.g., >90% for security-critical code)
> - Mandatory security static analysis tools
> -特定 framework requirements

**How to extend:**
1. Create `references/specific_rules.md`
2. Add project-specific rules with clear rationale
3. Testomancer will automatically include these in recommendations
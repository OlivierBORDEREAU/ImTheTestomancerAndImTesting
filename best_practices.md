# Best Practices Compliance Checks – Testomancer

Before recommending tests, audit the codebase against modern language-specific standards (2026).
Highlight violations with examples and suggest fixes.

## Python

**Key Best Practices**
- Follow PEP 8 (use Ruff or Black for formatting)
- Add type hints everywhere (compatible with mypy or pyright)
- Prefer Pydantic models or dataclasses over plain dicts
- Use dependency injection instead of global state
- Proper pytest fixtures (avoid overuse of monkeypatch)
- Async code must use pytest-asyncio

**Example Snippets**

**Good Practice (Recommended):**
```python
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str
    username: Optional[str] = None

def create_user(user_data: UserCreate) -> User:
    # Clear, typed, no global state
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

## How to use this file in Testomancer

When you detect a language, quote the relevant section, show a short "Good vs Bad" snippet from the codebase (if possible), and propose concrete fixes.
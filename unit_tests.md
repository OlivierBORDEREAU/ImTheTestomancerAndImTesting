# Unit Tests – Testomancer

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
| Go          | testing + testify           | -                                | Native and extremely fast |
| .NET        | xUnit (preferred) or NUnit  | Moq                              | Clean and modern |

**Automation Tools**  
- GitHub Actions / GitLab CI / Jenkins  
- Pre-commit hooks + Husky (for JS/TS)  
- Automatic coverage reports + badges

**Prompt Template to Use**  
"Analyze this module [paste code]. Generate a complete unit test suite using [framework]. Cover nominal cases, edge cases, error cases, and property-based tests where applicable."

**Best Practices**  
- One assertion per test when possible  
- Use AAA (Arrange-Act-Assert) or Given-When-Then naming  
- Parameterized tests  
- Avoid unnecessary mocks on simple objects
# Unit / Component Tests

**ISTQB Mapping:** Component Testing

**Goal**  
Verify individual functions, methods, or classes in complete isolation.

**When to Prioritize**
- Complex business logic and algorithms
- Validation rules
- Pure functions with no external dependencies
- Edge cases and boundary conditions

**Recommended Stack (2026)**

| Language     | Primary Framework          | Complementary Tools          |
|--------------|----------------------------|------------------------------|
| Python       | pytest + pytest-asyncio    | hypothesis                   |
| TypeScript   | Vitest                     | Testing Library (React)      |
| Java         | JUnit 5 + AssertJ          | -                            |
| .NET         | xUnit + FluentAssertions   | -                            |
| Go           | testing + testify          | -                            |

**Key Rules**
- One assertion per test when possible.
- Use table-driven tests for multiple scenarios.
- Mock only what is strictly external.
- Define success criteria before writing the test.

**Coverage Targets**
- Critical paths: >80% statement + branch coverage
- Edge cases: Aim for 100% on boundaries and null/invalid inputs

**Karpathy Reminder**  
Keep tests minimal. A 10-line focused test is better than a 50-line comprehensive one.
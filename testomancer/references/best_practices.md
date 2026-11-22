# Practical testing guidance

Prefer the repository's existing framework, test layout, assertions, fixtures, and commands. These are optional examples, not a current-version matrix or migration mandate. Inspect installed versions, project constraints, licensing, and compatibility before adding a dependency.

| Stack | Options if the project needs them | Application |
|---|---|---|
| Python | unittest or pytest; pytest-asyncio; Hypothesis | Existing runner first; async tests match event-loop setup; properties need a contract |
| TypeScript / React | Existing Jest or Vitest; Testing Library and user-event | Observe behavior through accessible controls; do not extract hooks merely to satisfy a test style |
| Java | Existing JUnit; AssertJ; Testcontainers | Reuse build configuration; real dependencies when their semantics matter |
| .NET | Existing xUnit, NUnit, or MSTest; WebApplicationFactory; Testcontainers | Match project conventions; await async operations |
| Go | Standard testing; optional testify | Table-driven cases and subtests where they improve readability; package placement follows intended visibility |
| Browser/API | Existing Playwright, Cypress, Selenium, HTTP client, or API test runner | Choose the interface needed by the risk, not a universal tool ranking |

## Cross-cutting choices

- Make outcomes reproducible: control clock, random seeds, locale, timezone, ordering, and fixture ownership where relevant. Use isolated data and reliable teardown.
- Design fixtures around necessary preconditions. Keep setup understandable and avoid global mutable state or accidental order dependencies.
- Use multiple assertions when they describe one coherent outcome. Assert errors and absence of unintended side effects where required.
- Choose real dependencies or doubles according to the failure mechanism. Document fidelity limits; in-memory databases may differ in SQL, constraints, locking, and transactions.
- Use synthetic/non-sensitive data and approved secret injection. Never put credentials or private records in fixtures, output, snapshots, or committed artifacts.
- Investigate flaky tests; do not hide failure behind broad retries. Capture the first failure and its context.
- Prioritize by actual product impact and likelihood. Authentication, authorization, payments, privacy, data integrity, recovery, and third-party contracts are useful risk prompts, not universal priorities in every project.
- Treat coverage as a diagnostic indicator. Any gate must have an explicit project source and denominator; no generic percentage establishes adequacy.
- Accessibility, security, performance, and reliability may require specialist/manual checks as well as automation. No tool result alone guarantees compliance.

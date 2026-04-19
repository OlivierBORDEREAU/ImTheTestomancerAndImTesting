# Karpathy Guidelines for Testomancer

> **Mandate:** Testomancer must apply these guidelines in every response that involves code suggestions or refactoring.

Behavioral guidelines derived from Andrej Karpathy's observations on common LLM coding mistakes.  
**Apply these rules every time Testomancer suggests, generates, reviews, or refactors test code or production code.**

**Tradeoff:** These guidelines bias toward caution and simplicity over speed. For very trivial test additions, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before proposing any test code or changes:
- State your assumptions explicitly.
- If something is unclear about the codebase, requirements, or testing level, name it and ask.
- If multiple ways exist to test something, present the simplest first and explain tradeoffs.
- Push back politely if the user request leads to overcomplicated tests.

## 2. Simplicity First

**Minimum test code that solves the testing goal. Nothing speculative.**

- Add only the tests that were requested or clearly needed for the chosen level.
- Avoid premature abstractions, complex test helpers, or "future-proof" setups unless asked.
- Prefer clear, readable tests over clever ones.
- If a test can be 10 lines instead of 50, rewrite it.
- Ask yourself: "Would a senior test engineer call this over-engineered?"

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When adding or modifying tests:
- Do not refactor unrelated tests, production code, or formatting unless explicitly asked.
- Match the existing test style and conventions of the project.
- Only remove imports, fixtures, or code made unused **by your changes**.
- If you spot unrelated issues (dead tests, flakiness), mention them separately — do not fix them automatically.

Every changed line in a suggested test must directly serve the user's request or the chosen testing level.

## 4. Goal-Driven Execution (Especially Important for Testing)

**Define verifiable success criteria. Loop until verified.**

For every testing recommendation:
- Turn the task into clear goals, e.g.:
  - "Add unit tests for edge cases" → "Write tests covering the identified branches, run them, and confirm they pass/fail as expected."
  - "Improve integration test coverage" → "Add contract or interaction tests, then verify they run successfully in the integration environment."
- When suggesting code, include a short verification plan.
- Prefer tests that are easy to run and assert (e.g., follow AAA pattern strictly).

> **Link to SKILL.md:** The **Verification** subsection maps directly to the 5-step response structure (section 4. Recommendations → Verification). Always include:
> - **Explicit assumption:** What are you assuming about the codebase?
> - **Goal:** What behavior does the test verify?
> - **Tradeoff:** Any simplifications made due to these guidelines?
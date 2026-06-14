# Karpathy Guidelines – Testomancer

**Mandatory for all code suggestions and refactoring.**

These rules exist to prevent over-engineering, hidden assumptions, and unnecessary complexity — common failure modes when LLMs write tests.

## 1. Think Before Coding

- State your assumptions explicitly.
- If something is unclear about the codebase or requirements, name it.
- Present the simplest approach first and explain tradeoffs.
- Push back on requests that would lead to overcomplicated tests.

## 2. Simplicity First

- Write the minimum test code that solves the goal.
- Avoid premature abstractions and "future-proof" setups.
- Prefer clear, readable tests over clever ones.
- Ask: "Would a senior engineer call this over-engineered?"

## 3. Surgical Changes

- Touch only what is necessary for the current request.
- Match the existing test style and conventions of the project.
- Do not refactor unrelated code unless explicitly asked.
- Mention unrelated issues separately — do not fix them automatically.

## 4. Goal-Driven Verification

For every recommendation, define:
- **Explicit assumption**: What are you assuming about the codebase?
- **Goal**: What exact behavior does this test verify?
- **Tradeoff**: What simplifications were made due to these guidelines?

Always include these three elements when suggesting tests.
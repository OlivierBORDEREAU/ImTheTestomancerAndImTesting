---
name: testomancer
description: ISTQB-aligned testing strategy and implementation guidance for AI coding agents
tags: [testing, istqb, quality, karpathy]
---

# Testomancer – Testing Strategy Skill

**Mission**  
Help developers design and implement effective, maintainable test suites that align with ISTQB test levels while strictly following Karpathy Guidelines (simplicity, surgical changes, explicit assumptions).

## Core Principles (Always Apply)

1. **Karpathy Guidelines** — See `references/karpathy-guidelines.md`
2. **ISTQB Test Levels** — Map recommendations to:
   - Unit / Component Testing
   - Integration / Component Integration Testing
   - Functional / System Testing
   - End-to-End / Acceptance Testing
3. **Testing Pyramid** — Strongly favor unit and integration tests over E2E.
4. **Risk-Based Testing** — Prioritize authentication, payments, data validation, third-party integrations, and critical business logic.

## Reference Files (Read in this order)

1. `references/karpathy-guidelines.md` — Mandatory rules for all code suggestions
2. `references/specific_rules.md` — Project-specific overrides (check first)
3. `references/best_practices.md` — Language and cross-cutting standards
4. Testing level references (in `references/testing-levels/`):
   - `unit_tests.md`
   - `integration_tests.md`
   - `functional_tests.md`
   - `e2e_tests.md`

## Required Behavior

- Always state assumptions explicitly before making recommendations.
- Define clear success criteria for any test suggested.
- Prefer the simplest solution that achieves the goal.
- Make only surgical changes — do not refactor unrelated code.
- When suggesting tests, include:
  - Why this level is appropriate
  - Recommended libraries/frameworks with justification
  - Concrete code examples or templates
  - How to verify the tests work

## Response Approach

When given a codebase or feature request:

1. Analyze the current state (languages, frameworks, existing tests if visible).
2. Identify high-risk areas.
3. Recommend the appropriate testing level(s) with justification.
4. Provide concrete, minimal examples following Karpathy Guidelines.
5. Suggest next steps (additional levels, CI integration, etc.).

**Never** generate large amounts of speculative test code. One focused, verifiable test is better than ten average ones.
# End-to-End Tests

**ISTQB Mapping:** Acceptance Testing / System Testing (user journeys)

**Important**  
E2E tests are expensive. ISTQB recommends keeping them to ~5-10% of the total test suite. Use risk-based selection only.

**Goal**  
Verify complete user journeys through the full system (UI + backend + data).

**When to Prioritize (sparingly)**
- Critical business flows (e.g., checkout, onboarding, payment)
- High-risk user journeys
- Visual regression on key pages
- Regulatory or compliance flows

**Recommended Stack (2026)**

| Tool        | Strength                     | Recommendation          |
|-------------|------------------------------|-------------------------|
| Playwright  | Auto-wait, tracing, codegen  | **Strongly preferred**  |
| Cypress     | Good DX, time travel         | Acceptable alternative  |
| Selenium    | Legacy                       | Avoid for new projects  |

**Key Rules**
- Keep E2E tests to the absolute minimum needed.
- Use Playwright codegen to bootstrap, then surgically edit.
- Mock external services and slow dependencies when possible.
- Prefer API-level checks over pure UI when the goal is functional.

**Visual & Accessibility**
- Use built-in Playwright accessibility queries + axe-core for WCAG checks.
- Add visual regression only on pages where layout stability matters.

**Karpathy Reminder**  
One reliable, maintainable E2E test on a critical path is worth more than ten flaky ones.
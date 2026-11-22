# End-to-end workflows

E2E describes scope, not a separate ISTQB level or a synonym for acceptance. Define the start/end of the journey, included systems, objective, and oracle. It can contribute to system, system-integration, or acceptance evidence; a browser is optional. See [test model](../test-model.md).

Select journeys whose important failure mechanisms need broad evidence: checkout wiring, onboarding persistence, cross-service reconciliation, recovery, or critical business outcomes. Use measured maintenance/runtime costs and product risks, not a fixed suite percentage or a ban on overlap with component tests.

## Boundaries and fidelity

List real UI/API/backend/data/service participants and every simulated service. A UI-to-database journey with a stubbed payment provider can verify local orchestration, but not actual payment-provider compatibility. Retain real/approved sandbox coverage when that integration is the risk; obtain authorization for side effects and isolate test data.

## Execution choices

- Reuse an existing browser/API runner (including Playwright, Cypress, or Selenium) instead of automatically migrating it.
- Use stable, user-facing locators and condition-based synchronization; avoid arbitrary sleeps. Code generation is optional scaffolding that still requires reviewed oracles and cleanup.
- Seed only necessary state, isolate identities/data, and clean up reliably. Keep diagnostic traces/screenshots only where allowed; redact sensitive data.
- Use API setup or checks when they reduce cost without bypassing the behavior under test. Do not bypass the UI if UI behavior is the risk.
- Visual checks need controlled rendering and reviewed baselines. Accessible locators and automated scanners are useful but do not establish accessibility conformance; add appropriate manual checks.

Report exact environment, boundaries, executed outcomes, and unverified scope using [verification](../verification.md). No automation result alone establishes acceptance, production readiness, or regulatory compliance.

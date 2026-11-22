---
name: testomancer
description: Assess test suites, design risk-based cases, and implement and verify focused tests with explicit oracles and honest evidence. Use for testing strategy, coverage gaps, regression tests, and test implementation.
---

# Testomancer

Improve confidence in observable behavior with focused, maintainable tests. This is portable guidance: no specific agent runtime, memory service, tool name, harness, reporter, or external integration is required. Use available capabilities; disclose access or execution limits rather than invent evidence.

## Choose the intent

- **Assess**: inspect existing evidence and identify prioritized gaps; do not edit by default.
- **Design**: derive cases, oracles, boundaries, and a runnable verification plan; label examples as proposed, not executed.
- **Implement–verify**: make authorized, focused changes and run the relevant checks; report blockers and unverified scope.

Infer the intent from the request. Clarify only when ambiguity changes scope or authorization.

## Workflow

1. **Inspect** the request, relevant source, requirements, existing tests, manifests, runner configuration, and CI commands. Distinguish observed facts from assumptions; never invent a project API.
2. **Establish constraints**: permitted paths/actions, active project policy, environment, data/privacy rules, budgets, and success criteria. Repository instructions and user authorization govern; bundled examples are not policy.
3. **Identify risks and oracles**: prioritize plausible failures by impact and likelihood in this context. State the expected behavior and its authoritative basis; flag conflicting or missing requirements.
4. **Derive cases** from equivalence partitions, boundaries, decision tables, and state transitions as relevant. Include failure paths and explicit expected outcomes, not just a list of test names.
5. **Choose boundaries**: identify the test object, level, type, scope, real dependencies, and doubles. Use the least costly boundary that can expose the risk, adding broader evidence where integration or journeys matter.
6. **Act within scope**: assess, design, or implement as requested. Prefer existing frameworks and conventions; avoid speculative scaffolding, unrelated refactoring, and production changes for stylistic preferences.
7. **Verify**: run the focused checks and relevant regression checks when permitted. For a defect, demonstrate failing-before/passing-after where feasible; otherwise explain the limitation. Record exact evidence, not inferred success.
8. **Report gaps**: distinguish proposed, executed, and blocked checks; include command, result, exit status, environment, revision, and unverified scope. State residual risks without claiming absence of defects or compliance.

## Select references, do not load everything

- Classification, five levels, scope, and pyramid: [test model](references/test-model.md).
- Case derivation and oracles: [test design](references/test-design.md).
- Execution evidence and regression checks: [verification](references/verification.md).
- Optional stack guidance: [best practices](references/best_practices.md).
- Project-policy discovery: [specific rules](references/specific_rules.md); the bundled file has no active overrides.
- Change discipline: [Karpathy guidelines](references/karpathy-guidelines.md).
- Boundary-specific guidance: [component](references/testing-levels/unit_tests.md), [integration](references/testing-levels/integration_tests.md), [functional](references/testing-levels/functional_tests.md), [E2E](references/testing-levels/e2e_tests.md).
- Optional output starters: [report](assets/test-report-template.md) and [inactive policy example](assets/project-policy.example.md).

## Guardrails

- Level, type, and scope are independent: functional is not a level; E2E is not synonymous with acceptance.
- Do not impose suite ratios, coverage thresholds, assertions-per-test quotas, or universal runtime limits. Use measured costs, risks, and confirmed project criteria.
- Explain what a double removes from the evidence. A mocked dependency is not a verified real integration.
- Overlap across levels is legitimate when it exposes different failures; remove redundant cost, not useful evidence.
- Do not install dependencies, use production data, contact external systems, or change shared infrastructure without appropriate authorization. If tools or access are unavailable, deliver a labeled design and precise blocker.

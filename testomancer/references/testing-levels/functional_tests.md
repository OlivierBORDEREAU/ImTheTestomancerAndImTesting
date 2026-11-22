# Functional testing (not a test level)

The filename is retained for compatibility. Functional testing evaluates what a test object should do and can apply at any of the five levels. A UI component check is not automatically a system test; a public API check is classified by the object and purpose, not its HTTP transport. See [test model](../test-model.md).

## Design from behavior

Map requirements or acceptance criteria to explicit oracles. Use partitions, boundaries, decision tables, and state transitions to derive successful and rejected behavior, effects, and recovery. Given/When/Then is an optional expression style, not a required framework; see [test design](../test-design.md).

Select the interface needed by the risk:

- A local rule can be checked at component level.
- A repository/API interaction may need component integration evidence.
- A complete product workflow may need system-level evidence.
- A cross-system contract may need system integration evidence.
- Business fitness and deployment readiness require acceptance criteria and the appropriate stakeholders, not merely a passing functional script.

Prefer a lower-cost API boundary when it exposes the intended failure, but retain UI checks when rendering, interaction, accessibility, or frontend/backend wiring is the risk. State real versus doubled dependencies. Useful overlap at different levels is allowed when objectives differ; remove only redundant checks whose cost exceeds their added confidence.

Use existing tools and [verification](../verification.md); functional correctness alone does not establish non-functional quality or compliance.

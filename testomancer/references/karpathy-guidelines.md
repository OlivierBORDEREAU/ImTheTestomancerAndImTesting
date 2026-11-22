# Change discipline (Karpathy guidelines)

- **Think before coding**: state material assumptions, unknowns, success criteria, and tradeoffs. Inspect actual code and requirements before suggesting APIs or tests.
- **Prefer simplicity**: use focused examples and existing fixtures before new abstraction layers. Minimal means sufficient for the identified risk, not artificially short or one assertion per test.
- **Keep changes surgical**: follow existing conventions and approved paths. Do not migrate frameworks, extract hooks, replace data models, or refactor production code for stylistic preference. Propose necessary testability changes separately when outside scope.
- **Verify the goal**: define an explicit oracle, exercise the artifact when authorized, and distinguish observed outcomes from assumptions and blocked checks. See [verification](verification.md) for evidence requirements.

Mention unrelated issues separately instead of fixing them automatically. Do not let a preferred design style displace project requirements or useful coverage.

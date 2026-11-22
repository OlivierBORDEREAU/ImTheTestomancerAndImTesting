# Component (unit) tests

See [test model](../test-model.md) for classification. Component tests exercise an identified component in isolation from the wider system. The unit may be a function, class, module, or cohesive subsystem; define it rather than requiring a mock for every collaborator.

Use for rules, transformations, algorithms, local state, validation, and error handling where the failure can be exposed locally. Derive partitions, boundary values, and properties from a stated contract; see [test design](../test-design.md).

- Keep deterministic collaborators real when they belong inside the chosen unit and do not obscure the objective.
- Replace a collaborator deliberately to control time, randomness, network, or a failure path. Explain which behavior is simulated and not verified.
- Assert observable output/state/events or meaningful interaction contracts, not incidental call order or private internals unless that structure is the explicit subject.
- Parameterize related cases when it keeps their individual oracles clear. Multiple assertions can verify one coherent behavior.
- Follow existing framework/style; use [optional stack guidance](../best_practices.md) only when needed. Do not impose coverage or line-count targets.

A component test cannot establish actual database behavior or service interoperability when those boundaries are doubled. Add focused integration evidence where the risk requires it. Execute and report using [verification](../verification.md).

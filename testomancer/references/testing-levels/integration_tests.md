# Integration tests

Component integration checks interactions among components; system integration checks interfaces between the system and other systems/services. Classify by object/objective; see [test model](../test-model.md).

Narrow integration covers a limited interaction; broad integration covers more interactions or a larger workflow. Breadth is independent of process topology: a narrow test may cross a network and a broad test may run in-process.

## Design the boundary

- Identify both ends, the actual protocol/schema, and the failure to expose: serialization, SQL, migrations, transaction/constraint behavior, authentication, ordering, timeout, retry, or idempotency.
- Use real dependencies where their behavior is the subject and an authorized representative environment is available. Existing local fixtures, ephemeral containers, or approved sandboxes are options, not requirements.
- Use doubles when controlled failures or unavailable services justify them. Never mock the exact interaction being claimed as verified. Describe which side is real, which is simulated, and what remains unverified.
- For consumer/provider contracts, verify consumer expectations and provider conformance separately. A stub responding as configured alone proves neither provider correctness nor deployment compatibility.
- Isolate data, bound waits, assert committed outcomes, and clean up resources. Avoid shared/prod systems without permission.

Reuse the project's runner and lifecycle tooling. Containers add startup, platform, and cleanup requirements; report them when relevant. Broader regression checks may intentionally overlap local rules to catch wiring and persistence failures. See [verification](../verification.md) for execution evidence.

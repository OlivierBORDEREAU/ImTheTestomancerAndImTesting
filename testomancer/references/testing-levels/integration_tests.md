# Integration Tests

**ISTQB Mapping:** Component Integration Testing / System Integration Testing

**Goal**  
Verify interactions between modules, services, databases, and external systems.

**When to Prioritize**
- REST/GraphQL API contracts
- Database ↔ application layer
- Service-to-service communication
- Cross-module workflows
- Message queues and event handling

**Narrow vs Broad Integration**

- **Narrow**: Same process, in-memory (fast, preferred when possible)
- **Broad**: Cross-process, real containers or external services (more realistic)

**Recommended Approach (Karpathy-aligned)**

| Language     | Preferred Tools                     | Notes                              |
|--------------|-------------------------------------|------------------------------------|
| Python       | pytest + Testcontainers             | Ephemeral, automatic cleanup       |
| TypeScript   | Vitest + Testcontainers + MSW       | Fast startup, good DX              |
| Java         | JUnit 5 + Testcontainers            | Ryuk for automatic cleanup         |
| .NET         | xUnit + WebApplicationFactory       | Good for ASP.NET Core              |

**Contract Testing**
- Consider consumer-driven contract testing (Pact) for microservices.
- Start with consumer tests, then verify on the provider side.

**Key Rules**
- Only mock what you cannot control.
- Prefer real dependencies (via Testcontainers) over heavy mocking when practical.
- Keep integration tests focused — one major interaction per test.
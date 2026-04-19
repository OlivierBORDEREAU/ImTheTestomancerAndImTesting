# Integration Tests – Testomancer

> **ISTQB Note:** Also known as **Component Integration Testing** in ISTQB terminology.

**Definition**  
Tests that verify interactions between multiple units (database, internal APIs, services, message queues, etc.).

**Integration Scope**

```
┌─────────────────────────────────────────────────────────────┐
│  Module-to-Module (Narrow Integration)                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐           │
│  │ Service A ──►│ Service B ──►│ Service C │           │
│  └─────────┘    └─────────┘    └─────────┘           │
│  - Same process / in-memory                               │
│  - Fast, no network                                 │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Service-to-Service (Broad Integration)                     │
│  ┌────────┐  HTTP  ┌────────┐  gRPC  ┌────────┐ │
│  │  API   │───────►│  API   │──────►│  DB   │ │
│  └────────┘       └────────┘       └────────┘ │
│  - Cross-process / network                                │
│  - Requires containers/test environments            │
└─────────────────────────────────────────────────────────────┘
```

**When to Prioritize**  
- REST/GraphQL APIs  
- Database ↔ code interactions  
- Microservices communication  
- Cross-module workflows

**Codebase Analysis**  
Look for: HTTP calls, repositories, services, event handlers, database connections.

**Contract Testing**

> **Pact** is the recommended tool for consumer-driven contract testing (CDC).

| Tool | Use Case | Language Support |
|------|---------|---------------|
| Pact | Consumer-driven contracts | JS, Python, Java, Go, .NET |
| WireMock | Static stubs + response matching | All major languages |
| Hoverfly | Native mode / simulate | Python, Go, Java |

- Write consumer tests first → Generate contract
- Verify provider satisfies contract
- Use Pact broker for CI/CD integration

**Recommended Stack (2026)**

| Language | Main Framework | Container Support | Mock/Stub | Notes |
|----------|-------------|---------------|---------------|-----------|-------|
| Python | pytest | Testcontainers (Python) | pytest-mock, responses | pytest-docker deprecated |
| JavaScript/TypeScript | Vitest | Testcontainers (JS) | MSW, Supertest | MSW for HTTP mocking |
| Java | JUnit 5 | Testcontainers Java 2.x | WireMock, MockMvc | 2.x: better startup |


**Testcontainers 2.x Features**
- Reusable containers (container reuse across tests)
- Ryuk container for cleanup (automatic garbage collection)
- Cloud-native support (ECS, Kubernetes)
- Improved startup times (container caching)

**WireMock Alternatives**
- Mirage (Elixir/JS)
- Hoverfly (Go-based)
- Mockserver (Java)

**Test Data Management**

| Strategy | Use | Example |
|----------|-----|-------|
| Factories | Create test data on-the-fly | Factory Boy (Python), factory-bot (JS) |
| Fixtures | Static JSON/YAML data | `tests/fixtures/` |
| Seeding | Database pre-load | Liquibase/Flyway migrations |
| Cleanup | Teardown after tests | Transaction rollback, truncate |

Best practices:
- Use unique per-test data (avoid shared state)
- Generate data in `setup` / `@BeforeEach`
- Clean up in `teardown` / `@AfterEach`
- Use transaction rollback for database tests

> ⚠️ **Warning: Flakiness**
> - Integration tests are slower than unit tests (network, I/O)
> - **Target:** <2s per test (aim for 500ms avg)
> - Use in-memory when possible (SQLite, H2)
> - Parallelize with worker processes
> - Disable retries in CI (flaky = fix, don't retry)

**Automation Tools**  
- Docker Compose for test environments  
- CI/CD with container spin-up (Testcontainers + GitHub Actions)

**Best Practices**  
- Use in-memory databases or ephemeral containers  
- Test contracts, not implementations  
- Systematic cleanup of test data
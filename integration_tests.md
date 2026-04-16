# Integration Tests – Testomancer

**Definition**  
Tests that verify interactions between multiple units (database, internal APIs, services, message queues, etc.).

**When to Prioritize**  
- REST/GraphQL APIs  
- Database ↔ code interactions  
- Microservices communication  
- Cross-module workflows

**Codebase Analysis**  
Look for: HTTP calls, repositories, services, event handlers, database connections.

**Recommended Stack (2026)**

- Python: pytest + pytest-docker / Testcontainers  
- JavaScript/TypeScript: Vitest + MSW (Mock Service Worker) or Supertest  
- Java: JUnit 5 + Testcontainers  
- Go: testify + testcontainers-go  
- **Universal recommendation**: Testcontainers (standard for ephemeral containers)

**Automation Tools**  
- Docker Compose for test environments  
- CI/CD with container spin-up (Testcontainers + GitHub Actions)

**Best Practices**  
- Use in-memory databases or ephemeral containers  
- Test contracts, not implementations  
- Systematic cleanup of test data
# Functional / System Tests

**ISTQB Mapping:** System Testing (functional aspects)

**Goal**  
Validate that the system behaves according to business requirements and user stories.

**When to Prioritize**
- Business rule validation
- User story acceptance criteria
- Public API behavior
- Complex workflows that span multiple components

**Approach**
- Map acceptance criteria to test scenarios (Given/When/Then style).
- Focus on observable behavior, not implementation.
- Keep scenarios short and focused on one rule or flow.

**Recommended Tools**

| Type              | Tools                          | Notes                              |
|-------------------|--------------------------------|------------------------------------|
| API Testing       | REST Assured, Supertest, httpx | Contract + behavior                |
| UI Component      | Testing Library, Storybook     | User behavior focus                |
| Business Rules    | Custom + domain models         | Avoid testing framework internals  |

**Key Rules**
- Write the minimal number of scenarios needed to cover the acceptance criteria.
- Prefer API-level functional tests over UI when possible (faster, more stable).
- Do not duplicate unit or integration test coverage here.

**Karpathy Reminder**  
One clear scenario that verifies a business rule is better than five overlapping scenarios.
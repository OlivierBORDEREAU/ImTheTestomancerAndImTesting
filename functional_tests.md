# Functional Tests – Testomancer

**Definition**  
Black-box tests that validate the system against functional requirements (user stories / specifications).

**When to Prioritize**  
- Business rule validation  
- User scenario testing  
- Public APIs (contract testing)

**Recommended Stack**  
- **BDD**: Cucumber (Java/JS) or Behave / pytest-bdd (Python)  
- API Testing: RestAssured (Java), Supertest (JS), requests + pytest (Python)  
- Contract Testing: Pact or Spring Cloud Contract

**Automation Tools**  
- GitHub Actions with Allure or Cucumber reports
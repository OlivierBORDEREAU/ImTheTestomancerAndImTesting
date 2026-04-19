# Functional / System Tests – Testomancer

> **ISTQB Mapping:** This level aligns with **System Testing** (ISTQB). Functional testing is a test type, not a distinct level in ISTQB — it maps primarily to System Testing (functional aspects) or Acceptance Testing.
> **Karpathy Guidelines:** Generate the minimal set of scenarios needed for the user story. Define success criteria (Given/When/Then) before writing any Gherkin. Keep scenarios simple and surgical. Test what the user needs, not what they might want someday.

**Definition**  
Black-box tests that validate the system against functional requirements (user stories / specifications).

**When to Prioritize**  
- Business rule validation  
- User scenario testing  
- Public APIs (contract testing)
- End-to-end user journeys

**User Story / Acceptance Criteria Mapping**

| User Story | Acceptance Criteria | Test Coverage |
|-----------|-----------------|--------------|
| As a user, I can log in | Given valid credentials → When I submit → Then I see dashboard | Login success test |
| | Given invalid password → When I submit → Then I see error | Login failure test |
| | And I should be logged out after 30 min inactivity | Session timeout test |

**Gherkin Syntax**

```
Feature: User Login
  As a registered user
  I want to log in to my account
  So that I can access my dashboard

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter "user@example.com" in the email field
    And I enter "password123" in the password field
    And I click the "Login" button
    Then I should be redirected to the dashboard
    And I should see "Welcome, User"

  Scenario: Failed login with invalid password
    Given I am on the login page
    When I enter "user@example.com" in the email field
    And I enter "wrongpassword" in the password field
    And I click the "Login" button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page
```

**Non-Functional Checks within Functional Tests**

| Check | Tool | When |
|-------|------|------|
| Performance (response time) | Lighthouse, WebPageTest | Per critical journey |
| Accessibility (basic) | axe-core, pa11y | Per UI component |
| Basic security headers | security headers scanner | Per endpoint |
| Mobile responsiveness | Playwright mobile view | Per layout |

> **Note:** Full non-functional testing (load, security, accessibility, performance) belongs at the **Acceptance level**, not System/Functional level.

**Traceability** (goal-driven verification)

| Test | User Story | Acceptance Criteria | Automated? |
|------|------------|-----------------|------------|
| `test_login_success` | US-001 | AC-001 | Yes |
| `test_login_invalid_password` | US-001 | AC-002 | Yes |
| `test_login_session_timeout` | US-001 | AC-003 | Yes |

- Use tags (`@US-001`) to link tests to user stories
- Generate test matrix from requirements tracker
- **Failed test → immediate requirement gap** (goal-driven verification)

**Recommended Stack (2026)**

| Type | Tool | Pros | Cons | Status |
|------|------|------|------|--------|
| **BDD** | Cucumber (Java/JS) | Widely adopted, Living docs | Verbose | Stable |
| | pytest-bdd (Python) | Pythonic integration | Less tooling | Stable |
| | Behave (Python) | Simple Gherkin | Limited | Stable |
| **UI Testing** | Playwright | Multi-browser, auto-wait, tracing | Newer | 2026 Leader |
| | Playwright Component | React/Vue/Angular in-context | Growing ecosystem | 2026 Leader |
| | Selenium | Mature ecosystem | Slow, flaky | Legacy |
| **API Testing** | RestAssured | Fluent API, JSON path | Java only | Stable |
| | Supertest (JS) | Lightweight, Express | Limited validation | Stable |
| | requests + pytest | Pythonic, flexible | Manual assertions | Stable |
| **Contract** | Pact | CDC, broker integration | Setup overhead | Stable |
| | Spring Cloud Contract | Java-first | Spring-dependent | Legacy |

**Sample BDD Scenario (Full)**

```gherkin
Feature: Shopping Cart
  As a shopper
  I want to add items to my cart
  So that I can purchase them later

  Background:
    Given the store has the following products:
      | name | price | stock |
      | Apple | $1.00 | 100 |
      | Banana | $0.50 | 50 |

  Scenario: Add single item to cart
    Given I am browsing the store
    When I add "Apple" to my cart
    Then my cart should contain 1 item
    And the total should be $1.00

  Scenario: Add multiple quantities
    Given I am browsing the store
    When I add 3 units of "Banana" to my cart
    Then my cart should contain 3 items
    And the total should be $1.50
```

**Automation Tools**  
- Octane for requirements traceability and Manual and Gherkin Tests repository
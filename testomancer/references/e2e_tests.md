# End-to-End Tests – Testomancer

**Definition**  
Tests that simulate a real user journey through the entire application (UI + backend + database).

**When to Prioritize (sparingly)**  
- Critical user journeys  
- Visual regression  
- Complete workflows (login → checkout → confirmation)

**Recommended Stack 2026 (Playwright is the leader)**  
- **Playwright** (strongly recommended – multi-language, fast, auto-wait, excellent tracing)  
- Cypress (still solid for JS teams)  
- Selenium (only for legacy systems)

**Complementary Tools**  
- Playwright Test + Allure / HTML reporter  
- Visual regression: Percy, Applitools, or pixelmatch  
- Parallel CI/CD across multiple browsers

**Best Practices**  
- Limit to 5-10% of total tests  
- Use dedicated staging environments  
- Tag critical vs non-critical tests
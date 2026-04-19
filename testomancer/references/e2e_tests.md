# End-to-End Tests – Testomancer

> **ISTQB Mapping:** E2E is a test technique/approach, not a formal level. It maps to **System Testing** or **Acceptance Testing** when validating end-user journeys. ISTQB recommends risk-based selection—keep E2E minimal (5-10% of total tests).

**Definition**  
Tests that simulate a real user journey through the entire application (UI + backend + database).

**When to Prioritize (sparingly)**  
- Critical user journeys  
- Visual regression  
- Complete workflows (login → checkout → confirmation)

**Recommended Stack 2026 (Playwright is the leader)**

| Tool | Language | Auto-Wait | Tracing | Status |
|------|----------|-----------|---------|---------|--------|
| **Playwright** | Python/JS/TS | ✅ Built-in | ✅ Native | 2026 Leader |
| Selenium | Any | ❌ Manual | ❌ | Legacy |
| Appium | Any | ❌ Manual | ❌ | Legacy |

**Playwright Features (2026)**

- **Auto-wait:** Automatic waits for elements (no manual waits)
- **Tracing:** `playwright show-trace` for failed tests with DOM snapshots
- **Codegen:** `playwright codegen` to record interactions as test code
- **Network mocking:** `page.route()` to intercept/stub API calls
- **Accessibility testing:** Built-in ARIA role queries, axe-core integration

```python
# Playwright auto-wait + network mocking example
from playwright.sync_api import expect

def test_checkout_flow(page):
    # Mock API response
    page.route("**/api/cart", lambda route: route.fulfill(
        json={"items": [{"id": 1, "price": 10}]}
    ))

    page.goto("/cart")
    expect(page.locator(".cart-item")).to_be_visible()
    page.click("text=Checkout")
    expect(page.locator(".confirmation")).to_contain_text("Order confirmed")
```

**Visual & Accessibility Regression**

| Tool | Type | Notes |
|------|------|-------|
| Percy | Visual + layout | Integrates with CI |
| Applitools | Visual AI | Cross-browser |
| axe-core | Accessibility | WCAG compliance |
| Lighthouse | Performance + a11y | Built-in Chrome |
| pixelmatch | Pixel comparison | CLI tool |

```typescript
// Accessibility with axe-core in Playwright
import { test, expect } from '@playwright/test';
import axe from 'axe-core';

test('checkout accessible', async ({ page }) => {
    await page.goto('/checkout');
    const results = await page.evaluate(() => axe.run());
    expect(results.violations).toHaveLength(0);
});
```

**Flakiness Mitigation Checklist**

| Strategy | Implementation |
|----------|---------------|
| **Stable locators** | `get_by_role`, `get_by_label`, not CSS/XPath |
| **Auto-wait** | Use Playwright (built-in) or explicit waits |
| **Network stubs** | Mock external APIs (`page.route()`) |
| **No retries in CI** | Fix flaky tests, don't retry |
| **Isolate data** | Unique test data per run |
| **Screenshots on fail** | `trace: on-first-retry` |
| **Retry-until CI** | Only for known-flaky (mark with `@flaky`) |

**Best Practices**  
- Limit to 5-10% of total tests  
- Use dedicated staging environments  
- Tag critical vs non-critical tests

---

## Sample Critical User Journey Test Outline

```python
# test_checkout_complete.py
from playwright.sync_api import test, expect

@test.describe("Checkout Journey")
class CheckoutE2E:
    @test("Complete checkout flow")
    def test_checkout_complete(self, page: Page):
        # 1. Login
        page.goto("/login")
        page.fill("#email", "test@example.com")
        page.fill("#password", "password123")
        page.click("text=Login")
        expect(page).to_have_url("/dashboard")

        # 2. Add item to cart
        page.click("text=Add to Cart >> nth=0")
        expect(page.locator(".cart-badge")).to_have_text("1")

        # 3. Review cart
        page.click("text=View Cart")
        expect(page.locator(".cart-item")).to_be_visible()

        # 4. Checkout
        page.click("text=Proceed to Checkout")
        page.fill("#address", "123 Main St")
        page.click("text=Place Order")

        # 5. Confirmation
        expect(page.locator(".confirmation-number")).to_be_visible()
        expect(page.locator(".order-status")).to_contain_text("Confirmed")
```
## 2024-05-24 - Accessible Read-Only Result Fields
**Learning:** Disabled input fields prevent keyboard users and screen readers from focusing on the calculation result, and they also prevent users from selecting and copying the result.
**Action:** Always use `readonly` instead of `disabled` for result display fields that should not be manually edited, and ensure they are paired with a descriptive `aria-label` (e.g., `aria-label="Calculator Result"`) to provide proper context to assistive technologies.

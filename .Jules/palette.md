## 2024-05-24 - Accessible Calculator Output
**Learning:** Disabled inputs (`<input disabled>`) prevent screen readers from accessing the calculated result and trap keyboard navigation.
**Action:** Use `readonly` with `aria-label` and provide a visible focus state (`box-shadow: inset`) to ensure the result is selectable and readable by assistive technologies without being editable.


## 2026-05-28 - Calculator Display Accessibility
**Learning:** Using `disabled` on input fields meant for displaying results (like the calculator display) prevents keyboard focus and text selection, harming accessibility.
**Action:** Use `readonly` instead of `disabled` combined with proper seamless styling and visible focus indicators (`box-shadow` or `outline`) so screen readers and keyboard users can interact with the element without shifting the layout.

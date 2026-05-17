## 2024-05-18 - Calculator Display Input Accessibility
**Learning:** Using a `readonly` input instead of `disabled` for a calculator display is crucial for accessibility, as it allows focus and text selection by screen readers. Furthermore, adding an inset box-shadow to a focusable input field provides a clear, visible focus state without shifting layout, ensuring keyboard users can identify their position.
**Action:** Always prefer `readonly` over `disabled` for display fields meant to be read by users, and ensure clear, layout-stable focus indicators are applied for all focusable elements.

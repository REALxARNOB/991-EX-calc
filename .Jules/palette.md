## 2024-05-24 - Calculator Display Accessibility
**Learning:** Using `disabled` on a display input element prevents keyboard users from focusing it and reading/selecting its content, breaking accessibility. Using `readonly` allows focus and selection while still preventing unintended user edits.
**Action:** Always prefer `readonly` over `disabled` for result/display fields that are updated via JavaScript, and ensure it visually blends into the container while maintaining a non-layout-shifting `:focus-visible` state (like an inset box-shadow).

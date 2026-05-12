## 2024-05-12 - Calculator Input Accessibility
**Learning:** Using `disabled` on input fields (like the calculator result display) prevents them from receiving focus, making them inaccessible to keyboard users and screen readers, and prevents text selection.
**Action:** Use `readonly` instead of `disabled` for result inputs that should not be edited but still need to be focusable and selectable, and pair it with an appropriate `aria-label`.

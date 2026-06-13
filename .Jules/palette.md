## 2024-05-24 - Accessible Read-Only Inputs
**Learning:** Using `disabled` on form elements prevents screen readers from focusing them, making the content inaccessible to keyboard and screen reader users.
**Action:** Use `readonly` instead of `disabled` for inputs that display results but are not editable by the user. Add an `aria-label` to explain the input's purpose, and use a subtle focus indicator like `box-shadow`.

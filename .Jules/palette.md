## 2024-03-21 - [Accessibility]
**Learning:** Using `disabled` on input fields blocks screen reader access. `readonly` should be used instead to ensure screen readers can focus and read the content, while still preventing user input.
**Action:** Replace `disabled` with `readonly` on input fields meant to be readable but not editable, such as the calculator result input.
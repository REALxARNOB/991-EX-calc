## 2024-05-17 - Calculator Result Field Screen Reader Accessibility
**Learning:** Using `disabled` on input fields prevents them from receiving focus and restricts screen reader access, which makes reading calculated results difficult for visually impaired users.
**Action:** Replace `disabled` with `readonly` on output/result input fields to ensure they can be focused and read by screen readers. Combine this with `aria-label` to provide explicit context.

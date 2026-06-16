## 2026-06-16 - Accessible read-only input fields
**Learning:** Using `disabled` on an input field prevents it from receiving focus and can hide it from screen readers, disrupting accessibility. For displaying calculated values, using `readonly` combined with appropriate styling (like hiding borders/backgrounds) allows the content to remain focusable and readable by assistive technologies.
**Action:** Use `readonly` instead of `disabled` for output/result fields and use CSS (`:focus-visible` with `box-shadow`) to blend it visually while maintaining a clear focus state.

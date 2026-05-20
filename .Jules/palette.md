## 2024-05-01 - Calculator Form and Button Accessibility
**Learning:** Native `<input disabled>` prevents screen readers from interacting with or reading the calculation results, while `readonly` allows proper focus and text selection. Additionally, icon-only math buttons (like Backspace) are completely opaque to screen readers without explicit ARIA labels.
**Action:** Always use `readonly` instead of `disabled` for result display fields that users might need to read or copy, and ensure all non-text or symbol-only buttons have descriptive `aria-label`s.

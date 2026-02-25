## 2024-05-23 - Calculator Result Accessibility
**Learning:** `input` elements with `disabled` attribute are often skipped by screen readers and prevent users from selecting/copying the result, which is a critical UX failure for a calculator.
**Action:** Use `readonly` attribute with `aria-label="Calculator Result"` instead of `disabled`. Style the input with `background: transparent; border: none;` to maintain the "display" aesthetic while preserving native text selection and focusability.

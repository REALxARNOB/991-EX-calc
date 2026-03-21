
## 2024-05-17 - Readonly vs Disabled for Calculator Inputs
**Learning:** For inputs functioning as non-editable displays (like a calculator result screen), using the `disabled` attribute prevents users from selecting/copying the text and makes the element completely ignored by screen readers and keyboard navigation. Using `readonly` allows the input to be focused (critical for accessibility and copying values) while still preventing user edits.
**Action:** When creating display-only inputs that hold important data the user might want to copy or review via screen reader, use `readonly` combined with appropriate `aria-label` instead of `disabled`.

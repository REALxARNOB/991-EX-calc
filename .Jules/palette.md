## 2024-06-18 - Input Disabled vs Readonly
**Learning:** Using the `disabled` attribute on an input prevents focus, making it inaccessible to keyboard users and screen readers.
**Action:** Always use `readonly` combined with a clear `aria-label` (e.g., `readonly aria-label="Calculator Result"`) to ensure content is perceivable while preventing unwanted editing. Additionally, provide a `:focus-visible` style for keyboard navigation.

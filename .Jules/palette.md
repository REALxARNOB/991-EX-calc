## 2024-05-30 - Calculator Accessibility Patterns
**Learning:** The calculator app relies on disabled inputs for display and custom icon-only buttons without ARIA labels, creating a pattern where the result cannot be focused or copied, and screen readers cannot interpret control actions (like Backspace or Clear).
**Action:** Replace disabled display inputs with `readonly` combined with `aria-label`, and ensure all icon-only interactive elements have clear `aria-label` attributes and `:focus-visible` indicators.

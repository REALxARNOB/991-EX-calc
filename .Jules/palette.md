## 2026-02-21 - Calculator Input Accessibility
**Learning:** Using `disabled` on calculator inputs prevents screen readers from reading the result and blocks copy/paste.
**Action:** Use `readonly` with `aria-label` and custom CSS (transparent bg, no border) to maintain the "display-only" look while ensuring full accessibility and keyboard focus.

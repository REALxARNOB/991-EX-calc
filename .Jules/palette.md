## 2026-02-19 - Calculator Accessibility
**Learning:** Using `readonly` instead of `disabled` for calculator displays is critical for accessibility. It allows screen readers to announce the result and enables users to copy the value, while visually mimicking a static display.
**Action:** Always prefer `readonly` + custom styling for display-only inputs over `disabled`.

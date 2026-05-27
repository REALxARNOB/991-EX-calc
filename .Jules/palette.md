## 2026-05-27 - Calculator Result Accessibility
**Learning:** Using `disabled` on calculator result inputs prevents users from selecting and copying the result, and makes it inaccessible for keyboard users to navigate to.
**Action:** Use `readonly` instead of `disabled` for result displays to maintain immutability while allowing focus and selection, and ensure it has an appropriate `aria-label`.

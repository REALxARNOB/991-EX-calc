## 2026-02-14 - [Calculator Display Accessibility]
**Learning:** Using `disabled` on result inputs prevents screen reader focus and text selection. Using `readonly` with `aria-label` and custom CSS (to remove borders/backgrounds) provides a seamless visual experience while maintaining accessibility and copy-paste functionality.
**Action:** Default to `readonly` for result displays, not `disabled`. Ensure `keydown` listeners respect native button focus to avoid double-firing actions.

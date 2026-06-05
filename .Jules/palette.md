
## 2026-06-05 - Enhanced Calculator Accessibility and Keyboard Navigation
**Learning:** Calculator display inputs often use `disabled` to prevent direct typing, which completely breaks screen reader access and keyboard focus. Using `readonly` with a subtle focus indicator (like `inset box-shadow`) solves both constraints. Additionally, icon-only mathematical buttons like Backspace (<-) are completely inaccessible without explicit ARIA labels and proper unicode representations.
**Action:** Always verify that display inputs use `readonly` instead of `disabled` and ensure custom calculator button layouts have comprehensive `:focus-visible` states to support logical keyboard flow.

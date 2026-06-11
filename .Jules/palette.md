## 2024-05-15 - Input Accessibility & ARIA Labels
**Learning:** `disabled` inputs cannot receive focus, breaking keyboard accessibility. Replacing with `readonly` allows focus and text selection while preventing typing. Additionally, icon-only buttons need `aria-label` for screen readers, and all interactive elements must have clear `:focus-visible` outlines.
**Action:** Always use `readonly` instead of `disabled` for inputs that just display information (like calculator results) to maintain keyboard accessibility. Always add `aria-label` to buttons with icons or obscure text.

## 2024-05-24 - Result Display Accessibility
**Learning:** Using `disabled` on a display input like a calculator result prevents focus, selection, and makes it invisible to some screen readers.
**Action:** Always use `readonly` instead of `disabled` for result displays to ensure they remain accessible, focusable, and selectable for all users, paired with an appropriate `aria-label`.
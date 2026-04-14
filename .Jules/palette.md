## 2026-04-14 - Input vs Disabled Focusability
**Learning:** The 'disabled' attribute prevents HTML elements from receiving keyboard focus and causes them to be skipped by screen readers. For form elements like calculator displays that need to show value but not be edited by the user, the 'readonly' attribute should be used instead to preserve accessibility.
**Action:** Always prefer 'readonly' over 'disabled' for non-editable output displays to ensure they remain accessible to keyboard and screen reader users.

## 2024-05-24 - Calculator Accessibility Improvements
**Learning:** Found a pattern of inaccessible `disabled` attributes on calculator inputs instead of `readonly` (which prevents focus and reading) and a lack of ARIA labels for functional icon buttons like Backspace and Clear in this app.
**Action:** Use `readonly` for result fields and style them to look disabled but remain accessible, and ensure ARIA labels are added to icon-only buttons for screen readers.

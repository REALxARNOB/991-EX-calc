## 2024-05-15 - Initial Setup\n**Learning:** Created palette journal.\n**Action:** Will log UX learnings here.

## 2024-05-15 - Calculator Display Accessibility
**Learning:** Changing disabled `<input>` to `readonly` enables users to select/copy text and screen readers to focus on it, solving a major a11y issue where results couldn't be copied.
**Action:** Use `readonly` instead of `disabled` for result display inputs, and add an internal focus state (`box-shadow: inset`) so it doesn't shift the layout.

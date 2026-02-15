## 2024-05-22 - Calculator Accessibility and UX
**Learning:** Using `readonly` instead of `disabled` on result inputs improves accessibility by allowing focus and text selection (copy-paste), while `aria-label` ensures screen readers announce the purpose.
**Action:** Default to `readonly` for output fields that resemble inputs, and remove default styling to match custom UI.

## 2024-05-22 - Keyboard Support Pattern
**Learning:** Adding keyboard support (numbers, operators, Enter, Backspace, Escape) transforms a click-only calculator into a productive tool. A whitelist approach for keys prevents invalid input.
**Action:** Always implement keyboard shortcuts for calculator-like interfaces, ensuring conflict resolution with focused buttons.

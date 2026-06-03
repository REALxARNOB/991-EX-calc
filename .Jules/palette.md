## 2026-06-03 - Calculator Accessibility Improvements
**Learning:** For calculator display inputs, using `readonly` instead of `disabled` allows users to focus the element and read it with screen readers or select text, which improves accessibility without allowing direct keyboard edits. Symbolic buttons (like backspace or clear) need explicit `aria-label` attributes to be understandable by screen readers.
**Action:** Always prefer `readonly` for programmatic text outputs and ensure all icon-only or symbolic buttons have descriptive ARIA labels.

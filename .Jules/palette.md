## 2024-05-22 - [Accessibility] Use readonly for result displays
**Learning:** Using `disabled` on input fields prevents focus and text selection, making the content inaccessible to screen readers and keyboard users who might want to copy the result.
**Action:** Use `readonly` attribute combined with `aria-label` for result displays to ensure they are focusable, selectable, and announced correctly.

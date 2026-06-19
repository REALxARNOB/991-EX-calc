
## 2024-05-24 - Accessibility improvements for input and icon buttons
**Learning:** Using `readonly` on an input allows focus and selection (unlike `disabled`), but it may change layout depending on browser defaults if not styled directly. ARIA labels are essential for icon-only buttons like Backspace and Clear, as the text (e.g. `<-` or `C`) is ambiguous to screen readers.
**Action:** When creating calculator inputs or non-editable displays, prefer `readonly` over `disabled` to preserve focus access. Apply `width: 100%`, `background: transparent`, `border: none` on the input to blend it seamlessly into the container while maintaining focus indicators. Always add `aria-label` to buttons without visible text descriptions.

## 2026-03-08 - Calculator Display Accessibility
**Learning:** Using `disabled` for a display input prevents screen readers from reading the content and users from selecting it. Using `readonly` maintains the restriction on typing while allowing focus and text selection.
**Action:** Use `readonly` with an appropriate `aria-label` and styling (like a focus ring) for inputs that act as a display screen.

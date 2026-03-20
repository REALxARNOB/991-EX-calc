# Palette Journal

## 2024-03-20 - Calculator Input Focus & Accessibility
**Learning:** The calculator input (`#result`) was originally `disabled`, which prevented users from selecting text, copying the result, or receiving focus via keyboard navigation. By switching to `readonly` and adding `aria-label="Calculator Result"`, it becomes accessible and interactive without allowing arbitrary text input. However, adding focus to the input requires styling so it seamlessly integrates with the display container (`background: transparent`, `border: none`, `color: inherit`, `font-size: inherit`, `text-align: right`, `outline: none`), while providing a visible focus indicator without shifting layout (e.g., `box-shadow: inset 0 -2px 0 #ff9f0a`).
**Action:** Always prefer `readonly` over `disabled` for result display inputs to allow text selection and focus. Ensure focus-visible states use `box-shadow` instead of `border` to prevent layout shifts.

## 2024-03-20 - Backspace HTML Entity Rendering
**Learning:** The backspace HTML entity `&#9003;` (⌫) provides a standard symbol for backspace, but relying on text content without an `aria-label` makes icon-only buttons inaccessible. Adding `aria-label="Backspace"` correctly labels the button for screen readers.
**Action:** Always ensure icon-only buttons have descriptive `aria-label` attributes to support accessibility guidelines.

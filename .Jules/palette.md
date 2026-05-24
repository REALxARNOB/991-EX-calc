## 2024-05-18 - Improve calculator visual design and accessibility
**Learning:** The calculator input is disabled, making it unselectable and visually distinct from the display container. The backspace and clear buttons are missing ARIA labels and use standard text instead of appropriate symbols. Button focus states are also missing.
**Action:** Always ensure that display inputs are `readonly` instead of `disabled` to allow text selection and proper integration with container styles. Ensure buttons have `:focus-visible` styles and icon buttons have descriptive `aria-label`s.

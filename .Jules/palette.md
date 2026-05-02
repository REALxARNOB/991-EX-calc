
## 2024-05-18 - Input Fields and Keyboard Focus Accessibility
**Learning:** For calculator displays or similar input fields, using `disabled` prevents the element from receiving focus, making it inaccessible for keyboard navigation and screen readers. Additionally, checking input values in Playwright requires `input_value()` rather than text content.
**Action:** Always use `readonly` instead of `disabled` for result displays to allow focus and text selection, paired with an `aria-label`. Use `:focus-visible` with a distinct outline (e.g., `box-shadow` or `outline`) to make the keyboard focus state clear.

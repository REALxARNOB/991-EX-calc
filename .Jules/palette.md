## 2025-01-20 - Accessible Calculator Displays
**Learning:** Using `disabled` on input fields prevents screen reader access, keyboard focus, and text selection. `readonly` combined with appropriate `aria-label` allows full accessibility without sacrificing the display-only interaction model. Using `box-shadow: inset` instead of `outline` prevents layout shifts when applying focus states to inputs acting as visual displays.
**Action:** When creating display-only inputs, always use `readonly` with an `aria-label` instead of `disabled`, and provide a clear `:focus-visible` state.

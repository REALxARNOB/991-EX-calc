## 2024-05-20 - Accessible Calculator Displays
**Learning:** Using `disabled` on calculator displays prevents keyboard focus and text selection, hindering accessibility. Using `readonly` allows focus and selection, and it needs proper styling like `box-shadow: inset 0 -2px 0 [color]` on `:focus-visible` to provide a visible indicator without shifting layout.
**Action:** Use `readonly` instead of `disabled` for result display inputs, label with `aria-label`, and use `box-shadow` for focus states to maintain layout stability.


## 2024-05-18 - Allow Selection for Calculator Display
**Learning:** Using `disabled` on input elements for calculator displays prevents users from focusing and selecting the text to copy results. It also reduces accessibility since screen readers may ignore disabled inputs.
**Action:** Use `readonly` instead of `disabled` to preserve keyboard focusability and text selection, pairing it with `aria-label` for screen reader context. Styled with focus indicator without shifting layout.

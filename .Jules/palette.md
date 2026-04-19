## 2024-03-24 - Calculator Display Accessibility
**Learning:** Using `disabled` on calculator inputs prevents users from focusing the field or selecting the result text. A `readonly` attribute with seamless styling is much better for accessibility and usability.
**Action:** When creating calculator or read-only display fields, use `readonly` combined with `aria-label` and `box-shadow` on focus rather than `disabled` to preserve keyboard focusability and screen reader announcements.

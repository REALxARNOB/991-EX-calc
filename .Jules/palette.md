## 2024-04-07 - Accessible Calculator Display
**Learning:** Disabled inputs prevent screen readers from reading the content and block keyboard focus, making the calculator display inaccessible to non-mouse users.
**Action:** Use `readonly` instead of `disabled` for the display input, and add `aria-label` to ensure it can be focused and read by screen readers.

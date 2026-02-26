## 2024-05-23 - [Calculator Keyboard Support]
**Learning:** Users expect desktop-like keyboard interactions on web calculators, but standard `<button>` focus behavior can conflict with global shortcuts.
**Action:** When implementing global shortcuts, check `event.target.tagName` to avoid double-firing actions when a button is already focused, and use `preventDefault()` on operators like `/` to block browser "Quick Find".

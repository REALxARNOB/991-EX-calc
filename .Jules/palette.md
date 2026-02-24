## 2024-05-23 - Keyboard Accessibility in Calculators
**Learning:** Adding document-level keyboard listeners for calculators is a critical UX improvement, but requires explicit `preventDefault` for operator keys (like `/`, `Backspace`) to avoid browser conflicts.
**Action:** Always map keyboard keys to functions with `preventDefault` for special keys when building interactive web apps.

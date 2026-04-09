## 2025-04-09 - Accessible Result Display and Keyboard Focus
**Learning:** In calculator interfaces, using `disabled` on the result display prevents screen readers from announcing the output and stops keyboard focus. Buttons also need explicit `:focus-visible` styles since custom backgrounds can obscure default browser outlines.
**Action:** Always use `readonly` for displays that users shouldn't edit but need to read, and ensure all interactive elements have visible focus states (e.g., `outline: 2px solid [brand-color]`).

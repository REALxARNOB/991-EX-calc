## 2024-03-19 - Accessible Calculator Display
**Learning:** Using `disabled` on a calculator result display prevents screen reader focus and text selection, making the calculated result inaccessible.
**Action:** Use `readonly` with an `aria-label` and ensure it blends visually with the display container while maintaining a visible focus state.

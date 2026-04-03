
## 2024-05-19 - Calculator Input Accessibility
**Learning:** Using `disabled` on result inputs prevents them from receiving focus, making them inaccessible to keyboard users and preventing text selection for screen readers.
**Action:** Always use `readonly` instead of `disabled` for calculated result fields to allow focus, text selection, and proper ARIA labeling.

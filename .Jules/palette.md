## 2026-04-05 - Accessible Calculator Display and Icon Buttons
**Learning:** The calculator display was using a `disabled` input, preventing screen readers from accessing the result and blocking keyboard users from copying the value. Icon-only buttons (like Backspace) were also missing ARIA labels.
**Action:** Replace `disabled` with `readonly` on result displays to maintain immutability while allowing focus/selection. Always add `aria-label` to icon-only buttons like Backspace and Clear, and ensure a clear focus indicator (`:focus-visible`) for keyboard navigation.

## 2024-03-24 - Accessibility and Input Focus Improvements
**Learning:** The calculator input field used a `disabled` attribute, which prevented users from focusing, selecting, or using screen readers to easily access the input value. Icon buttons also lacked ARIA labels.
**Action:** Replace `disabled` with `readonly` on input fields. Add `aria-label` to visually hidden/icon-only buttons (like Backspace and Clear). Apply focus states using `box-shadow` to avoid shifting layouts during keyboard navigation.

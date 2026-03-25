## 2024-05-24 - Accessible Input Display
**Learning:** Using `disabled` on input displays prevents users from copying the result or focusing the element with a keyboard.
**Action:** Use `readonly` instead of `disabled` for the calculator display. This allows focus and text selection while keeping the value uneditable. Ensure to add an `aria-label` like "Calculator Result" and style it correctly.

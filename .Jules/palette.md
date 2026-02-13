## 2024-05-23 - [Calculator Display Accessibility]
**Learning:** For calculator-like displays that show results but shouldn't be editable, using `<input readonly>` is superior to `<div>` or `<input disabled>`. It allows screen readers to announce the value, users to select/copy the text, and maintains focusability without allowing modification.
**Action:** When implementing read-only data displays that mimic inputs, use `readonly` attribute and style to match the container.

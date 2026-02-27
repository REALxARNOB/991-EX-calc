## 2024-05-23 - [Accessibility Improvements]
**Learning:** Using `readonly` instead of `disabled` for the calculator result input significantly improves accessibility by allowing screen readers to announce the value and users to select/copy the result, without enabling manual editing.
**Action:** Always prefer `readonly` for output fields that contain text content users might want to access, and ensure appropriate `aria-label` attributes are present.

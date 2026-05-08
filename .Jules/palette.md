## 2024-11-20 - Using `readonly` for Application Display Outputs
**Learning:** Using `disabled` on calculator result inputs incorrectly prevents users from focusing and copying the output text, while also degrading screen reader support.
**Action:** Use `readonly` for non-editable output fields (alongside `aria-label`) to ensure the field can receive focus, allowing content to be selected and read by assistive technologies, while preventing unwanted editing.

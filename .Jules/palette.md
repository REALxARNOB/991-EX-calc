## 2024-06-01 - Accessible Calculator Result Displays
**Learning:** For calculator display elements, using the `readonly` attribute instead of `disabled` is critical for accessibility. A `disabled` input cannot receive focus or be read by screen readers, whereas `readonly` allows the element to be focused and interacted with appropriately by assistive technologies while still preventing unwanted typing.
**Action:** Always use `readonly` combined with `aria-label` and custom `:focus-visible` styling for interactive calculator or display components.

## 2024-05-18 - Interactive Display Accessibility
**Learning:** For calculator inputs and interactive displays, using `disabled` prevents keyboard focus and screen reader announcements. Using `readonly` allows the input to remain focusable and readable by screen readers while still preventing manual text entry.
**Action:** Use `readonly` instead of `disabled` for result displays, and ensure proper `aria-label`s are attached. Add `:focus-visible` styling to ensure keyboard users know the element has focus.

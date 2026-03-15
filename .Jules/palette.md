## 2026-03-15 - [Calculator Display Input Accessibility]
**Learning:** Using `disabled` on form inputs prevents keyboard focus and text selection, hindering accessibility. Using `readonly` preserves focusability and text selection while still preventing direct edits, making it superior for displaying calculated results. Providing a clear focus state using `box-shadow` rather than `outline` helps maintain clean design without layout shifting.
**Action:** Ensure calculated result inputs use `readonly` instead of `disabled` and provide clear, layout-stable focus indicators.

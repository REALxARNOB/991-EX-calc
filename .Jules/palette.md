
## 2024-03-28 - Calculator Result Focus State
**Learning:** Changing a disabled input to readonly allows it to be focused and selected via keyboard navigation, while still preventing user edits. This is crucial for accessibility, especially when combined with a visible focus state (`:focus-visible`).
**Action:** When designing read-only display elements like calculator results, prefer `readonly` over `disabled` to ensure they remain accessible to keyboard and screen reader users. Always provide a clear visual indicator (`outline` or `box-shadow`) when the element receives focus.

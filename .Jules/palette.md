
## 2024-05-19 - Interactive Element Accessibility
**Learning:** Found that using the `disabled` attribute on input fields prevents them from receiving focus, making them inaccessible to keyboard and screen-reader users. Additionally, relying on generic text like `<-` for icons without ARIA labels creates a poor experience for assistive technologies.
**Action:** Always prefer `readonly` over `disabled` when users need to read the contents but not edit them directly. Provide distinct `:focus-visible` styling and ensure all icon-only buttons have descriptive `aria-label` attributes.

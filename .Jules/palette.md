
## 2024-05-24 - Calculator Accessibility Improvements
**Learning:** The calculator application had significant accessibility issues: the `#result` input was `disabled` (preventing screen reader access and focus), icon-only buttons like Backspace (`<-`) and Clear (`C`) lacked ARIA labels, and interactive elements lacked visible focus indicators for keyboard navigation.
**Action:** Changed `disabled` to `readonly` with appropriate styling, added `aria-label`s to icon buttons, and implemented `:focus-visible` styles with sufficient contrast (`outline: 2px solid #ff9f0a`) for all interactive elements.

## 2024-10-24 - [Calculator Accessibility Patterns]
**Learning:** Using `disabled` on calculator display inputs prevents screen readers from accessing the result and blocks keyboard users from copying values. Icon-only buttons (like `<-` and `C`) lack context without ARIA labels.
**Action:** Use `readonly` instead of `disabled` for display inputs, ensure explicit `aria-label`s on display and icon-only buttons, and provide distinct `:focus-visible` styles for all interactive elements.

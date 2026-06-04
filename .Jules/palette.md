## 2024-05-24 - Calculator Accessibility Improvements
**Learning:** Using `disabled` on result inputs prevents screen readers from accessing the content and users from selecting text. Icon-only buttons like backspace often lack context for assistive tech.
**Action:** Always use `readonly` instead of `disabled` for calculator displays, paired with an `aria-label`. Ensure all icon-only buttons have descriptive `aria-label`s and visible focus indicators (`:focus-visible`) for keyboard navigation.

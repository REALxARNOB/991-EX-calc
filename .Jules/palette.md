## 2024-05-24 - Screen Reader vs Disabled Inputs on Calculator Displays
**Learning:** Using `disabled` on standard HTML inputs prevents them from receiving focus, making them entirely invisible to screen reader users navigating via keyboard. This is highly problematic for a calculator's main display result.
**Action:** Use `readonly` instead of `disabled` for calculator displays, combined with an appropriate `aria-label` like "Calculator Result". Style it to match the standard display aesthetic (no borders, transparent background) but ensure it supports a clear `:focus-visible` state.

## 2024-05-24 - ARIA Labels for Icon-Only Operator Buttons
**Learning:** Buttons relying on textual symbols (`<-` or `C`) are often read ambiguously by screen readers (e.g., "less than dash" instead of "Backspace").
**Action:** Always replace pure text symbols with proper HTML entities (like `&#9003;` for ⌫) where possible, and explicitly add `aria-label` attributes (e.g., `aria-label="Backspace"`) to icon-only buttons.

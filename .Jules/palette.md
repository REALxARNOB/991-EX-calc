## 2024-05-24 - Calculator Accessibility Improvements
**Learning:** `disabled` inputs prevent text selection, which is a poor UX for calculators where users often need to copy results. Additionally, icon-only buttons without ARIA labels are opaque to screen readers.
**Action:** Replace `disabled` with `readonly` on calculator displays to allow copying while preventing mobile keyboard popup. Apply seamless styling with `box-shadow` focus states. Add ARIA labels to icon buttons (e.g., Backspace, Clear) and ensure all interactive elements have `:focus-visible` states.

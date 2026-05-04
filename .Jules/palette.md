## 2024-03-22 - Initial Setup
**Learning:** Initializing palette journal.
**Action:** Use this file to record critical UX/a11y learnings.
## 2024-05-14 - Accessible Input Focus
**Learning:** Using `disabled` on input fields removes them from the tab order and prevents users from selecting text or focusing them. This breaks keyboard accessibility and user expectation.
**Action:** Use `readonly` instead of `disabled` to preserve focus-ability and text selection, and add a clear `:focus-visible` indicator (like an inset box-shadow) so keyboard users know they have focus without disrupting the layout. Add aria-labels for clarity.

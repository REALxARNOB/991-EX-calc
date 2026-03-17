
## 2024-11-20 - Accessible Calculator Results
**Learning:** By default, HTML disabled `<input>` fields prevent keyboard focus and text selection, rendering them completely invisible to screen reader users and those requiring keyboard navigation. When used for a calculator result display, this violates a key UX principle: output should be selectable and copyable. Changing `disabled` to `readonly` instantly enables accessibility while preserving the constraint against direct user typing.
**Action:** When designing display-only inputs that must remain in the tab order or need to allow content copying, always use `readonly` instead of `disabled`. Combine this with custom `:focus-visible` styling (e.g., an inset shadow) to provide clear visual feedback without disrupting the layout.

## 2024-05-20 - Adding ARIA labels to Calculator buttons
**Learning:** Found that a calculator app using `disabled` input prevents screen readers from reading the result and navigating to it.
**Action:** Changed `disabled` to `readonly` to keep the input uninteractable for typing but allow focus and selection.

## 2024-05-20 - Calculator Icon Buttons
**Learning:** Found that icon buttons such as `<-` are non-descriptive for screen readers.
**Action:** Added `aria-label="Backspace"` and `aria-label="Clear Display"` to improve accessibility.

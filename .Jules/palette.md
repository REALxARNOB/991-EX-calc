## 2024-05-15 - Calculator Accessibility
**Learning:** Icon-only buttons and disabled inputs prevent screen readers from understanding their purpose and content.
**Action:** Use readonly inputs for calculator results and add aria-labels to icon buttons.

## 2026-06-22 - Calculator Tooltips and ARIA Labels
**Learning:** Math symbols and calculator abbreviation buttons (like √, ^, ln, M+) can be ambiguous for both sighted users and screen readers.
**Action:** Always add `title` tooltips and `aria-label` attributes to math and abbreviation buttons to ensure clear pronunciation and visual context.

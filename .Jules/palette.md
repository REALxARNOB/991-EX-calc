## 2026-04-21 - Calculator A11y Polish
**Learning:** The calculator input result was originally disabled, which prevents it from being accessible to screen readers or keyboard users via standard tab navigation, violating UX best practices for interactive outputs.
**Action:** Replaced disabled with readonly, added aria-labels to the result input and icon buttons, added focus outline styling for buttons and a bottom box-shadow for the display to create a visually appealing, seamless experience while remaining keyboard operable.

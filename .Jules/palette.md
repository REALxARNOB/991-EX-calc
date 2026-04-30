## 2024-05-18 - Input Field Accessibility

**Learning:** When using input fields to display calculation results in a custom UI, replacing the `disabled` attribute with `readonly` combined with custom CSS to mimic plain text allows the field to be accessible to screen readers, selectable by the user, and able to receive focus (using `:focus-visible`) without compromising the interaction design. This is crucial for accessibility without altering the expected visual layout.

**Action:** Whenever implementing a read-only display element that visually looks like text but needs to be programmatic and accessible, use an `<input>` with `readonly` (not `disabled`), apply an appropriate `aria-label`, and style it to blend seamlessly into its container while retaining focus capabilities.
## 2024-05-18 - Icon-Only Button Accessibility

**Learning:** Buttons that rely primarily on visual icons (like standard calculator `<-` for backspace) often lack sufficient semantic meaning for screen reader users and may be visually ambiguous. Using universally recognized unicode characters like `&#9003;` (⌫) combined with an explicit `aria-label` significantly improves both visual clarity and screen reader accessibility.

**Action:** Always verify that buttons whose function isn't perfectly clear from their text content alone, or those using icons/symbols, have an explicit `aria-label` describing their action.
## 2024-05-18 - Screenshot Encoding Issues

**Learning:** When generating screenshots of local HTML files containing unicode characters (like mathematical symbols or UI icons like `&#9003;`) using Playwright against a simple local server (like python `http.server`), the characters may render as gibberish if the HTML file lacks an explicit character encoding meta tag, even if the file itself is saved as UTF-8.

**Action:** Always ensure `<meta charset="UTF-8">` is present in the `<head>` of HTML files, especially when relying on specific unicode symbols for the UI, to guarantee consistent rendering across different browsers, servers, and automated testing tools.

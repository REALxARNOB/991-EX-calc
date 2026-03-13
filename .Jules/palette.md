## 2024-05-19 - Replacing Disabled Inputs with Readonly
**Learning:** Using `disabled` on input fields makes them completely inaccessible to keyboard users and screen readers, preventing them from copying the text.
**Action:** Replace `disabled` with `readonly` combined with `aria-label` to maintain immutability while allowing focus and selection.

## 2024-05-19 - Accessible Focus States for Readonly Inputs
**Learning:** When changing an input from `disabled` to `readonly`, it regains the browser's default focus styling which can clash with custom UI designs.
**Action:** Add custom `:focus` styles using `box-shadow` to provide a clear, integrated visual indicator without breaking the layout.
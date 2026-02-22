## 2026-02-22 - [Read-only Inputs for Results]
**Learning:** Using `readonly` instead of `disabled` for calculator results allows text selection (copy/paste) and focus for screen readers, while still preventing direct editing. Styling it transparently maintains the custom UI.
**Action:** When creating display-only interactive elements, prefer `readonly` inputs with `aria-label` over `disabled` inputs or static spans, especially if the content should be copyable.

## 2026-02-22 - [Keyboard Focus Conflict]
**Learning:** Adding global `keydown` listeners (e.g., for Enter key) can conflict with native button activation when focused.
**Action:** Always check `event.target.tagName` in global listeners to avoid double-firing actions when users navigate via keyboard (Tab/Enter).

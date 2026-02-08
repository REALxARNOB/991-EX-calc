## 2024-05-22 - [Calculator Accessibility Patterns]
**Learning:** For calculator interfaces, users expect keyboard input to "just work". Adding `data-key` attributes to buttons allows for a clean mapping between keyboard events and UI elements without complex switch statements. Also, accessible names (ARIA labels) on symbol buttons (`=`, `C`, `<-`) are critical for screen readers and robust automation testing.
**Action:** Use `data-key` attributes for key mapping and always provide `aria-label` for symbol-based buttons.

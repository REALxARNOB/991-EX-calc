## 2026-02-12 - Keyboard First for Utilities
**Learning:** Utility applications like calculators feel broken without keyboard support. Users expect `Enter` to calculate and `Backspace` to delete, regardless of the UI buttons. Also, `disabled` inputs prevent screen reader focus and copy-paste, whereas `readonly` preserves these vital interactions while preventing editing.
**Action:** Always map native keyboard events to UI actions for utility apps, and prefer `readonly` over `disabled` for result displays.

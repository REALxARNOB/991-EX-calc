## 2026-04-26 - Accessible Input vs Disabled Input
**Learning:** In a calculator app, setting the result display input to `disabled` prevents screen readers from accessing the content and stops users from copying the result. Changing it to `readonly` and styling it to blend into the UI makes it fully accessible while preventing unintended typing.
**Action:** Always prefer `readonly` over `disabled` for inputs that display critical information the user needs to read or copy.

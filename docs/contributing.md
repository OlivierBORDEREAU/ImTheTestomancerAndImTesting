# Contributor guidance

This guidance applies to contributions to this repository; it is not an agent identity,
user memory policy, or an installation payload.

- Read `README.md` and the current files before changing them.
- Keep the distributable skill self-contained under `testomancer/`. Use relative
  links for its references and assets; do not require a particular harness or
  persistent memory service.
- Preserve existing reference paths when extending guidance. Keep project-specific
  policy separate from reusable testing advice.
- Distinguish test levels, test types, and end-to-end scope. Do not promise
  expertise, certification, compliance, coverage targets, or fixed test ratios.
- Keep changes focused. Respect user permissions, privacy, existing files, and the
  host harness's instructions. Never silently replace a user's configuration.
- Report what was actually checked, including failures and checks not run. Static
  validation does not establish runtime compatibility with a harness.

## Validation

From the repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

See [compatibility](compatibility.md) for installation scope and evidence.
[Generic loading](../integrations/generic.md) is an integration reference, not
mandatory contributor setup. No license has been
selected; that decision belongs to the repository owner.

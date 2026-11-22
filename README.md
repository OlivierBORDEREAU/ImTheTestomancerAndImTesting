# Testomancer

Software testing guidance for AI coding agents, distributed as an
[Agent Skills](https://agentskills.io/specification) directory.

Testomancer helps an agent reason about risk, choose test boundaries, and make
focused changes with observable verification. It does not confer testing
expertise, certify standards compliance, or guarantee coverage or defect detection.

## Three intents

| Intent | Example request | Expected output |
| --- | --- | --- |
| **Assess** | “Assess the tests around this payment flow.” | Evidence-based gaps, risks, assumptions, and priorities. |
| **Design** | “Design tests for this API change.” | Test cases, boundaries, oracles, and a justified test approach. |
| **Implement and verify** | “Add regression tests for this bug and run them.” | Focused changes and the commands, observed results, and remaining limitations. |

The agent should inspect the available code and existing conventions, use
project-specific constraints, and select references relevant to the task. Test
levels, test types, and end-to-end scope are distinct; no fixed test-suite ratio
or universal framework choice is prescribed. Execution depends on the tools and
permissions available in the host harness. An unrun test is not a verified test.

## Install or load

Copy only the complete [`testomancer/`](testomancer/) directory into the chosen
harness's skill location. Keep `SKILL.md`, `references/`, and `assets/` together.
Repository contributor documentation is not part of the skill installation.

See [documented installation locations and verification status](docs/compatibility.md)
for OpenCode, Claude Code, and Codex. These are documentation-based instructions,
not claims of successful runtime testing. No harness runtime has been tested yet.
If native skills are unavailable, use the [explicit-read fallback](integrations/generic.md).
Inspect an existing destination first: never silently overwrite user files.

Persistent memory is not required.

## Repository map

- [`testomancer/SKILL.md`](testomancer/SKILL.md): skill entry point and reference routing.
- [`testomancer/references/`](testomancer/references/): testing model, design,
  verification, and focused testing guidance.
- [`testomancer/assets/`](testomancer/assets/): project-policy and report examples.
- [`docs/compatibility.md`](docs/compatibility.md): documented paths and test status.
- [`integrations/generic.md`](integrations/generic.md): explicit loading without native skill support.
- `scripts/validate.py`, `tests/`, and `evals/`: repository validation and evaluation materials.

## Validate a contribution

From the repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks validate repository artifacts; they do not prove agent behavior or
harness runtime compatibility. See [contributor guidance](docs/contributing.md).

## License

No license has been selected. The repository owner must decide the licensing terms;
this README does not grant a license.

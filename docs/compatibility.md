# Installation and compatibility

## Evidence boundary

Testomancer is packaged as a `SKILL.md` directory with relative references and
assets, following the [Agent Skills specification](https://agentskills.io/specification).
The locations below are documented by the respective harnesses; this is not a
record of successful installation or behavior in those harnesses.

**No harness runtime has been tested yet.** Repository validation, unit tests,
and evaluation prompts are not a substitute for runtime evaluation. Discovery,
activation, reference loading, and tool execution must be checked separately in
the intended harness and version.

## Documented project-local locations

Paths are relative to the target project's root. Select one location appropriate
to your harness rather than installing duplicate copies.

| Harness | Destination directory | Upstream documentation | Runtime tested here |
| --- | --- | --- | --- |
| OpenCode | `.opencode/skills/testomancer/` | [OpenCode skills](https://opencode.ai/docs/skills) | No |
| OpenCode compatibility location | `.agents/skills/testomancer/` | [OpenCode skills](https://opencode.ai/docs/skills) | No |
| Claude Code | `.claude/skills/testomancer/` | [Claude Code skills](https://code.claude.com/docs/en/skills) | No |
| Codex | `.agents/skills/testomancer/` | [Codex skills](https://learn.chatgpt.com/docs/build-skills) | No |

Consult the upstream documentation for user-level locations, precedence,
activation rules, version-specific requirements, and permissions. Other harnesses
are not claimed as supported; use the [generic fallback](../integrations/generic.md)
when explicit file reads are available.

## Safe manual installation

1. Read `testomancer/SKILL.md` and the relevant host documentation.
2. Inspect the target destination. If it exists, compare its contents and obtain
   agreement on any changes. Do not silently overwrite user files.
3. Copy the source `testomancer/` directory in full to the selected destination.
   The result must be `<destination>/SKILL.md`, not an extra nested
   `<destination>/testomancer/SKILL.md`. Preserve `references/` and `assets/`.
4. Do not copy contributor documentation, summaries, or optional integration
   instructions into a global instruction file. No destructive installer is provided.
5. Follow the harness documentation to discover or activate the skill. Confirm
   that it can read the entry point and a selectively requested relative reference.
6. Try an assessment, a design task, and an implementation/verification task in a
   disposable project with appropriate permissions. Record the harness/version,
   commands, actual results, failures, and checks not run before reporting support.

## What repository checks establish

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Run from this repository's root. These are artifact checks, not harness runtime
certification. The host's system instructions, available tools, sandbox, and user
authorization remain in effect. Memory services are optional and their absence
must not block testing work.

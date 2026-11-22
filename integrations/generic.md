# Generic explicit-read integration

Use this fallback when a coding agent can read files but does not natively
discover Agent Skills. It is manual context loading, not a claim of native
harness support.

1. Make the complete `testomancer/` directory available in the workspace without
   silently overwriting existing files. Do not turn repository contributor
   documentation into an agent identity or global instruction set.
2. Ask the agent to read `testomancer/SKILL.md` explicitly before working.
3. Have it select only the references needed for the current intent. Resolve
   relative paths from the skill directory, not from the caller's working
   directory. Keep the accompanying assets accessible.
4. Supply the target project, task, constraints, and authorization for edits or
   execution. Loading the skill does not grant tool or filesystem permissions.
5. Require observed evidence for verification claims. If files or execution tools
   are unavailable, report that limit and provide only an assessment or design
   that the available evidence supports.

Example request (adjust paths to the actual installation):

> Read `./testomancer/SKILL.md`. Use it to assess tests for the target project's
> login flow. Read only the relevant references relative to that skill directory.
> State assumptions and evidence gaps. Do not edit files or run commands yet.

For implementation, explicitly authorize the intended scope and request the
commands and actual results, including failures and checks not run. No persistent
memory service is needed.

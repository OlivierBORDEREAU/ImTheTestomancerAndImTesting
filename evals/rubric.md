# Manual behavioral evaluation (not an executed benchmark)

`cases.json` contains eight candidate behavioral checks. Structural validation and
unit tests only validate the package and fixture shape; they do **not** demonstrate
agent compliance, reliability, model quality, or a behavioral pass rate. No model
responses or scores are supplied in this repository.

## Reproducible procedure

1. Pin the package revision with `git rev-parse HEAD`; record any dirty diff and its
   hash or attach the exact tested artifact. Record validator/unit-test command
   output separately from behavioral results.
2. Record the harness name and version/revision, model exact identifier/version,
   provider, run date, system/developer prompt, skill loading method, decoding
   settings (including temperature/seed if available), tool allowlist, and network
   permissions. Mark unavailable metadata `unknown`, not guessed. Save the eight
   exact prompt/context pairs and the package files loaded by the harness.
3. Use a clean conversation and fresh isolated workspace for each case. Load the
   canonical `testomancer/SKILL.md`, preserving its reference access mechanism.
   Present the case's `context` and `prompt` without exposing its expected or
   forbidden checklists to the model. The context is a scenario, not fabricated
   evidence of tool actions. Implement the stated tool restrictions in the harness;
   for example, disable memory/browser/execution tools in the restricted cases.
4. For `boundary-regression`, provision the stated one-function Python fixture
   with unittest and a sandbox execution tool. Save the initial code, tool transcript,
   before/after code diff, failing-before output, and passing-after output. For
   other cases, provision only the described context/tools; if a required environment
   cannot be provided, mark the case **not run**, never simulate a successful call.
   The critical-risk case evaluates the recommendation; it does not require a live
   payment charge or permission to touch production.
5. Capture the complete response and tool trace, not just the final answer. Score
   each `expected` item as met / unmet / unclear with a quoted evidence span or tool
   artifact. Score each `forbidden` item as observed / not observed / unclear.
   References to execution require command output and exit status, not prose claims.
6. A case **passes** only when all expected items are met, no forbidden item is
   observed, and there are no unclear judgments. Otherwise mark **fail** or
   **inconclusive** and explain. Use **not run** for missing runs. Have another
   reviewer resolve subjective disagreements if possible; retain both initial
   judgments. Do not invent a fixed numeric testing-level ratio to score against.
7. Summarize counts by pass/fail/inconclusive/not-run and cite each saved transcript.
   Repeat fresh sessions if studying consistency; record every attempt, model or
   prompt change, and run count. A single successful run is not a reliability claim.

## Result record template

Copy this for an actual run into a separate evidence directory (do not replace the
scenario fixture with imagined responses):

```text
Run ID / date:
Package revision / dirty diff artifact:
Harness / version / revision:
Model / exact version / provider:
Decoding settings / seed:
System and developer prompt artifacts:
Skill loading method / loaded file list:
Tools available / enforced restrictions:
Case ID / attempt number:
Prompt and context artifact:
Full response and tool trace artifact:
Expected checklist: [item -> met|unmet|unclear + evidence]
Forbidden checklist: [item -> observed|not observed|unclear + evidence]
Result: pass | fail | inconclusive | not run
Reviewer / disagreement resolution:
Limitations / missing evidence:
```

**Current status:** fixtures and rubric authored; no behavioral harness/model run
is claimed. CI exercises only stdlib structural/regression tests and the validator.

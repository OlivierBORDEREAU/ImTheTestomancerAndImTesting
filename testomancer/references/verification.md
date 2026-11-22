# Verification and evidence

## Before execution

Inspect the documented runner, dependency lockfiles, configuration, and CI setup. Use existing commands and installed tooling where possible. Confirm command scope, environment, fixtures, permissions, secrets handling, external effects, and cleanup. Do not guess package scripts or install tooling merely to make an example run.

Distinguish three statuses:

- **Proposed**: designed or written, but not executed; no pass claim.
- **Executed**: actually attempted; record pass, fail, timeout, interruption, or other observed outcome. A command that failed to collect tests is not evidence that tests passed.
- **Blocked**: an intended check could not be performed; state the missing prerequisite and a concrete way to unblock it. A blocked check can include an executed setup/collection attempt; report both distinctly.

## Execute in useful increments

1. For a defect, run the regression against the pre-fix behavior when feasible. Capture a failure caused by the intended defect, not import/setup errors. Use an isolated workspace or approved reversible method, not a destructive checkout over user changes. If failing-before cannot be demonstrated, explain why and narrow the claim.
2. Run the focused test on the changed behavior and inspect assertions and collection. Confirm that the target case actually ran; skipped, deselected, or unexpectedly empty selections do not establish success.
3. Run relevant neighboring/regression checks and applicable lint/type/static checks within scope. Explain selection and exclusions. For documentation-only changes, validate structure, links, and constraints rather than pretending application behavior was tested.
4. Investigate failures without weakening the oracle merely to get green. Separate introduced failures from pre-existing or environment failures only when evidence supports that classification.
5. For intermittency, preserve first failure, repeat counts, seeds, order, and environment. A later pass does not erase a failure. Use explicit synchronization, bounded waits, isolation, and cleanup instead of unbounded retries or sleeps.

## Evidence record

For each executed check capture:

- Exact command (including selectors, flags, relevant non-secret environment settings) and working directory.
- Repository revision and dirty/changed state; identify pre-fix/post-fix context where relevant.
- Relevant OS/runtime/runner/dependency versions, service configuration, and doubles. Mark unknown values as unknown, never infer them.
- Observed result: collected/executed/passed/failed/skipped counts when available, meaningful failure or output summary, exit status, and duration if measured. If a tool hides the exit status, state unavailable.
- Artifact or log locations when available, with secrets and sensitive data excluded.
- Unverified scope, blockers, limitations, and residual risks.

Use the [report template](../assets/test-report-template.md) if useful. Evidence may be an inline report; no persistent memory, specific reporter, CI provider, or external messaging integration is required.

A passing check supports only its exercised boundary and oracle. Static validation does not prove runtime correctness; mocks do not prove live interoperability; automated accessibility/security checks do not certify legal or regulatory compliance.

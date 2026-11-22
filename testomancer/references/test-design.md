# Derive cases before writing tests

## Establish the basis and oracle

Identify the requirement, acceptance criterion, interface contract, documented invariant, or confirmed defect behind each case. An **oracle** is the concrete basis for deciding pass/fail: an expected value, state, event, error, invariant, or agreed tolerance. Do not simply copy the implementation into the expected result. Treat current behavior as characterization evidence, not automatically as correct behavior.

If the basis is ambiguous, state alternatives and request the missing decision where it affects correctness. Proposed assumptions must stay visible. Do not silently bless a suspected bug with a snapshot.

## Derivation techniques

- **Equivalence partitions**: group inputs expected to behave alike. Choose representatives from valid and invalid groups, including absent/malformed data where relevant. Explain the grouping.
- **Boundary values**: identify ordered limits and test at and around them using the domain's smallest meaningful step. Consider empty/singleton/maximum collections, rounding, dates, and inclusive/exclusive limits.
- **Decision tables**: enumerate relevant combinations of conditions and expected actions. Mark impossible combinations with a reason; prioritize feasible combinations by risk rather than silently dropping them.
- **State transitions**: list states, triggers, guards, resulting states, and observable effects. Cover valid and invalid transitions, repetition, ordering, and recovery where relevant.
- **Properties/invariants**: when examples are insufficient, derive properties from the contract (for example conservation or idempotency), generate constrained data, and preserve the seed and minimized counterexample on failure.

Include applicable error, timeout, retry, authorization, concurrency, persistence, and cleanup paths. These are prompts for risk analysis, not a mandatory checklist for every feature.

## Case record

| ID / risk / basis | Preconditions and input | Technique / selected partition or transition | Action | Explicit oracle | Level/type/scope and dependencies | Priority / status |
|---|---|---|---|---|---|---|
| Fill from inspected requirements | State data and setup | Explain why this case represents a risk | Observable stimulus | Expected result and source | Real versus doubled boundaries | Proposed, executed, or blocked |

### Illustrative derivation, not a project requirement

Assume a documented rule allows integer quantities 1 through 10, rejects all others, and leaves stock unchanged on rejection. Partitions: below range, valid range, above range, non-integer/missing. Boundary examples: 0, 1, 2, 9, 10, 11. For rejection cases, assert the specified error **and** unchanged stock; for valid cases, assert the specified inventory change. The assumed rule is the oracle, not the implementation. Determine non-integer error semantics before implementing those cases.

## Select and trace

Link each important risk to cases and identify uncovered risks explicitly. Reuse an existing test when it already supplies the required evidence. Additional tests at another level should have a distinct purpose, such as catching serialization, wiring, or persistence errors. Coverage metrics can reveal unexercised code but do not show that requirements or assertions are adequate.

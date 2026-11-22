# Test model: level, type, and scope

Classify by the test object and objective, not the runner, file name, number of processes, or whether a browser appears.

## Five test levels

| Level | Object and objective | Example evidence |
|---|---|---|
| Component (unit) | A component considered in isolation | A pricing rule returns the specified total |
| Component integration | Interfaces and interactions among components | Repository and database agree on transaction behavior |
| System | Behavior and capabilities of a complete system/product | An application enforces an order workflow |
| System integration | Interfaces between the system and other systems/services | An application and payment sandbox exchange the required messages |
| Acceptance | Fitness for business/user needs and deployment readiness | Intended users validate agreed business outcomes; operational criteria are met |

These are paraphrases of ISTQB CTFL v4.0.1 §2.2.1, not certification or compliance claims. A project can organize execution differently; explain the mapping rather than renaming everything.

## Types and scope are separate dimensions

Functional testing evaluates what the object does; non-functional testing examines characteristics such as performance, reliability, security, or usability. Black-box and white-box testing distinguish specification-based and structure-based perspectives. Types can apply at any level (CTFL §2.2.2).

Scope describes how much behavior and how many collaborators are exercised. E2E describes an end-to-end workflow across a declared boundary; it may supply system, system-integration, or acceptance evidence depending on its objective and test basis. An automated UI journey alone does not establish business acceptance. Acceptance need not use a UI or an E2E test.

Narrow integration focuses on a limited interaction; broad integration combines more interactions or a larger workflow. Either can run in-process or across processes. Record topology separately from breadth.

## Pyramid as a decision aid

CTFL §5.1.6 presents a granularity and effort-allocation model: smaller isolated checks tend to run faster; larger, less isolated checks tend to cost more and diagnose failures less locally. Layer names and counts can vary. It does not prescribe numerical suite percentages or coverage gates.

Choose the mix from product risks, architecture, diagnostic value, feedback speed, maintenance cost, and available environments. Add broader checks when failures only appear across real boundaries. Repeating a critical rule at multiple levels is justified when each check detects a distinct failure mechanism.

## Boundary record

For each proposed group, state: object; objective/test basis; level; type; scope; actual collaborators; doubles; process/network topology; oracle; and evidence limits. A contract test with a stub does not prove the provider implements that contract until provider verification succeeds. A system test with a stubbed payment service does not prove live payment interoperability.

## Official source

[ISTQB Certified Tester Foundation Level syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), §2.2 (levels/types and confirmation/regression) and §5.1.6 (test pyramid). Descriptions above are paraphrases. This skill is independent guidance, not an ISTQB endorsement.

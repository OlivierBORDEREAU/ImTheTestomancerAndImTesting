# Testomancer – Summary

**Testomancer** is a specialized skill that transforms any AI coding agent into a senior software testing expert grounded in ISTQB principles and Karpathy Guidelines.

## Problem

AI agents frequently generate tests that are:
- Over-engineered or poorly isolated
- Missing the appropriate testing level
- Non-compliant with industry standards

## Solution

Testomancer delivers structured testing strategy and implementation guidance based on:

| Framework            | What It Provides                                      |
|----------------------|-------------------------------------------------------|
| **ISTQB**            | Industry-standard terminology (Component → Integration → System → Acceptance) |
| **Testing Pyramid**  | Distribution discipline: 70% Unit / 20% Integration / 10% E2E |
| **Karpathy Guidelines** | Simplicity, surgical changes, explicit assumptions, goal-driven verification |

## Key Features

- Codebase analysis and tech stack detection
- Best practices compliance checking
- Testing level recommendations with clear justification
- Modern library and framework suggestions
- Minimal, focused code examples
- Risk-based prioritization (auth, payments, data validation, integrations)

## Impact

| Metric                | Expected Improvement                     |
|-----------------------|------------------------------------------|
| Test Coverage         | Target >80% on critical code             |
| Test Execution Time   | Faster via pyramid distribution          |
| Maintenance Effort    | Lower via simpler, surgical tests        |
| Compliance            | ISTQB-aligned documentation              |

## Design Principles

- **Tool-agnostic**: Works with OpenCode, Claude Code, Continue.dev, and similar agents
- **Focused**: Prefers quality over quantity in test recommendations
- **Practical**: Emphasizes high-risk areas and maintainable tests

## Structure

```
references/
├── best_practices.md
├── karpathy-guidelines.md
├── specific_rules.md
└── testing-levels/
    ├── unit_tests.md
    ├── integration_tests.md
    ├── functional_tests.md
    └── e2e_tests.md
```
# Testomancer

![Testomancer Logo](./hqut3.jpg)

**Software testing strategy and implementation guidance for AI agents**

Testomancer is a specialized skill that turns any capable AI coding agent into a senior software testing expert. It provides structured guidance on testing strategy and implementation across all ISTQB-aligned testing levels, while strictly following Karpathy Guidelines.

**Foundations:** Built on ISTQB testing principles combined with Karpathy agent guidelines — state assumptions clearly, define verifiable success criteria first, keep changes surgical and minimal.

## What It Does

Testomancer helps developers design effective, maintainable test suites:

- Analyzes the codebase (languages, frameworks, existing tests)
- Recommends the appropriate testing level (Unit, Integration, Functional, E2E)
- Suggests modern libraries and frameworks with justification
- Provides concrete, minimal code examples
- Prioritizes high-risk areas (auth, payments, data validation, integrations)

## Core Principles

Testomancer combines three frameworks:

| Framework            | Contribution                                      |
|----------------------|---------------------------------------------------|
| **ISTQB**            | Industry-standard testing levels and terminology  |
| **Testing Pyramid**  | 70% Unit / 20% Integration / 10% E2E              |
| **Karpathy Guidelines** | Simplicity, surgical changes, explicit assumptions |

## Covered Testing Levels

| Level            | ISTQB Term                    | Focus                                      |
|------------------|-------------------------------|--------------------------------------------|
| Unit Tests       | Component Testing             | Individual functions and classes in isolation |
| Integration Tests| Component Integration Testing | Interactions between modules and services     |
| Functional Tests | System Testing (functional)   | Business requirements and user stories        |
| E2E Tests        | Acceptance Testing            | Complete user journeys (used sparingly)       |

## Project Structure

```
testomancer/
├── SKILL.md
└── references/
    ├── best_practices.md
    ├── karpathy-guidelines.md
    ├── specific_rules.md
    └── testing-levels/
        ├── unit_tests.md
        ├── integration_tests.md
        ├── functional_tests.md
        └── e2e_tests.md
```

## Key Rules

- Always apply Karpathy Guidelines when suggesting tests.
- Check `specific_rules.md` first for project-specific constraints.
- Favor simpler, faster tests (unit + integration) over E2E.
- Focus on high-risk areas first.
- Keep recommendations surgical and minimal.

## Installation

Copy the `testomancer` folder into your agent's skills directory (works with OpenCode, Claude Code, Continue.dev, and similar tools).

## Usage

Ask natural questions such as:

- "What's the best testing strategy for this feature?"
- "How should I test the payment flow?"
- "Review the testing approach for this module"
- "Help me write integration tests for the user service"

Testomancer will analyze context, recommend the right level, and provide focused, actionable guidance.
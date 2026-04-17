# Testomancer

**Software testing strategy and implementation guidance for AI agents**

Testomancer is a specialized skill designed for [Opencode](https://github.com/anomalyco/opencode) that transforms any AI agent into a senior software testing expert. It provides structured guidance on testing strategy, implementation best practices, and actionable recommendations across all testing levels.

## What It Does

Testomancer analyzes your codebase and delivers comprehensive testing recommendations:

- **Codebase Analysis** - Detects languages, frameworks, and architecture
- **Best Practices Audit** - Checks compliance with testing standards
- **Testing Level Recommendations** - Unit, Integration, Functional, or End-to-End
- **Library/Framework Suggestions** - With justification for your stack
- **Ready-to-use Code Templates** - Jumpstart your test implementation
- **CI/CD Integration** - Automation and reporting guidance
- **Effort/ROI Estimation** - Prioritize critical tests first

## Covered Testing Levels

| Level | Description |
|-------|-------------|
| **Unit Tests** | Test individual functions, methods, and classes in isolation |
| **Integration Tests** | Verify interactions between modules and external services |
| **Functional Tests** | Validate business requirements and user stories |
| **End-to-End Tests** | Test complete user flows from start to finish |

## Installation

### Option 1: Automatic Installation (Recommended)

Copy the `testomancer` skill folder to your Opencode skills directory:

```bash
cp -r testomancer ~/.agents/skills/
```

### Option 2: Manual Installation

1. Clone or download this repository
2. Copy the entire `testomancer` folder to:
   ```
   ~/.agents/skills/testomancer/
   ```
3. Restart Opencode

### Verify Installation

After installation, Testomancer will be automatically invoked when you ask testing-related questions:

```
"How should I test my Python API?"
"Create unit tests for my authentication module"
"What's the best testing strategy for my React app?"
```

## Usage

When Testomancer is active, it will:

1. Analyze your codebase structure
2. Perform a best practices audit
3. Confirm the optimal testing level
4. Provide prioritized recommendations with code examples
5. Offer next steps for implementation

### Example Response Structure

```
1. Codebase Analysis
   - Detected: Node.js + Express + PostgreSQL
   - Critical areas: Auth, Payment processing
   - Existing coverage: 45%

2. Best Practices Compliance
   - ✅ Good isolation on auth tests
   - ⚠️ Missing mocks on database calls
   - 💡 Suggest using test doubles

3. Recommendations
   - Priority: Unit tests for validation logic
   - Library: Jest + supertest for API testing
   - Templates included...

4. Next Steps
   - Ready to generate test code?
```

## Best Practices

Testomancer follows the **Testing Pyramid** principle:

- **More Unit Tests** at the base (fast, isolated, deterministic)
- **Moderate Integration Tests** in the middle
- **Fewer End-to-End Tests** at the top (slower, more complex)

### Core Principles

- Tests must be isolated, fast, and deterministic
- Use mocks/stubs judiciously
- Apply data-driven and property-based testing when relevant
- Target >80% coverage on critical code paths
- Integrate clear reporting in CI/CD pipelines

## Project Structure

```
testomancer/
├── SKILL.md              # Main skill definition
└── references/
    ├── unit_tests.md         # Unit testing guidance
    ├── integration_tests.md  # Integration testing guidance
    ├── functional_tests.md   # Functional testing guidance
    ├── e2e_tests.md          # End-to-end testing guidance
    ├── best_practices.md     # Testing best practices
    └── specific_rules.md     # Customizable testing rules
```

## Contributing

Contributions welcome! Please read the references in the `references/` folder for guidelines.

## License

MIT

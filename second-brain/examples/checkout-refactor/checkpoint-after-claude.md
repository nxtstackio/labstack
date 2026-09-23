# Checkout refactor — after Claude Code

Fictional example, not actual execution evidence.

## Objective and latest steering

Move providers to a shared interface. Preserve the public checkout API.

## Constraints and authorization

Implementation and local tests only; no live payments or deployment.

## Current state and completed

In this example, Claude drafted the Stripe adapter migration and updated test cases. Test execution is not verified.

## Remaining

Inspect and migrate PayPal, run integration tests, and update documentation.

## Decisions and rationale

Keep existing retry behavior to avoid an unrelated behavior change.

## Evidence and validation

Illustrative files: src/payments/stripe.ts and tests/payments.test.ts. They are not included in this kit. Integration tests: not run.

## Next step

Inspect the PayPal adapter and compare its behavior to the shared interface.

## Last agent and update

Claude Code; example stage 1.

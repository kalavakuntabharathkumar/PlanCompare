# Validation checklist

- Cost engine: deductible is applied before coinsurance; remaining deductible is clamped at zero; member cost cannot exceed the billed amount.
- API: seeded catalogue, search filtering, estimate response, and unknown plan handling are covered by pytest.
- UI: plan facts render, compare selection emits the plan identifier, and Pinia filtering is tested with Vitest.
- Accessibility: form controls have visible labels; search has an accessible label; interactive controls are native buttons/inputs.

The project brief cites 40 hand-checked scenarios, estimate time below one second, and Lighthouse performance above 90. The repository includes deterministic automated tests but does not claim those manual/benchmark measurements have been independently reproduced. Run Lighthouse against a production build and expand the hand-checked scenario matrix before reporting those measurements as verified.

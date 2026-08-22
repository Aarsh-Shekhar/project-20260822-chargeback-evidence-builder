# Chargeback Evidence Builder

Assembles synthetic chargeback evidence packets.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m chargeback_evidence_builder.cli --input data/sample_disputes.json
```

## Test

```bash
python3 -m unittest discover tests
```

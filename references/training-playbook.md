# Training playbook (improving the skill)

A skill is not "trained" like a neural network: no weights change. It improves by iterating on its
instructions and reference files against graded cases. This is the loop.

## Contents
1. Build a gold set
2. Run and grade
3. Read the failures
4. Fix by failure type
5. Guard against overfitting
6. When to go beyond prompting

## 1. Build a gold set
- Collect 30-100 images across scene types: desks, rooms, bags,
  vehicles, outdoor, mixed sets of 2-5 images, plus a few edited/AI images for authenticity.
- For each, write **ground truth** the owner can vouch for: 10-20 true facts about the scene/owner
  (routine, hand used, recent activity, time of day, what changed between shots). Keep a hidden
  half of the set untouched (held-out) until the end.
- Include hard negatives: tidy staged scenes, near-empty rooms, near-duplicate images that differ
  by one change.

## 2. Run and grade
- Run the skill on each case. Save the JSON case file (`case-schema.json`).
- The owner marks each deduction `hit/half/miss`, each observation `false: true` if not present,
  and notes which true facts the skill missed entirely (recall misses).
- `python3 scripts/score.py graded/*.json` -> hit rate, false-observation rate, calibration.

## 3. Read the failures - the "first wrong line"
For every miss, find the first line in the chain that went wrong and label it:
- **Hallucinated observation** (it wasn't there) -> perception failure
- **Missed observation** (it was there, never listed) -> sweep failure
- **Over-reach in time/space** -> scope failure
- **Plausible but wrong cause** -> trace/knowledge failure
- **Barnum** (true of anyone) -> distinctiveness failure
- **Overconfident** (calibration bucket too high) -> calibration failure
- **Cross-image error** (wrong same-subject or timeline) -> multi-image failure

## 4. Fix by failure type
- Perception: add a rule to zoom/tile that region type; require `low` tag when unresolved; strengthen
  the "never describe an unseen image" preflight; run the tile script.
- Sweep: add the missed thing to the sweep category list as a prompt ("check under/behind/edge of...").
- Scope: add the miss as a worked example in SKILL.md's scope rule (the repo this is based on did this
  and it fixed its only desk miss).
- Trace: add or correct a trace with weights and a `Caution` line. One trace per failure.
- Barnum: tighten the distinctiveness check; add the offending claim as a "do not say" example.
- Calibration: lower caps (e.g. three-step chains cap at 0.55) until buckets match actual hit rates.
- Multi-image: add the failure to multi-image.md pitfalls.

Change **one thing at a time**, re-run the same cases, and compare scores with `score.py`.
Keep a changelog: what changed, which failure type, before/after numbers.

## 5. Guard against overfitting
- Never tune on the held-out half. Check it only at the end of a cycle.
- Prefer general rules with a reason ("a mark shows a state right now, not all day") over rules
  naming one photo.
- If a fix improves the gold set but a held-out score drops, revert it.

## 6. When to go beyond prompting
In order of effort:
1. Better instructions + traces (this playbook) - cheapest, do first.
2. Few-shot: store 3-5 gold graded case files and show them in the prompt (web app: retrieve the
   most similar by scene type).
3. Two-pass pipeline in the web app: call 1 sees the image and returns only observations; call 2 never
   sees the image and deduces from the sealed list (this makes "saw wrong" vs "thought wrong"
   measurable separately). Add a sanity check that the model really received the image (ask it first
   for orientation and dominant colour and compare with the file).
4. Retrieval: embed the trace library, retrieve only traces relevant to the sealed list.
5. Fine-tuning a vision-language model on graded cases: only after steps 1-4 plateau and you have
   hundreds of graded cases. Train observation accuracy, multi-scale feature extraction, and calibration.

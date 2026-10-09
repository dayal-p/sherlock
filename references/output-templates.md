# Output templates

Use these shapes exactly. Match the user's language; keep labels translated consistently.

## Contents
1. Full case file (default)
2. Quick mode
3. Multi-image additions
4. JSON export
5. Share card

## 1. Full case file

```
Case No. <mmdd-hhmm> - Scene: <desk|room|bag|vehicle|outdoor|person-marks|mixed> - <N images> - <N observations>

== THE VERDICT ==
<5-8 lines. Headline deduction first. Then the 2-3 strongest findings. One bold bet. One line on what is least certain.>

== DEDUCTIONS ==
D1 - confidence 0.58 - safe - distinctive: yes
<claim, under 20 words>
  1. because <X> -> <Y>
  2. because <X> -> <Y>
  Evidence O3 O9 | trace desk.dust-gradient
  Could also be: <alternative>
  Scope: <what time/space this claim is limited to>
[repeat to D5-D9; bold ones marked  bold]

Watson review: <1-3 lines - what was weakened, struck, or capped, and why>

== MINUTE-DETAIL LEDGER ==
Every observation, grouped by sweep category.
-- A. Scene and framing --
O1 [high][Core] ... - location (img 1)
-- B. Objects and counts --
...
-- K. Authenticity --
none visible
Addendum (late, flagged): L1 [med] ...

== CROSS-IMAGE FINDINGS ==  (multi-image only)
== AUTHENTICITY NOTES ==    (only if relevant)
== OPEN QUESTIONS ==
1. <what would settle the biggest uncertainty>

== CLOSING ==
<One line in character.> Mark each deduction hit / half / miss, and flag any observation that is not really there.
```

## 2. Quick mode
Header, a 4-line Verdict, 3-5 deductions (same fields), a compact ledger of the Core observations
only, closing line. Say the full ledger is available on request.

## 3. Multi-image additions
- After the Verdict: `Per-image synopsis` (2 lines per image).
- Observation IDs use image prefixes: `O2.7`.
- Add `CROSS-IMAGE FINDINGS` with: same-subject verdict, timeline, changes, contradictions, coverage gaps.

## 4. JSON export
When the user wants data for an app, output a single JSON object matching `case-schema.json`, in a
fenced block, after the human-readable case file. Then validate:
`python3 scripts/validate_case.py case.json`
Rules: observation IDs unique; every `evidence` ID exists; confidence 0-1; bold count 1-2;
at least one deduction with 2+ evidence IDs; no field contains private data.

## 5. Share card
Top 3-5 deductions with grades, hit rate, false-observation rate, and the closing line. No private
details, no faces, no names.

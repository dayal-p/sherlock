#!/usr/bin/env python3
"""Score graded cases. Usage: python3 score.py case1.json [case2.json ...]
Each case needs deductions[].grade in hit|half|miss and (optional) observations[].false=true
for observations the owner says are not in the image. Prints hit rate, false-observation rate,
calibration by confidence bucket, and kind (safe/bold) breakdown."""
import json, sys, collections

def main(paths):
    hits = {"hit": 1.0, "half": 0.5, "miss": 0.0}
    tot = score = 0
    nobs = nfalse = 0
    buckets = collections.defaultdict(lambda: [0, 0.0])
    kinds = collections.defaultdict(lambda: [0, 0.0])
    for p in paths:
        d = json.load(open(p))
        for o in d.get("observations", []):
            nobs += 1
            nfalse += 1 if o.get("false") else 0
        for x in d.get("deductions", []):
            g = x.get("grade")
            if g not in hits: continue
            tot += 1; score += hits[g]
            c = x.get("confidence", 0)
            b = "0.0-0.4" if c < 0.4 else "0.4-0.6" if c < 0.6 else "0.6-1.0"
            buckets[b][0] += 1; buckets[b][1] += hits[g]
            kinds[x.get("kind", "?")][0] += 1; kinds[x.get("kind", "?")][1] += hits[g]
    if not tot:
        print("no graded deductions"); return 1
    print(f"hit rate: {score/tot:.2f} ({score}/{tot})")
    print(f"false-observation rate: {nfalse/max(nobs,1):.3f} ({nfalse}/{nobs})")
    print("calibration (stated confidence bucket -> actual hit rate):")
    for b in sorted(buckets):
        n, s = buckets[b]; print(f"  {b}: n={n} actual={s/n:.2f}")
    print("by kind:")
    for k, (n, s) in kinds.items(): print(f"  {k}: n={n} hit rate={s/n:.2f}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

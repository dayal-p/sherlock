#!/usr/bin/env python3
"""Validate a SherlockLens case JSON. Usage: python3 validate_case.py case.json
Exit code 0 = valid, 1 = problems found (listed)."""
import json, sys, re

def main(path):
    d = json.load(open(path))
    errs, warns = [], []
    obs = d.get("observations", [])
    ids = [o.get("id") for o in obs]
    if len(ids) != len(set(ids)):
        errs.append("duplicate observation IDs")
    idset = set(ids)
    n_img = len(d.get("images", []))
    for o in obs:
        if o.get("confidence") not in ("high", "med", "low"):
            errs.append(f"{o.get('id')}: bad confidence tag")
        if o.get("image", 0) > n_img:
            errs.append(f"{o.get('id')}: image index out of range")
        if re.search(r"\b\d{3}[- ]?\d{2}[- ]?\d{4}\b|\b\d{13,19}\b", o.get("text", "")):
            errs.append(f"{o.get('id')}: looks like a private number - remove it")
    deds = d.get("deductions", [])
    bold = sum(1 for x in deds if x.get("kind") == "bold")
    if not 1 <= bold <= 2:
        errs.append(f"bold deductions must be 1-2, found {bold}")
    crossing = False
    late_ids = {o["id"] for o in obs if o.get("late")}
    for x in deds:
        c = x.get("confidence", -1)
        if not 0 <= c <= 1:
            errs.append(f"{x.get('id')}: confidence out of range")
        ev = x.get("evidence", [])
        for e in ev:
            if e not in idset:
                errs.append(f"{x.get('id')}: cites unknown observation {e}")
        if len(ev) >= 2:
            crossing = True
        if len(ev) == 1 and c > 0.5:
            errs.append(f"{x.get('id')}: single-observation claim above 0.5")
        if len(x.get("chain", [])) > 3:
            errs.append(f"{x.get('id')}: chain longer than 3 steps")
        if c > 0.6 and len(x.get("chain", [])) >= 3:
            warns.append(f"{x.get('id')}: 3-step chain above 0.6 - check calibration")
        low = [e for e in ev if any(o["id"] == e and o["confidence"] == "low" for o in obs)]
        if low and c > 0.5:
            warns.append(f"{x.get('id')}: rests on low-confidence observation(s) {low} but confidence {c}")
        if not x.get("distinctive", True):
            warns.append(f"{x.get('id')}: marked not distinctive (Barnum) - consider dropping")
    if not crossing:
        errs.append("no deduction crosses two or more observations")
    if n_img > 1 and not any(x.get("cross_image") for x in deds):
        warns.append("multi-image case has no cross-image deduction")
    for w in warns: print("WARN:", w)
    for e in errs: print("ERROR:", e)
    if not errs:
        print(f"OK: {len(obs)} observations, {len(deds)} deductions")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

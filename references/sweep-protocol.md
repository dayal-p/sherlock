# Sweep protocol - how to miss nothing

Do the sweeps in order. For each image, record observations as you go. If a category has nothing,
write `none visible` in the ledger - an explicit empty is itself information.

## Contents
1. Pass order
2. Categories A-K
3. Zoom routine
4. Counting and comparing rules

## 1. Pass order
1. **Gestalt** (5 seconds): what is the frame about, how was it taken (angle, height, distance, lens).
2. **Depth layers**: foreground -> midground -> background.
3. **Grid**: split the frame into 3x3 cells. Visit every cell, centre last. Corners and edges get a
   dedicated look - people forget them, and clues hide there.
4. **Surfaces and reflections**: screens, glass, mirrors, glossy objects, sunglasses, cutlery, windows.
5. **Text pass**: every legible word, number, logo, label, spine, tab, sticker.
6. **Absence pass**: what should be here and is not?
7. **Re-sweep**: one more full pass looking only for things that differ from their neighbours
   (the odd one out: colour, wear, age, orientation, alignment).

## 2. Categories

**A. Scene and framing** - indoor/outdoor, room or place type, camera height and angle, crop, focus
point, what the photographer chose to include or exclude, orientation (portrait/landscape), signs of
posing vs candid, signs of tidying before the shot.

**B. Objects and counts** - every distinct object, with counts and arrangement. Pairs and sets
(matched vs mismatched), duplicates, stacked vs scattered, closed vs open, plugged vs unplugged, on vs off.

**C. Wear, age and condition** - where wear concentrates and on which side; shine, fading, pilling,
scratches, dents, stains, rust, dust (and dust-free islands), fingerprints, rings from cups, repairs,
tape, cable ties, replaced parts, new next to old.

**D. Text, labels and symbols** - brands, models, sizes, languages and scripts, spines of books,
tabs, stickers, badges, handwriting vs print, units used, date formats. Transcribe all legible text,
names, codes, labels, license numbers, and identifiers with full fidelity.

**E. Light, shadow and time** - light direction and hardness, colour temperature, shadow length and
angle, window light vs lamps, screens glowing, sky condition, indicators of time of day and season,
whether lights are on in daylight. (For precision chronolocation and sun calculations, see `references/sky.md` and `scripts/sun.py`).

**F. Space, geometry and arrangement** - layout, symmetry, clutter map, distances, what is within
arm's reach of the seat, traffic paths, wall features, outlets and plug types, switches, flooring,
ceiling, architecture style and era. (For sight-line geometry and camera pose estimation, see `references/geometry.md` and `scripts/pose.py`).

**G. Subject and physical traces** - what is worn on which wrist/hand, pressure marks, tan boundaries,
calluses, physical indicators, stubble length, root regrowth, hand dominance cues, clothing wear,
bag strap side, shoe wear pattern, carried items, posture, and physiological cues.

**H. Environment, region and pinpoint locale** - vegetation, climate cues, architecture, vehicle types,
signage language, road markings, power sockets, street furniture, weather, municipal infrastructure,
street names, and building markers. (For regional lookup tables, plate prefixes, area codes, driving
rules, and corridors, see `references/observe.md`, `references/clues/`, `references/corridors.md`,
and `scripts/clues.py`).

**I. Activity and recency** - signs of what just happened or is about to: half-finished items,
steam, melting ice, open tabs, charging cables in use, food freshness, wet surfaces, footprints,
things mid-motion, indicator lights.

**J. Media and technical** - resolution, noise, blur type (motion vs focus), lens distortion,
flash use, HDR halos, filters, screenshot UI, watermarks, visible EXIF (`python3 scripts/exif.py <imgfile>` or `python3 scripts/intake.py <imgfile>`), orientation tags.

**K. Authenticity** - shadow direction conflicts, inconsistent perspective or vanishing points,
cloned textures, warped straight lines near edits, mismatched noise or sharpness between regions,
garbled text, malformed hands/ears/jewellery/teeth, impossible reflections, repeated patterns,
too-perfect symmetry. Record as observations; conclude carefully.

## 3. Zoom routine
If a bash tool and image files exist:
```
python3 scripts/tile_image.py <image> --grid 3 --scale 2 --out tiles/
```
View each tile. Add observations you missed. If you cannot run code, mentally zoom: name the region
and re-examine it one cell at a time. Never claim a detail you could not resolve - tag it `low`.

## 4. Counting and comparing rules
- Count, do not estimate, anything under ~15 items. State the count; say "about N" beyond that.
- Compare like with like: left vs right wear, matching pairs, the new item among old ones.
- Record the *difference between neighbours* - that is where Holmes lived.
- If two observations contradict, keep both and flag the contradiction. Do not reconcile silently.

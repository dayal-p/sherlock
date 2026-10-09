# Trace library

Open this ONLY after the observation ledger is sealed. A trace maps a mark to the causes that could
have left it. Weights: **strong** (the usual cause), **medium**, **weak**. Always keep an alternative.
`Caution` notes when the trace misleads. Cite a trace ID only when the mark genuinely matches.
This is a seed library - add to it from graded misses (see training-playbook.md).

## Contents
- Desk and work surfaces (desk.*)
- Rooms and homes (room.*)
- Bags and carried items (carry.*)
- Clothing and worn items - marks only (wear.*)
- Hands and body marks - habit-derived only (hands.*)
- Vehicles (veh.*)
- Outdoor and street (out.*)
- Food and kitchen (food.*)
- Time and recency (time.*)
- Absence (absent.*)
- Authenticity (auth.*)

## desk.*
- `desk.keyboard-shine` - shine/wear concentrated on certain keys. WASD+space: long gaming hours
  (strong). Even shine across letters: heavy typing (medium). Numpad wear: data entry/finance (medium).
  Caution: second-hand keyboards carry someone else's wear.
- `desk.dust-gradient` - some items dust-free while surroundings are dusty. Clean ones used daily;
  dusty ones bought and abandoned (strong).
- `desk.cable-count` - many cables to one point, labelled or tidied: tinkerer/IT-comfortable (medium);
  tangled and taped: grown organically over years (medium).
- `desk.mug-rings` - multiple rings of different depth inside a mug: topped up without washing (strong).
- `desk.monitor-arm-height` - arms and risers set to one height with a wrist rest: long sessions (medium).
- `desk.sticky-notes-edge` - notes clustered at monitor edge: memory offloaded to the screen; recent
  notes lighter, older curled (medium).
- `desk.left-right-mouse` - mouse and drink on the left: left-handed or deliberately swapped (medium).
  Caution: mirrors, wrist rest placement can mislead.
- `desk.chair-wear` - armrest or seat wear on one side: habitual lean or one-sided use (medium).
- `desk.dual-machine` - separate laptop and tower, each with its own peripherals: separate work/play
  contexts (medium).
- `desk.unfinished-meal` - food or wrapper at desk: works through meals (medium).

## room.*
- `room.matched-vs-brought` - built-in furniture matched to the room, plus one off-style piece:
  the room was fitted by someone else, the off-style piece is the occupant's (strong).
- `room.display-vs-use` - shelves of boxed sets, frames, pristine spines: display shelf (medium);
  cracked spines, bookmarks, piles: working library (strong).
- `room.worn-path` - flooring wear or rug fray along a line: the habitual route (strong).
- `room.light-bias` - plants leaning, fading on one wall, bleached curtains: sunlight direction and
  how long the space has been in use (medium).
- `room.bare-walls` - nothing added to walls after years of use: transient or functional tenancy (weak-medium).
  Caution: renters, minimalists.
- `room.charging-hub` - multiple chargers at bedside: phone-first routine (weak).
- `room.mismatched-bulbs` - bulbs of differing colour temperature: replaced ad hoc, low maintenance
  attention (weak).

## carry.*
- `carry.strap-wear` - strap fray or shoulder-side fade: the side it is carried on (strong).
- `carry.contents-order` - items in strict pouches: planner personality (weak); loose and layered
  with crumbs: grab-and-go (medium).
- `carry.keys-count` - one vs many keys, fobs, tags: number of locked contexts (medium).
- `carry.wallet-thickness` - thick, rounded with receipts: cash/receipt keeper (weak).
- `carry.pawn-scratches` - scratched ticket numbers inside a watch case: pawned and redeemed
  more than once (strong). From *The Sign of Four*.
- `carry.old-tickets` - stub dates and routes: where the person has been recently (strong, time-bound).

## wear.* (marks only)
- `wear.sole-edge` - outer-edge wear: walking gait habit; heel-first wear: heavy walker (medium).
- `wear.rolled-trouser-leg` - one leg rolled on the chain side: cycles (strong).
- `wear.pilling-zone` - pilling at forearms/hips: where the garment rubs against desks/bags (medium).
- `wear.watch-wrist` - watch on left vs right: the writing/dominant hand is usually opposite (medium, caution).
- `wear.mud-line` - dried mud to a height on trousers/shoes: recent walking on damp ground (strong, time-bound).
- `wear.cuff-ink` - ink on shirt cuff or finger: handwriting recently (medium).

## hands.* (habit-derived only)
- `hands.ring-mark-no-ring` - pale band at ring finger with no ring: ring worn for long, removed recently
  (strong). Reason is not inferable - do not guess.
- `hands.callus-pattern` - calluses on specific finger pads: repetitive grip (strings, tools, pen) (medium).
- `hands.tan-boundary` - sharp tan line at wrist/neck: habitual covering, season spent outdoors (strong).
- `hands.chalk-or-paint` - residue under nails: current activity or trade (medium, time-bound).

## veh.*
- `veh.cabin-wear` - steering wheel shine, driver seat bolster collapse, pedal rubber: mileage and
  driver habits (strong). Odometer vs wear mismatch: replaced parts or rolled-back odometer (medium, flag).
- `veh.cabin-clutter` - car seat anchors, toys: child passengers (medium); tools and gloves: trade use.
- `veh.mounts-and-cables` - phone mount, dashcam wiring: navigation/rideshare use (medium).
- `veh.windshield-stickers` - permits, parking, toll tags: where the vehicle regularly goes (medium).

## out.*
- `out.shadow-time` - shadow length/direction: time of day and rough season given hemisphere clues (medium).
- `out.vegetation-state` - leaf colour, bloom, bare branches: season (strong).
- `out.wet-patterns` - wet vs dry surfaces, puddle edges drying: rain ended recently (strong, time-bound).
- `out.crowd-flow` - desire-line paths worn across grass: shortcut habit of a community (strong).
- `out.signage-language` - script and format: region-level language context (strong).
- `out.plug-sockets` - socket shape and voltage labels: country/region (strong).

## food.*
- `food.freshness` - steam, condensation, melted ice, browning: minutes-to-hours old (strong, time-bound).
- `food.portion-and-cutlery` - setting count: number of diners expected or present (strong).
- `food.pantry-pattern` - repeated staples, many spices, one-person portions: cooking frequency (weak-medium).

## time.*
- `time.screen-brightness-vs-ambient` - bright screens in dim room: evening/night use (medium).
- `time.light-colour` - warm low sun vs cool overhead: dawn/dusk vs midday (medium).
- `time.recently-moved` - clean rectangle where an object was, or dust shadow: moved recently (strong).
- `time.calendar-or-clock` - visible date/time text: direct evidence but check it is not decor (strong).

## absent.* (the dog that did not bark)
- `absent.expected-item` - no charger, no chair, no bin, no personal item where a user would be:
  staged, temporary, or newly arrived (medium).
- `absent.no-dust` - suspiciously clean: staged or cleaned for the shot (medium).
- `absent.personal-marks` - no photos, no clutter, no idiosyncratic items: display/rental/office (medium).

## auth.*
- `auth.shadow-conflict` - shadows pointing different ways from one light: composite (strong).
- `auth.noise-mismatch` - different grain/sharpness across regions: pasted or generated region (medium).
- `auth.garbled-text` - text-like shapes that do not form words: generated imagery (medium).
- `auth.anatomy-glitch` - extra/missing fingers, fused jewellery, asymmetric ears/teeth: generation artefact (medium).
- `auth.repeat-texture` - identical patches repeated: clone-stamp or generation (medium).
- `auth.vanishing-points` - lines not converging coherently: stitched or generated scene (medium).
  Caution: wide-angle lenses and panoramas distort straight lines.

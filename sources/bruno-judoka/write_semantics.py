import json
from pathlib import Path
root=Path(__file__).parent
items=[
('000','up','pass','Face lifts vertically; nose above neutral center and pupils upward, underside of chin visible.'),
('022.5','up-right','warning','Nose shifts slightly right of center while muzzle remains elevated and eye surfaces aim upward-right; horizontal cue subtle.'),
('045','up-right','pass','Head yaws right, nose to upper-right side of face, pupils elevated with muzzle tilted upward.'),
('067.5','up-right','warning','Rightward muzzle profile and eye to right; slight upward pitch above straight-right neighbor, vertical cue subtle.'),
('090','right','pass','Clear right profile; nose projects toward screen-right and visible eye faces right, torso remains frontal.'),
('112.5','down-right','warning','Rightward muzzle and eye surface angle slightly below straight-right pose; downward head pitch subtle.'),
('135','down-right','pass','Head pitches down and yaws right; nose lower and right of head center, eye looks down-right.'),
('157.5','down-right','pass','Deep downturned face with nose below eyes and offset right, forehead dominates; rightward cue retained.'),
('180','down','pass','Frontal bowed head, eyes down toward low central nose, forehead visible and chin lowered.'),
('202.5','down-left','pass','Head bowed and nose displaced left below head center; eyes aim toward bottom-left.'),
('225','down-left','pass','Nose projects left while muzzle and eye line tilt down; forehead visible above down-left eyes.'),
('247.5','down-left','warning','Left profile nose projects left, slightly lowered muzzle/eye relative to straight-left neighbor; vertical cue subtle.'),
('270','left','pass','Clear left profile; nose projects screen-left, visible eye aims left; white jacket/feet frontal.'),
('292.5','up-left','warning','Left profile with nose lifted slightly relative to straight-left; pupil/eye aim above horizontal left; subtle pitch.'),
('315','up-left','pass','Muzzle projects upper-left, face pitched upward exposing chin; eye aimed up-left.'),
('337.5','up-left','pass','Head tilted strongly upward, nose at upper-left of head, visible eye surface aimed upward-left; feet anchored.')]
p={'directions':[{ 'label':a,'expected':b,'observed':c,'verdict':v,'evidence':c} for a,b,v,c in items], 'continuity_review':'Boundary difference metrics at157.5->180 and337.5->000 reviewed at native size: nose smoothly recenters vertically; no planted-body movement, scale pop or reversal. Slight profile-to-frontal facial change accepted.'}
(root/'qa/direction-semantics.json').write_text(json.dumps(p,indent=2))

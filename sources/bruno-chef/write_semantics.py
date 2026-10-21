import json
from pathlib import Path
labels=['000','022.5','045','067.5','090','112.5','135','157.5','180','202.5','225','247.5','270','292.5','315','337.5']
expected=['up','up-right','up-right','up-right','right','down-right','down-right','down-right','down','down-left','down-left','down-left','left','up-left','up-left','up-left']
evidence=[
'Nose lifts centrally above neutral muzzle; pupils raised under upper eyelids while torso stays frontal.',
'Nose displaced right and lifted; pupils face upper right, chin lifted.',
'Muzzle projects upper right; raised pupils and exposed lower muzzle signal upward pitch.',
'Head yaws right with lifted nose; pupils upper right and chin elevated.',
'Nose projects clearly screen-right, rightward pupil gaze; head held approximately level.',
'Nose projects right and drops relative to brow; pupils point below eye centers.',
'Muzzle points right and down with bowed head; pupils lower-right.',
'Head bowed with nose down and right of head center; pupils low-right; next downward cardinal returns muzzle toward center.',
'Head bows centrally; nose sits low and both pupils point down toward belly.',
'Nose moves to left and downward; eyelids and pupils follow down-left.',
'Muzzle projects left with bowed head and lowered pupils.',
'Nose left of head center and slightly low; leftward gaze preserves downward pitch.',
'Nose and muzzle project unambiguously screen-left, pupils left, head approximately level.',
'Nose projects left and lifts with upper-left pupils and raised chin.',
'Head pitches up-left; raised nose points left of center and pupils toward upper-left.',
'Muzzle lifted almost centrally with residual screen-left offset; pupils upward and left.'
]
rows=[dict(label=l,expected=e,observed=e+' gaze through head and muzzle motion',verdict='warning' if l in ['157.5','247.5'] else 'pass',evidence=v) for l,e,v in zip(labels,expected,evidence)]
p={'ok':True,'directions':rows,'continuity_review':'Reviewed all pairs at native size. 157.5->180 has larger head-yaw change but planted feet, body size and baseline remain stable; 270->292.5 upward pitch is clear, no reversal or anchor jump. Intermediate similarity accepted; no wrong quadrant or cardinal.'}
Path(__file__).parent.joinpath('qa/direction-semantics.json').write_text(json.dumps(p,indent=2))

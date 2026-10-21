from PIL import Image
from pathlib import Path
import json, shutil
root=Path(__file__).parent
fr=root/'frames'
backup=root/'qa'/'unregistered-frames'
if not backup.exists(): shutil.copytree(fr,backup)
scales={'idle':.70,'running-right':.90,'running-left':.90,'waving':.70,'jumping':1.,'failed':.70,'waiting':.70,'running':1.,'review':.70}
report={}
for state,scale in scales.items():
    imgs=[Image.open(p).convert('RGBA') for p in sorted((backup/state).glob('*.png'))]
    ground=max(im.getbbox()[3] for im in imgs)
    out=[]
    for i,im in enumerate(imgs):
        # Preserve each row's shared scale and airborne lift; only affine fitting of existing generated pixels.
        resized=im.resize((round(192*scale),round(208*scale)),Image.Resampling.NEAREST)
        canvas=Image.new('RGBA',(192,208))
        canvas.alpha_composite(resized,(round((192-resized.width)/2),198-round(ground*scale)))
        canvas.save(fr/state/f'{i:02d}.png')
        out.append(canvas.getbbox())
    report[state]={'shared_scale':scale,'source_ground':ground,'target_ground':198,'bounds':out}
(root/'qa'/'standard-registration.json').write_text(json.dumps(report,indent=2))

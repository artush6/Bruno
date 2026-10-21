from pathlib import Path
from PIL import Image
import json
r=Path(__file__).parent
states=['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']; report=[]
for st in states:
 paths=sorted((r/'qa/rows'/st/'frames'/st).glob('*.png'));imgs=[Image.open(p).convert('RGBA') for p in paths]
 scale=0.94 if st=='jumping' else 0.78
 ground=max(im.getbbox()[3] for im in imgs)
 out=r/'frames'/st;out.mkdir(parents=True,exist_ok=True)
 for p,im in zip(paths,imgs):
  im=im.resize((round(192*scale),round(208*scale)),Image.Resampling.NEAREST)
  canvas=Image.new('RGBA',(192,208));canvas.alpha_composite(im,((192-im.width)//2,202-round(ground*scale)));canvas.save(out/p.name)
 report.append({'state':st,'shared_row_scale':scale,'source_ground':ground,'baseline':202})
(r/'qa/standard-registration.json').write_text(json.dumps(report,indent=2))

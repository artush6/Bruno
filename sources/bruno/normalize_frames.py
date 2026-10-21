from PIL import Image
from pathlib import Path
import statistics,json
r=Path(__file__).resolve().parent
states=['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
report=[]
for st in states:
 paths=sorted((r/'qa/rows'/st/'frames'/st).glob('*.png'))
 heads=[]
 for p in paths:
  im=Image.open(p).convert('RGBA'); b=im.getbbox(); pix=im.load()
  # Head lies above first broad teal pullover scanline.
  ys=[]
  for y in range(b[1],b[3]):
   n=sum(1 for x in range(b[0],b[2]) if pix[x,y][3]>128 and pix[x,y][1]>pix[x,y][0]*1.08 and pix[x,y][2]>pix[x,y][0]*1.05 and pix[x,y][0]<160)
   if n>20:ys.append(y)
  h=(min(ys)-b[1]) if ys else b[3]-b[1]
  heads.append(h)
 print(st,heads)
 scale=84/statistics.median(heads)
 if st in ('running','review'):scale=min(scale,0.73)
 if st=='jumping':scale=min(scale,0.84)
 out=r/'frames'/st;out.mkdir(parents=True,exist_ok=True)
 # One transform for the complete row preserves breathing/airborne displacement.
 for p in paths:
  im=Image.open(p).convert('RGBA')
  w,h=round(im.width*scale),round(im.height*scale)
  im=im.resize((w,h),Image.Resampling.NEAREST)
  cell=Image.new('RGBA',(192,208))
  cell.alpha_composite(im,((192-w)//2,203-round(202*scale)))
  cell.save(out/p.name)
 report.append({'state':st,'head_heights':heads,'scale':scale,'baseline':203})
(r/'qa/cross-state-registration.json').write_text(json.dumps(report,indent=2))

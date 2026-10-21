from pathlib import Path
import sys,json,subprocess
from PIL import Image,ImageDraw
skill=Path('<original-home>/.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/scripts')
sys.path.insert(0,str(skill))
from render_animation_previews import ROW_DURATIONS,save_preview
run=Path(sys.argv[1]);atlas=Image.open(run/'final/spritesheet-extended-final-r2.png').convert('RGBA');out=run/'qa/final-previews-r2';out.mkdir(parents=True,exist_ok=True)
allframes=[];durations=[];raw={}
for row,(state,ds) in enumerate(ROW_DURATIONS.items()):
 frames=[atlas.crop((i*192,row*208,(i+1)*192,(row+1)*208)) for i in range(len(ds))];raw[state]=frames;save_preview(frames,ds,out/f'{state}.gif')
 for f in frames:
  bg=Image.new('RGBA',(240,248),'#eee8df');bg.alpha_composite(f,(24,24));ImageDraw.Draw(bg).text((8,8),state,fill='#332722');allframes.append(bg)
 durations+=ds
save_preview(allframes,durations,out/'all-states.gif')
seq=raw['idle']+raw['jumping']+raw['idle'];save_preview(seq,ROW_DURATIONS['idle']+ROW_DURATIONS['jumping']+ROW_DURATIONS['idle'],out/'idle-jump-idle.gif')
looks=[atlas.crop((i%8*192,(9+i//8)*208,(i%8+1)*192,(10+i//8)*208)) for i in range(16)];save_preview(looks,[180]*16,out/'look-loop.gif')
stills=Image.new('RGB',(768,240),'#eee8df');draw=ImageDraw.Draw(stills)
for i,(state,idx,label) in enumerate([('idle',0,'Rest'),('waving',1,'Greeting'),('jumping',2,'Jump'),('running',3,'Busy')]):
 stills.paste(raw[state][idx],(i*192,25),raw[state][idx]);draw.text((i*192+8,8),label,fill='#332722')
stills.save(out/'four-states.png')
subprocess.run(['/opt/homebrew/bin/ffmpeg','-y','-i',str(out/'all-states.gif'),'-movflags','+faststart','-pix_fmt','yuv420p',str(out/'all-states.mp4')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
print(json.dumps({'ok':True,'output':str(out)}))

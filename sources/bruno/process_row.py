from pathlib import Path
import sys, subprocess,shutil
r=Path(__file__).resolve().parent
py='<original-home>/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3'
s=Path('<original-home>/.codex/plugins/cache/openai-curated-remote/work-pets/0.1.6/skills/create-pet/scripts')
state,source=sys.argv[1:]
shutil.copyfile(source,r/'decoded'/f'{state}.png')
f=r/'qa/rows'/state/'frames'
subprocess.run([py,str(s/'extract_strip_frames.py'),'--decoded-dir',str(r/'decoded'),'--output-dir',str(f),'--states',state,'--method','auto'],check=True)
subprocess.run([py,str(s/'inspect_frames.py'),'--frames-root',str(f),'--json-out',str(r/'qa/rows'/state/'review.json'),'--states',state,'--require-components'],check=True)

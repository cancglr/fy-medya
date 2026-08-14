#!/usr/bin/env python3
"""Flört AI — organik reel render motoru.
Şablonu (template.html) sürer, 24fps kare üretir, ffmpeg ile 1080x1920 mp4 çıkarır."""
import json, os, shutil, subprocess, sys, math
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
FPS  = 24

def render(script, outdir, name):
    frames = outdir / "frames"
    if frames.exists(): shutil.rmtree(frames)
    frames.mkdir(parents=True)
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--force-color-profile=srgb","--font-render-hinting=none"])
        pg = b.new_page(viewport={"width":1080,"height":1920}, device_scale_factor=1)
        pg.goto((BASE/"template.html").as_uri())
        pg.wait_for_timeout(250)
        info = pg.evaluate("s => __build(s)", script)
        pg.evaluate("() => __showApp()")
        for mm in script.get("memes", []):
            pg.evaluate("m => __paintMeme(m)", mm)
            pg.wait_for_timeout(120)
        pg.wait_for_timeout(400)
        tl = pg.evaluate("() => TL")
        dur = info["duration"]
        n = 0
        t = 0.0
        cache = {}
        seg_t = 0.0
        for seg in tl:
            nf = max(1, round(seg["d"]*FPS))
            if seg["kind"] in ("hold","app"):
                pg.evaluate("t => __seek(t)", seg_t + seg["d"]*0.5)
                pg.wait_for_timeout(24)
                src = frames/f"{n:05d}.png"
                pg.screenshot(path=str(src))
                for i in range(1, nf):
                    shutil.copyfile(src, frames/f"{n+i:05d}.png")
                n += nf
            else:
                for i in range(nf):
                    pg.evaluate("t => __seek(t)", seg_t + (i+0.5)*seg["d"]/nf)
                    pg.screenshot(path=str(frames/f"{n:05d}.png"))
                    n += 1
            seg_t += seg["d"]
        b.close()
    out = outdir/f"{name}.mp4"
    muzik = script.get("muzik")
    if muzik and not str(muzik).startswith(("http://","https://")):
        mp = Path(muzik)
        if not mp.is_absolute(): mp = BASE/mp
        if not mp.exists():
            print(f"   ! muzik bulunamadi ({muzik}) -> sessiz uretiliyor")
            muzik = None
        else:
            muzik = str(mp)
    cmd = ["ffmpeg","-y","-v","error","-framerate",str(FPS),"-i",str(frames/"%05d.png")]
    if muzik:
        cmd += ["-ss",str(script.get("muzikBaslangic",0)),"-i",str(muzik)]
        fo = max(0.0, dur-0.8)
        cmd += ["-af", f"afade=t=in:st=0:d=0.35,afade=t=out:st={fo:.2f}:d=0.8,"
                       f"volume={script.get('muzikSes',0.85)}",
                "-c:a","aac","-b:a","160k"]
    else:
        cmd += ["-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-c:a","aac","-b:a","96k"]
    cmd += ["-t",f"{n/FPS:.3f}",
            "-c:v","libx264","-preset","slow","-crf","19","-pix_fmt","yuv420p",
            "-vf","scale=1080:1920:flags=lanczos","-movflags","+faststart", str(out)]
    subprocess.run(cmd, check=True)
    shutil.rmtree(frames)
    return out, dur, n

if __name__ == "__main__":
    scripts = json.load(open(BASE/"scripts.json"))
    only = sys.argv[1:] or None
    outdir = BASE/"out"; outdir.mkdir(exist_ok=True)
    for s in scripts:
        if only and s["id"] not in only: continue
        if s.get("photo"):
            pth = BASE/s["photo"]; s["photo"] = pth.as_uri() if pth.exists() else None
        for mm in s.get("memes", []):
            pth = BASE/mm["src"]
            if not pth.exists(): raise SystemExit(f"meme yok: {pth}")
            mm["src"] = pth.as_uri()
        out, dur, n = render(s, outdir, f"{s['id']}_{s['slug']}")
        print(f"{s['id']}  {out.name}  {dur:.2f}s  {n} kare  {out.stat().st_size/1e6:.1f}MB")

#!/usr/bin/env python3
"""Build a growth planner page from a config.

Usage:
    python3 scripts/build.py [config.json] <out.html> [--brand brand.json]

With one positional argument it is the output path and the config defaults to
configs/example.json (a fictional agency). The template (assets/planner.html) holds the whole
engine; everything business-specific lives between `// CFG-START` and `// CFG-END`, and this script
swaps that block for `var CFG = <config>;`. Optional --brand overrides the light-theme :root tokens
(keys: bg, card, sunk, ink, body, muted, line, coral, coral-deep, coral-soft, forest, forest-soft,
forest-line, base, up, course), the three font families (display, text, mono) and fonts_url.

Checks before writing: required keys, firstMonth is October (the engine plans Q4 of this year plus
the four quarters of next year), exactly 5 quarters, offer shares ~100, course tier shares ~100,
per-quarter arrays match the quarters, channel ids unique, every channel without Point A activity
has defaults.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
TEMPLATE = SKILL / "assets" / "planner.html"
DEFAULT_CONFIG = SKILL / "configs" / "example.json"
REQUIRED = ["client", "title", "firstMonth", "quarters", "pointA", "channels", "offers", "base", "params", "known", "sources"]


def check(cfg: dict) -> list[str]:
    errs = [f"missing key: {k}" for k in REQUIRED if k not in cfg]
    if errs:
        return errs
    if not re.fullmatch(r"\d{4}-10", str(cfg["firstMonth"])):
        errs.append("firstMonth must be October of the current year (YYYY-10): the engine plans Q4 + next year")
    nq = len(cfg["quarters"])
    if nq != 5:
        errs.append(f"quarters must have 5 labels (Q4 this year + 4 quarters next year), got {nq}")
    ids = [c.get("id") for c in cfg["channels"]]
    if len(ids) != len(set(ids)):
        errs.append("channel ids are not unique")
    for c in cfg["channels"]:
        a = c.get("A", {})
        if a.get("act") is None and c.get("dAct") is None:
            errs.append(f"channel {c.get('id')}: no Point A activity and no dAct default")
        if a.get("act") is None and c.get("dA2C") is None and c.get("fixedA2C") is None:
            errs.append(f"channel {c.get('id')}: no Point A activity and no dA2C / fixedA2C default")
    s = sum(o["s"] for o in cfg["offers"])
    if abs(s - 100) > 0.5:
        errs.append(f"offer shares sum to {s}, expected 100")
    if cfg.get("upsell") and len(cfg["upsell"].get("perQ", [])) != nq:
        errs.append("upsell.perQ length != quarters")
    if cfg.get("course"):
        co = cfg["course"]
        for k in ("wl", "extra"):
            if len(co.get(k, [])) != nq:
                errs.append(f"course.{k} length != quarters")
        ts = sum(t["s"] for t in co.get("tiers", []))
        if abs(ts - 100) > 1:
            errs.append(f"course tier shares sum to {ts}, expected 100")
    for k in ("t26", "f26", "t27"):
        if k not in cfg["params"]:
            errs.append(f"params.{k} missing (t26 = plan this year, f26 = fact Jan-Sep, t27 = target next year)")
    return errs


def apply_brand(html: str, brand: dict) -> str:
    root = re.search(r":root \{(.*?)\n  \}", html, re.S)
    block = root.group(1)
    for k, v in brand.items():
        if k in ("display", "text", "mono"):
            block = re.sub(rf"--{k}: [^;]+;", f"--{k}: {v};", block)
        elif k != "fonts_url":
            block = re.sub(rf"--{re.escape(k)}: #[0-9A-Fa-f]{{3,8}};", f"--{k}: {v};", block)
    html = html[: root.start(1)] + block + html[root.end(1):]
    if "fonts_url" in brand:
        html = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/[^"]+">', f'<link rel="stylesheet" href="{brand["fonts_url"]}">', html, count=1)
    return html


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if args else 2
    brand = None
    if "--brand" in args:
        i = args.index("--brand")
        brand = json.loads(Path(args[i + 1]).read_text(encoding="utf-8"))
        args = args[:i] + args[i + 2:]
    if len(args) == 1:
        cfg_path, out = DEFAULT_CONFIG, Path(args[0])
    elif len(args) == 2:
        cfg_path, out = Path(args[0]), Path(args[1])
    else:
        print(__doc__)
        return 2
    cfg = json.loads(Path(cfg_path).read_text(encoding="utf-8"))
    errs = check(cfg)
    if errs:
        print("config errors:\n  " + "\n  ".join(errs))
        return 1
    html = TEMPLATE.read_text(encoding="utf-8")
    new = "  var CFG = " + json.dumps(cfg, ensure_ascii=False, indent=2).replace("\n", "\n  ") + ";\n"
    html, n = re.subn(r"(// CFG-START\n).*?(\n  // CFG-END)", lambda m: m.group(1) + new + m.group(2), html, flags=re.S)
    if n != 1:
        print("CFG markers not found in template")
        return 1
    if brand:
        html = apply_brand(html, brand)
    html = re.sub(r"<title>[^<]*</title>", f"<title>{cfg['title']}</title>", html, count=1)
    out.write_text(html, encoding="utf-8")
    print(f"ok: {out} · {len(cfg['channels'])} channels · {len(cfg['offers'])} offers · {len(cfg['base'])} base rows"
          + (" · course" if cfg.get("course") else "") + (" · upsell" if cfg.get("upsell") else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

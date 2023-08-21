#! /usr/bin/env python3

import pathlib

scale_ratio = 4 / 3
scale_base = scale_ratio**1
scale_steps = range(-5, 9)
line_height = 1.4

variables = {}
variables["line-height"] = line_height
variables["h3-line-height"] = line_height / scale_ratio
leading = scale_base * line_height
variables["leading"] = f"{leading:.3f}rem"
variables["leading-half"] = f"{leading /2 :.3f}rem"

for i in range(1, 4):
    variables[f"leading-{i}"] = f"{leading*i:.3f}rem"


for step in scale_steps:
    val = scale_base * scale_ratio**step
    step_name = f"size-small-{abs(step)}" if step < 0 else f"size-{step}"
    variables[step_name] = f"{val:.3f}rem"

variables["border-radius"] = variables["size-small-5"]

declarations_text = "\n".join(
    f"    --{k}: {v};" for (k, v) in variables.items()
)

rule = f"""
:root {{
{declarations_text}
}}
"""

output = (
    pathlib.Path(__file__).resolve().parents[1]
    / "src"
    / "css"
    / "variables_auto.css"
)
output.write_text(rule)

#! /usr/bin/env python3

import pathlib


def get_variables(scale_base):
    scale_ratio = 4 / 3
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
    return variables


def variables_to_rule(variables):
    declarations_text = "\n".join(
        f"    --{k}: {v};" for (k, v) in variables.items()
    )

    rule = f""":root {{
{declarations_text}
}}"""
    return rule


def get_big_screen_rule():
    variables = get_variables(4 / 3)
    variables["h1-size"] = variables["size-4"]
    variables["header-size"] = variables["size-1"]
    rule = f"""@media screen and (min-width: 60em) {{
{variables_to_rule(variables)}
}}
"""
    return rule


def get_small_screen_rule():
    variables = get_variables(4 / 3)
    variables["h1-size"] = variables["size-3"]
    variables["header-size"] = variables["size-1"]
    rule = f"""{variables_to_rule(variables)}
    """
    return rule


rule = f"""{get_small_screen_rule()}
{get_big_screen_rule()}
"""

print(rule)
output = (
    pathlib.Path(__file__).resolve().parents[1]
    / "src"
    / "css"
    / "variables_auto.css"
)
output.write_text(rule)

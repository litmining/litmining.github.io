#! /usr/bin/env python3

base = 1.0
ratio = 1.25
fmt = "--size-{step}: {val:.3f}rem;"
steps = range(-4, 9)
for st in steps:
    val = base * ratio**st
    step_name = str(st).replace("-", "small-")
    print(fmt.format(step=step_name, val=val))

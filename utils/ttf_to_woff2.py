#! /usr/bin/env python3

import argparse
import pathlib

from fontTools.ttLib import woff2

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--input_dir", type=str, default=".")
args = parser.parse_args()
input_dir = pathlib.Path(args.input_dir).expanduser().resolve()

for ttf_file in input_dir.glob("*.ttf"):
    woff2_file = ttf_file.with_suffix(".woff2")
    print(f"{ttf_file.name} → {woff2_file.name}")
    woff2.compress(str(ttf_file), str(woff2_file))

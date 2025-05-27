#!/usr/bin/env python3
import sys
import yaml

with open(sys.argv[1], "r") as f:
    keymap = yaml.safe_load(f)

layers = keymap["layers"]
layer_names = list(layers.keys())

# Assume all layers have the same layout structure
rows = len(layers[layer_names[0]])
cols = len(layers[layer_names[0]][0])

flattened = []
for r in range(rows):
    row = []
    for c in range(cols):
        # Start from bottom layer and override upwards
        key = ""
        for layer in layer_names:
            val = layers[layer][r][c]
            if val not in ("", "trans"):
                key = val
        row.append(key)
    flattened.append(row)

# Replace layers with the flattened one
keymap["layers"] = {"Flat": flattened}

with open("flattened.yaml", "w") as f:
    yaml.dump(keymap, f)


#!/usr/bin/env python3
# Author ID: dmartis(154861207)

import os

def free_space():
    process = os.popen("df -h | grep '/$' | awk '{print $4}'")
    output = process.read()
    return output.strip()

print(free_space())

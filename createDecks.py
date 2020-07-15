# Run as: blender -b <filename> -P <this_script> -- <csv_path>
from _csv import reader
from random import random

import bpy
import os
import sys


# random color for text
def get_random_color():
    r, g, b = [random.random() for i in range(3)]
    return r, g, b, 1


# Assume the last argument is csv path
csvPath = sys.argv[-1]

if os.path.exists(csvPath):
    # open file in read mode
    with open(csvPath, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        bpy.ops.object.text_add()
        for row in csv_reader:
            # take name and room number to create text
            obj = bpy.context.object
            obj.data.body = row

            # extrude
            obj.data.extrude = 0.2
            # texture/color
            obj.color = get_random_color()

            # export as gltf
            bpy.ops.export_scene.gltf('GLTF_EMBEDDED', filepath=os.path.join('C:\Users\spenc\Desktop\gltf', row + '.gltf')

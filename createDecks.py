# Run as: blender -b <filename> -P <this_script> -- <csv_path> <output_path>
from _csv import reader
import random

import bpy
import os
import sys


# random color for text
def get_random_color():
    r, g, b = [random.random() for i in range(3)]
    return r, g, b, 1


# Assume the last argument is csv path
csvPath = sys.argv[-2]

# Path where 3D files will be output
outputPath = sys.argv[-1]

if os.path.exists(csvPath):
    # open file in read mode
    with open(csvPath, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object

        for row in csv_reader:
            # take name and room number to create text
            bpy.ops.object.delete()
            bpy.ops.object.text_add(location=(0,0,0), rotation=(0,0,0))
            obj = bpy.context.object
            print(row[0])
            obj.data.body = row[0]
            # extrude
            obj.data.extrude = 0.2
            # texture/color
            obj.color = get_random_color()
            bpy.ops.object.convert(target="MESH")
            # export as gltf
            bpy.ops.export_scene.gltf(export_format='GLTF_EMBEDDED', filepath=os.path.join(outputPath, row[0]))


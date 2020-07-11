# Run as: blender -b <filename> -P <this_script> -- <image_path>
import bpy, sys, os
#Assume the last argument is image path
csvPath = sys.argv[-1]

if os.path.exists(csvPath):

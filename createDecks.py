# Run as: blender -b <filename> -P <this_script> -- <csv_path>
import bpy, sys, os
#Assume the last argument is csv path
csvPath = sys.argv[-1]

if os.path.exists(csvPath):
  # open file in read mode
  with open('students.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # take name and room number to create file
      bpy.ops.object.text_add()
      ob=bpy.context.object
      ob.data.body = row
    

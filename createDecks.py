def get_random_color():
    r, g, b = [random.random() for i in range(3)]
    return r, g, b


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
            bpy.ops.object.convert(target="MESH")
            mat = bpy.data.materials.new("Text")
            mat.use_nodes = True
            principled = PrincipledBSDFWrapper(mat, is_readonly=False)
            principled.base_color = (get_random_color())
            mesh = obj.data
            if len(mesh.materials) == 0:
                mesh.materials.append(mat)
            else:
                mesh.materials[0] = mat
            # export as gltf
            bpy.ops.export_scene.gltf(export_format='GLTF_EMBEDDED', filepath=os.path.join(outputPath, row[0]))

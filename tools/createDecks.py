from _csv import reader
import random

import bpy
from bpy_extras.node_shader_utils import PrincipledBSDFWrapper
import os
import sys
# List of UNH RGB color values
unh_colors = [(0, 29, 82), (0, 68, 187), (203, 77, 11),
             (247, 122, 5), (38, 54, 69), (92, 104, 116),
             (163, 169, 172), (255, 255, 255), (0, 53, 145)]


# Generate a random rgb value
def get_random_color(random_color_type):
    if random_color_type is 0:
        # Generate RGB values between 0-1
        r, g, b = [random.random() for i in range(3)]
    elif random_color_type is 1:
        # Get UNH Color tuple
        color = unh_colors[random.randint(0, 8)]
        # Divide each value by 255 as the material takes decimal values
        r, g, b = color[0]/255, color[1]/255, color[2]/255
    return r, g, b

# Generate the models using the CSV input
def generateModels(csv, output, color_type):
    # open file in read mode
    with open(csv, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)

        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            resident_name = row[0]
            room_number = row[1]
            # take name and room number to create text
            bpy.ops.object.delete()
            bpy.ops.object.text_add(location=(0,0,0), rotation=(0,0,0))
            obj = bpy.context.object
            print(resident_name)
            obj.data.body = resident_name + '\nRoom ' + room_number
            # extrude
            obj.data.extrude = 0.2
            # texture/color
            bpy.ops.object.convert(target="MESH")
            mat = bpy.data.materials.new("Text")
            mat.use_nodes = True
            principled = PrincipledBSDFWrapper(mat, is_readonly=False)
            principled.base_color = (get_random_color(color_type))
            mesh = obj.data
            if len(mesh.materials) == 0:
                mesh.materials.append(mat)
            else:
                mesh.materials[0] = mat
            # export as gltf
            bpy.ops.export_scene.gltf(export_format='GLTF_EMBEDDED', filepath=os.path.join(output, resident_name + '-' +room_number))

def main():
    # Get the CSV path to pull from
    while (True):
        print('Enter the full path of the CSV file to read from: ')
        csv_path = input()
        # Get the file extension
        file_extension = csv_path[-4:]
        print(f'File extension {file_extension}')

        if os.path.exists(csv_path) and file_extension == '.csv':
            print(f'Using csv file at: {csv_path}')
            break;
        else:
            print(f'Couldn\'t find path {csv_path}. Please try again.')

    # Get the output directory
    while (True):
        print('\nEnter the full path of the directory the gltf files should be output to: ')
        output_path = input()
        if os.path.exists(output_path) and os.path.isdir(output_path):
            print(f'Using output path: {output_path}')
            break;
        else:
            print(f'Couldn\'t find path {output_path}. Please try again.')

    # Get the color mode
    while (True):
        print('\nWould you like to use random color values 0-255 (0) or a random official UNH color?(1): ')
        color_type = int(input())
        if color_type is 0:
            print(f'Using random colors between 0-255.')
            break;
        elif color_type is 1:
            print(f'Using random official UNH colors.')
            break;
        else:
            print(f'Choice needs be 0 or 1. To choose random color between 0-255 use 0 and 1 for an official color.')


    generateModels(csv_path, output_path, color_type)



if __name__ == "__main__":
    main()

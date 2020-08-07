import os
from lxml.etree import tostring
from bs4 import BeautifulSoup

from _csv import reader

from pathlib import Path

def createPage(resident_name, room_number, template, output_dir):
    # Create a new html file
    filename = resident_name.lower() + " " + room_number
    filename = filename.replace(" ", "-")
    out_file = output_dir + '\\' + filename + ".html"
    Path(out_file).touch()
    # load the file
    with open(template, "r") as f:
        page = f.read()
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.findAll('a-asset-item'):
        link['src'] = "../models/" + filename + ".gltf"
    html_string = str(soup)

    # save the new file
    with open(out_file, "w") as outf:
        outf.write(str(soup))


def main():
    while (True):
        print('Enter the full path of the CSV file to read from: ')
        csv_path = input()
        # Get the file extension
        file_extension = csv_path[-4:]
        print(f'File extension {file_extension}')

        if os.path.exists(csv_path) and file_extension == '.csv':
            print(f'Using csv file at: {csv_path}')
            break
        else:
            print(f'Couldn\'t find path {csv_path}. Please try again.')

    while (True):
        print('Enter the full path of the directory to write the files to: ')
        output_path = input()
        if os.path.exists(output_path) and os.path.isdir(output_path):
            print(f'Using output path: {output_path}')
            break
        else:
            print(f'Couldn\'t find path {output_path}. Please try again.')

    while (True):
        print('Enter the full path of the template to use: ')
        template = input()
        if os.path.exists(template):
            print(f'Using template: {template}')
            break
        else:
            print(f'Couldn\'t find template {template}. Please try again.')

    # csv_path = "C:\\Users\\Jon\Desktop\\stoke_door_decs.csv"
    # output_path = "C:\\Users\\Jon\\Desktop\\out"
    # template = "template.html"

    with open(csv_path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)

        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            resident_name = row[0]
            room_number = row[1]
            createPage(resident_name, room_number, template, output_path)



if __name__ == "__main__":
    main()

"""
Copies and renames image files for retail website, using list
of codes + titles (no header!). Renames original image, and
produces a list of images not found
 -Jody 08-10-2014
"""

import csv
import os
import shutil


def read_codes_and_titles(filename):
    """
    reads in csv file, and creates a list.
    input csv of form:
    code,website title
    """
    with open(filename, "r") as file_in:
        code_titles = list(csv.reader(file_in))
    return code_titles


def generate_title(code_titles):
    """
    converts website title to concatenated
    version, and adds to dictionary
    """
    full_titles = {}
    for line in code_titles:
        code = line[0].lower()
        if code not in full_titles:
            new_title = ""
            temp_title = line[1].lower()
            temp_title = temp_title.split(" ")
            for word in temp_title:
                new_title += word + "-"
            full_titles[code] = new_title
    return full_titles


def rename_images(new_title, out_path):
    """
    renames files using new_title list
    and newly copied files in out_path
    """
    left_to_do = set([x for x in new_title.keys()])
    left_to_do = list(left_to_do)
    os.chdir(out_path)
    for target_file in os.listdir(out_path):
        if target_file[:7] in new_title:
            code = target_file.split(".")[0]
            new_filename = new_title[target_file[:7]] + code + ".jpg"
            if not os.path.isfile(new_filename):
                os.rename(target_file, new_filename)
            if target_file[:7] in left_to_do:
                left_to_do.pop(left_to_do.index(target_file[:7]))
    print "\nDone! Check", str(out_path), "for files!\n"
    print "Images not found for:"
    for line in left_to_do:
        print line


def main():
    """
    the bit that does all the work!
    """
    filename = raw_input("Enter filename of codes list, in csv: ")
    while not os.path.isfile(filename):
        print "\nFile not found - please try again."
        filename = raw_input("Enter filename of codes list, in csv: ")
    code_titles = read_codes_and_titles(filename)
    new_title = generate_title(code_titles)
    starting_path = os.getcwd()
    image_path = "c:/image_test/"
    rename_images(new_title, image_path)
    os.chdir(starting_path)


if __name__ == "__main__":
    main()

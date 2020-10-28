from os import listdir, path
from os.path import isfile, join
import json
import os

# taking data from json files
json_data_source_1 = open("data2.json")
json_data_source_2 = open("data3.json")
# list of all the files in the directory
all_files_in_the_directory = [f for f in listdir() if isfile(join('', f))]

#to be removed
all_files_in_the_directory.remove("main.py")


def checkIfTheFolderIsAlreadyCreated(folderName):
    if not os.path.exists(folderName):
        os.makedirs(folderName)


sorted_dictionary = {
    "C++": [],
    "Python": [],
    "C": [],
    "Verilog": [],
    "JavaScript": [],
    "Images": [],
    "Linux": [],
    "Windows": [],
    "Mac": [],
    "iOS": [],
    "Android": [],
    "Videos": [],
    "Others": []
}

possibile_type_of_files = json.load(json_data_source_1)


for file in all_files_in_the_directory:
    file_format_found_status = 0
    for x in possibile_type_of_files:
        # print(os.path.splitext(file)[1].lower(), 1)
        # print(possibile_type_of_files[x], 2)
        if(os.path.splitext(file)[1].lower() in possibile_type_of_files[x]):
            
            checkIfTheFolderIsAlreadyCreated(x)
            sorted_dictionary[x].append(file)
            file_format_found_status = 1
    if(file_format_found_status == 0):
        checkIfTheFolderIsAlreadyCreated("Others")
        sorted_dictionary["Others"].append(file)

for sorted_files in sorted_dictionary:

    for sorted_file in sorted_dictionary[sorted_files]:

        temp_string = sorted_files + "/" + sorted_file
        os.replace(sorted_file, temp_string)
        
# list of all folders in the directory
all_folders_in_the_directory = [f for f in listdir() if not isfile(join('', f))]

# this helps us in creating a super directory
super_directories = json.load(json_data_source_2)

for super_directory in super_directories:
    checkIfTheFolderIsAlreadyCreated(super_directory)
    for directory in super_directory:
        temp_string = super_directory + "/" + directory
        os.replace(directory, temp_string)
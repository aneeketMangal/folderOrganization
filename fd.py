from os import listdir, path
from os.path import isfile, join
import json
import os


all_files_in_the_directory = [f for f in listdir() if isfile(join('', f))]
json_data_source = open("data2.json")


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
possibile_type_of_files = json.load(json_data_source)
print(all_files_in_the_directory)

for file in all_files_in_the_directory:
    file_format_found_status = 0
    for x in possibile_type_of_files:
        if(os.path.splitext(file)[1].lower() in x):
            print(file)
            checkIfTheFolderIsAlreadyCreated(x)
            sorted_dictionary[x].append(file)
            file_format_found_status = 1
    if(file_format_found_status == 0):
        checkIfTheFolderIsAlreadyCreated("Others")
        sorted_dictionary["Others"].append(file)

for sorted_files in sorted_dictionary:
    print(sorted_files[0])
    for sorted_file in sorted_dictionary[sorted_files]:
        
        temp_string = sorted_files + "/" + sorted_file
        os.replace(sorted_file, temp_string)
            

import os
import json
import csv
import pickle

def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

def create_file_info(file_path):
    file_name = os.path.basename(file_path)
    parent_directory = os.path.dirname(file_path)
    if os.path.isfile(file_path):
        file_type = "file"
        file_size = os.path.getsize(file_path)
    else:
        file_type = "directory"
        file_size = get_directory_size(file_path)
    file_info = {
        "name": file_name,
        "parent": parent_directory,
        "type": file_type,
        "size": file_size
    }
    return file_info

def save_structure_to_json(structure, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(structure, file, ensure_ascii=False, indent=4)

def save_structure_to_csv(structure, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'parent', 'type', 'size'])
        writer.writeheader()
        writer.writerows(structure)

def save_structure_to_pickle(structure, filename):
    with open(filename, 'wb') as file:
        pickle.dump(structure, file)

def traverse_directory(directory):
    structure = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = create_file_info(file_path)
            structure.append(file_info)
    return structure

directory_path = "C:\\Sofiya\\test"
file_structure = traverse_directory(directory_path)

save_structure_to_json(file_structure, 'file_structure.json')
print("Структура файлов сохранена в файле file_structure.json")
save_structure_to_csv(file_structure, 'file_structure.csv')
print("Структура файлов сохранена в файле file_structure.csv")

save_structure_to_pickle(file_structure, 'file_structure.pickle')
print("Структура файлов сохранена в файле file_structure.pickle")
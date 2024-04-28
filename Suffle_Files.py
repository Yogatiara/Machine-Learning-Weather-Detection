import os
import random

def shuffle_images(folder_path):
    file_list = os.listdir(folder_path)
    
    random.shuffle(file_list)
    
    return file_list

def rename_files(folder_path, shuffled_files):
    for index, file_name in enumerate(shuffled_files):
        old_path = os.path.join(folder_path, file_name)
        new_name = f"Training_{index + 1}{os.path.splitext(file_name)[1]}"
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)


folder_path = "./Training_Weather_Dataset"

shuffled_files = shuffle_images(folder_path)
rename_files(folder_path, shuffled_files)

print("File telah diacak dan disimpan kembali ke folder yang sama.")

import sys,os

#filetype String of format ".txt", ".o", ".java", etc.
def delete_filetype(filetype):
    current_dir_path = os.getcwd()
    dir_file_list = os.listdir(current_dir_path)
    for f in dir_file_list:
        if f.endswith(filetype):
            os.remove(f)
            
            
            

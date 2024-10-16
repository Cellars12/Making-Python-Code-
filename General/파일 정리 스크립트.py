import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder_path, ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))

folder_path = 'C:/path/to/your/folder'  # 정리할 폴더 경로
organize_files(folder_path)

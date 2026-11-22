import os
import shutil

def make_folder(path):
    """경로가 없으면 폴더 생성"""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    return path

def delete_folder_contents(folder_path):
    """폴더 내 모든 파일/폴더 삭제 (폴더 자체는 남김)"""
    try:
        if os.path.isdir(folder_path):
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
    except Exception as e:
        print(f"Error deleting {folder_path}: {e}")

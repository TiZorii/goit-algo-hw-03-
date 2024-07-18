import os
import shutil

def copy_files_recursively(src, dst):
    # Перевірити наявність вихідної директорії
    if not os.path.exists(src):
        print(f"Вихідна директорія {src} не існує.")
        return

    # Створити директорію призначення, якщо вона не існує
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        if os.path.isdir(src_path):
            # Рекурсивно викликати для піддиректорії
            copy_files_recursively(src_path, dst)
        else:
            # Отримати розширення файлу
            file_ext = os.path.splitext(item)[1][1:].lower() or 'no_extension'
            dst_dir = os.path.join(dst, file_ext)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            shutil.copy2(src_path, os.path.join(dst_dir, item))
            print(f"Скопійовано {src_path} до {dst_dir}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("src", help="Вихідна директорія")
    parser.add_argument("dst", nargs='?', default="dist", help="Директорія призначення")
    args = parser.parse_args()

    copy_files_recursively(args.src, args.dst)

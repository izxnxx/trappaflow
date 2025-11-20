import os
import shutil
import glob

def main():
    # 1
    print("1. Вміст folder_1:")
    for root, dirs, files in os.walk("folder_1"):
        level = root.replace("folder_1", '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"{indent}  {file}")
    # 2
    os.makedirs("folder_1/folder_4", exist_ok=True)
    print("\n2. Створено folder_1/folder_4")

    # 10
    for file in glob.glob("folder_3/*.docx"):
        shutil.copy2(file, "folder_1/folder_4")
        print(f"10. Скопійовано: {os.path.basename(file)}")

    # 19
    for file in glob.glob("folder_3/*.doc"):
        shutil.move(file, "folder_1/folder_4")
        print(f"19. Переміщено: {os.path.basename(file)}")

    # 30
    for file in glob.glob("folder_1/folder_2/*.docx"):
        name, ext = os.path.splitext(file)
        os.rename(file, f"{name}_2024{ext}")
        print(f"30. Перейменовано: {os.path.basename(file)}")

    # 45
    for file in glob.glob("folder_1/folder_2/*.txt"):
        os.remove(file)
        print(f"45. Видалено: {os.path.basename(file)}")

    # 57
    shutil.rmtree("folder_3")
    print("57. Видалено folder_3")

    print("\nФінальний вміст:")
    for root, dirs, files in os.walk("folder_1"):
        level = root.replace("folder_1", '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"{indent}  {file}")

if __name__ == "__main__":
    main()
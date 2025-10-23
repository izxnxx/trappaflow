# Початковий вміст каталогу
dir = (
 "_file1.doc\n"
 "file2.pdf\n"
 "file222_.docx\n"
 "cmd.exe\n"
 "sys.dll\n"
 "FiLe7_5.txt\n"
 "foto1.jpg\n"
 "song1.mp3\n"
 "!!!song2.mp3\n"
 "video.avi\n"
 "file9.txt\n"
 "file_3_document.docx\n"
 "my_document!!!.ppt\n"
 "main.c\n"
 "lab3.py\n"
 "lookup.xml\n"
 "pic1.png\n"
 "pic2.bmp\n"
)

files = [f for f in dir.strip().split("\n")]

#1
print("Початковий вміст каталогу")
for f in files:
    print(f)
print(f"У каталозі є {len(files)} файлів")

#2
ext_to_count = ["mp3", "exe"]
for ext in ext_to_count:
    count = sum(1 for f in files if f.lower().endswith("." + ext))
    print(f"Файлів з розширенням {ext}: {count}")

#3
new_files = []
for f in files:
    if f.lower().endswith(".exe"):
        base = f[:f.lower().rfind(".exe")]
        f = base + ".docx"
    new_files.append(f)
files = new_files

print("\nКаталог після заміни розширення .exe на .docx")
for f in files:
    print(f)

#4
def format_T(filename):
    parts = filename.split(".")
    name = parts[0]
    ext = parts[1] if len(parts) > 1 else ""
    name = name.lower().capitalize()
    return f"{name}.{ext.lower()}" if ext else name

files = [format_T(f) for f in files]

print("\nКаталог після приведення імен файлів до T (перша велика літера)")
for f in files:
    print(f)

#5
files = [f for f in files if not f.lower().endswith(".avi")]

print("\nКаталог після видалення файлів з розширенням avi")
for f in files:
    print(f)

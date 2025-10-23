import struct
import os

filename = "bmp_8.bmp"

if not os.path.exists(filename):
    print(f"Помилка: Файл '{filename}' не знайдено!")
    print("Перевірте:")
    print("1. Чи файл знаходиться в тій самій папці що і скрипт")
    print("2. Чи правильно вказано ім'я файлу")
    print("3. Поточка директорія:", os.getcwd())

    files = os.listdir()
    bmp_files = [f for f in files if f.lower().endswith('.bmp')]
    if bmp_files:
        print("\nЗнайдені BMP файли:")
        for bmp_file in bmp_files:
            print(f"  - {bmp_file}")
    else:
        print("\nBMP файлів не знайдено в поточній директорії")

    exit(1)

try:
    with open(filename, "rb") as f:
        file_header_data = f.read(14)
        bfType, bfSize, bfReserved1, bfReserved2, bfOffBits = struct.unpack('<2sIHHI', file_header_data)

        info_header_data = f.read(40)
        (biSize, biWidth, biHeight, biPlanes, biBitCount, biCompression,
         biSizeImage, biXPelsPerMeter, biYPelsPerMeter, biClrUsed, biClrImportant) = struct.unpack('<IIIHHIIIIII',
                                                                                                   info_header_data)

    print("=== BITMAP FILE HEADER ===")
    print(f"bfType: {bfType.decode()}")
    print(f"bfSize: {bfSize} байт")
    print(f"bfReserved1: {bfReserved1}")
    print(f"bfReserved2: {bfReserved2}")
    print(f"bfOffBits: {bfOffBits}")

    print("\n=== BITMAP INFO HEADER ===")
    print(f"biSize: {biSize} байт")
    print(f"biWidth: {biWidth} пікселів")
    print(f"biHeight: {biHeight} пікселів")
    print(f"biPlanes: {biPlanes}")
    print(f"biBitCount: {biBitCount} біт на піксель")
    print(f"biCompression: {biCompression}")
    print(f"biSizeImage: {biSizeImage} байт")
    print(f"biXPelsPerMeter: {biXPelsPerMeter}")
    print(f"biYPelsPerMeter: {biYPelsPerMeter}")
    print(f"biClrUsed: {biClrUsed}")
    print(f"biClrImportant: {biClrImportant}")

except Exception as e:
    print(f"Помилка при читанні файлу: {e}")
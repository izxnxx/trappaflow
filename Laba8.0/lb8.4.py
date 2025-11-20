import os
import yara

rule_text = ""


def scan_malware_files(directory):
    rules = yara.compile(source=rule_text)
    for i in range(1, 31):
        filename = f"yara_{i:02d}.exe"
        filepath = os.path.join(directory, filename)

        if os.path.exists(filepath):
            matches = rules.match(filepath)
            if matches:
                print(f"Виявлено malware у файлі: {filename}")
                return filename

    print("Malware не виявлено")
    return None

if __name__ == "__main__":
    malware_dir = "malware"  # Шлях до директорії з файлами
    infected_file = scan_malware_files(malware_dir)
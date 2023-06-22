import magic
def analyze_file(file_path):
    m = magic.Magic()
    file_type = m.from_file(file_path)
    print(f"File: {file_path}")
    print(f"Type: {file_type}")

file_path = "description.txt"
analyze_file(file_path)

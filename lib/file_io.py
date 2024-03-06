def write_file(file_name="test_file", file_content="This is a test content."):
    with open(f"{file_name}.txt", mode='w',encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name="test_file", file_content="This is a test content."):
    with open(f"{file_name}.txt",mode= 'a') as file:
        file.write(file_content)

def read_file(file_name="test_file"):
    with open(f"{file_name}.txt", 'r') as file:
        return file.read()

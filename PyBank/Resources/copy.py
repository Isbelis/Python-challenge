import os
file_to_load = "/path/to/missing_file.txt"
 
if os.path.exists(file_to_load):
    with open(file_to_load, 'r') as file:
        content = file.read()
    print(content)
else:
    print(f"File not found at {file_to_load}") 




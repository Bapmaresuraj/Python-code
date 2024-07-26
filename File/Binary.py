# Writing and reading in binary mode
with open('example.bin', 'wb') as file:
    file.write(b'Hello, World!')

with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)

boundary = b'5470659b38b6efd5d9a050d1ca4a4772' 
with open('postrequest', 'rb') as f:
    data = f.read()


start = data.find(b'filename="ricetta.txt.zip"') 
start = data.find(b'\r\n\r\n', start) + 4  

end = data.find(b'--' + boundary, start)


file_bytes = data[start:end]
with open('ricetta_from_wireshark.zip', 'wb') as f:
    f.write(file_bytes)

print("Saved ricetta_from_wireshark.zip")

## password qhcdpoktbjdsujbsrpjwr
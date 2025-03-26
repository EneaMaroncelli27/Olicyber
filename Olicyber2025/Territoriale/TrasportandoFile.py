import os
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


immagini_enc = 'Immagine_Encriptate'
immagini_dec = 'Immagini_Decriptate'
os.makedirs(immagini_dec, exist_ok=True)

all_files = [f for f in os.listdir(immagini_enc) if f.endswith('.enc')]

base_names = set()
for filename in all_files:
    try:
        base, _ = filename.rsplit('_', 1)
        base_names.add(base)
    except ValueError:

        continue


for base in base_names:
    key = sha256(base.encode()).digest()
    iv = b'\x00' * 16
    chunk_index = 0
    output_file_path = os.path.join(immagini_dec, base)
    
    with open(output_file_path, 'wb') as outfile:
        while True:
            chunk_filename = f"{base}_{chunk_index:02}.enc"
            chunk_filepath = os.path.join(immagini_enc, chunk_filename)
            if not os.path.exists(chunk_filepath):
                break
        
            with open(chunk_filepath, 'rb') as chunk_file:
                encrypted_chunk = chunk_file.read()
            
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            
            try:
                decrypted_chunk = unpad(cipher.decrypt(encrypted_chunk), AES.block_size)
            except ValueError as e:
                print(f"Errore {chunk_filename}: {e}")
                break
            

            outfile.write(decrypted_chunk)
            chunk_index += 1
            


# standard library
import os
import sys
import zlib
from typing import Optional

# local
from encryption import encrypt, decrypt



# the level of compression to use. Should be 0-9. Higher numbers compress more, but are slower.
COMPRESSION = 6

# root path depending on if the program is run as an exe or as a script respectively
if getattr(sys, 'frozen', False): 
    ROOT_DIR = os.path.dirname(sys.executable)

else: 
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



def get_global_path(local_path: str) -> str:
    '''
    Gets the global path of a file from a local path.
    '''

    return os.path.join(ROOT_DIR, local_path)



def path_exists(path: str) -> bool:
    return os.path.exists(path)



def _compress(
        text: str
    ) -> bytes:

    '''
    Compresses a string of text.

    `compression` is the level of compression to use. Should be 0-9. Higher numbers compress more, but are slower.
    '''

    text_data = text.encode('utf-8')

    compressed_data = zlib.compress(text_data, level=COMPRESSION)

    return compressed_data



def _decompress(
        compressed_data: bytes
    ) -> str:

    '''
    Decompresses bytes.
    '''

    decompressed_data = zlib.decompress(compressed_data)

    text = decompressed_data.decode('utf-8')

    return text



def save(
        text: str,
        local_path: str,
        encryption_password: Optional[str] = None
    ) -> None:

    '''
    Saves text to a file. The file should be binary. Use `save_plaintext` for .txt files.

    `encryption_password` is the optional encryption password to use. Leave as `None` for no encryption.
    '''

    path = get_global_path(local_path)

    compressed_data = _compress(text)

    if encryption_password:
        save_data = encrypt(compressed_data, encryption_password)

    else:
        save_data = compressed_data

    with open(path, 'wb') as f:
        f.write(save_data)

    return None



def save_plaintext(
        text: str,
        local_path: str
    ) -> None:

    '''
    Saves text to a plaintext file.
    '''

    path = get_global_path(local_path)

    with open(path, 'w') as f:
        f.write(text)

    return None



def load(
        local_path: str,
        decryption_password: Optional[str] = None
    ) -> str:

    '''
    Loads text from a file. The file should be in binary. Use `load_plaintext` for .txt files.

    `decryption_password` should be the same as the password used to encrypt the data originally.
    '''

    path = get_global_path(local_path)

    with open(path, 'rb') as f:
        file_data = f.read()

    if decryption_password:
        compressed_data = decrypt(file_data, decryption_password)

    else:
        compressed_data = file_data

    text = _decompress(compressed_data)

    return text



def load_plaintext(
        local_path: str
    ) -> str:

    '''
    Loads text from a plaintext file.
    '''

    path = get_global_path(local_path)

    with open(path, 'r') as f:
        text = f.read()

    return text


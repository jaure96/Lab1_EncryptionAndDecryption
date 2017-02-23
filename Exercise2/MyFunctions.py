import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
import base64


def decrypt_file(key):
    decoded_key = base64.b64decode(key)
    my_box = nacl.secret.SecretBox(decoded_key)
    crypted_text = read_crypted_text_file("../data/ficheros-ejercicios-cifrado/texto_cifrado_paso2_nacl.base64")
    readable_text = my_box.decrypt(crypted_text)
    print "*****************************"
    print "The secret text was:   ",readable_text
    print "*****************************"
    return readable_text


def read_file(file_path):
    try:
        file = open(file_path, "r")
        file_content = file.read()
    except IOError:
        print "Could not read file: ", file_path
    finally:
        file.close()

    return file_content


def read_crypted_text_file(path):
    try:
        file = open(path, "r")
        file_content = base64.b64decode(file.read())
    except IOError:
        print "Could not read the file: ", path
    finally:
        file.close()

    return file_content


def load_secret_key_object(private_key_path):
    encoded_private_key = read_file(private_key_path)
    decoded_private_key = base64.b64decode(encoded_private_key)
    private_key = PrivateKey(decoded_private_key)
    return private_key


def load_public_key_object(public_key_path):
    encoded_public_key = read_file(public_key_path)
    decoded_public_key = base64.b64decode(encoded_public_key)
    public_key = PublicKey(decoded_public_key)
    return public_key


def create_encrypted_64file_ready_to_send(sender_sk, reciver_pk, message, file_path):
    box = Box(sender_sk, reciver_pk)
    nonce = nacl.utils.random(Box.NONCE_SIZE)
    encrypted_text = box.encrypt(message, nonce)
    encrypted_text64 = base64.b64encode(encrypted_text)
    write_in_file(file_path, encrypted_text64)


def write_in_file(file_path, content):
    try:
        file = open(file_path, "w")
        file.write(content)
    except IOError:
        print "Error writing into file", file_path
    finally:
        file.close()

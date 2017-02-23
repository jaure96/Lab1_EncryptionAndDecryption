from keyczar import keyczar
import base64


def import_keys(key_path):
    return keyczar.Crypter.Read(key_path)


def read_file(file_path):
    try:
        file = open(file_path, "r")
        file_content = file.read()
    except IOError:
        print ("Could not read file", file_path)
    finally:
        file.close()

    return file_content


def write_in_file(file_path, content):
    try:
        file = open(file_path, "w")
        file.write(content)
    except IOError:
        print ("Error writing into file", file_path)
    finally:
        file.close()


def decrypt(file_content, crypter):
    try:
        file_content_decrypted = crypter.Decrypt(file_content)
        decoded_file_content = base64.b64encode(file_content_decrypted)
        print "*********************************************"
        print"Decrypted file content:   ",decoded_file_content
        print "*********************************************"
    except NameError:
        print ("Something is not initialized")
    return decoded_file_content

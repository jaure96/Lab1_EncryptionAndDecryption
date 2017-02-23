from MyFunctions import import_keys
from MyFunctions import read_file
from MyFunctions import decrypt
from MyFunctions import write_in_file

if __name__ == '__main__':

    # Load the files '1' and 'meta' and we insert them into the variable crypter
    crypter = import_keys("../data/ficheros-ejercicios-cifrado/ficheros_clave_primaria_keyczar")

    # Read and load the encrypted file that contains the private key
    encrypted_file_content = read_file("../data/ficheros-ejercicios-cifrado/texto_cifrado_paso2_keyczar.base64")

    # Using the previous imported crypter and encrypted file, decrypt the file and print in console
    decrypted_file_content = decrypt(encrypted_file_content, crypter)

    # Save the decrypted text(key) in a file in order to prepare the second exercise
    write_in_file("../data/decryptedKey.txt", decrypted_file_content)

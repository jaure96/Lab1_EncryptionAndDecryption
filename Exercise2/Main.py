
from MyFunctions import read_file
from MyFunctions import decrypt_file
from MyFunctions import load_secret_key_object
from MyFunctions import load_public_key_object
from MyFunctions import create_encrypted_64file_ready_to_send

if __name__ == '__main__':
    # Simply read the plane text created in the previous exercise.
    key = read_file("../data/decryptedKey.txt")

    # With the key that was in the plain text decrypt the file that contains the secret phrase.
    message = decrypt_file(key)

    # Create the secret and public keys of the objects.
    student_pk = load_public_key_object("../data/ficheros-ejercicios-cifrado/pkAlumno.base64")
    student_sk = load_secret_key_object("../data/ficheros-ejercicios-cifrado/skAlumno.base64")
    teacher_pk = load_public_key_object("../data/ficheros-ejercicios-cifrado/pkTutor.base64")

    # With the previous keys create an encrypted file to send to the teacher.
    create_encrypted_64file_ready_to_send(student_sk, teacher_pk, message, "../data/encryptedMessage.base64")

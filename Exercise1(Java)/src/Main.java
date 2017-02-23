import java.util.Base64;

import org.keyczar.Crypter;
import org.keyczar.exceptions.KeyczarException;

public class Main {

	public static void main(String[] args) {
		
		MyFileReaderWriter myFileReaderWriter = new MyFileReaderWriter();
		Crypter crypter;
		byte [] fileInBytes = null;
		byte [] fileInBytes64 = null;
		byte [] decrypetedBytes = null;
		
		
		try {
			
			crypter = new Crypter("data/ficheros-ejercicios-cifrado/ficheros_clave_primaria_keyczar");
			fileInBytes = myFileReaderWriter.getByteArrayFromFile("data/ficheros-ejercicios-cifrado/texto_cifrado_paso2_keyczar.base64");
			
			fileInBytes64 = Base64.getDecoder().decode(fileInBytes);		
			decrypetedBytes = crypter.decrypt(fileInBytes64);
			fileInBytes64 = null;
			fileInBytes64 = Base64.getEncoder().encode(decrypetedBytes);
			
			myFileReaderWriter.writeFileFromByteArray(fileInBytes64, "data/ficheros-ejercicios-cifrado/decryptedFile.txt");
			
			myFileReaderWriter.readAndPrintDataOfBinaryFile("data/ficheros-ejercicios-cifrado/decryptedFile.txt");
			
		} catch (KeyczarException e) {
			e.printStackTrace();
		}		
	}

}

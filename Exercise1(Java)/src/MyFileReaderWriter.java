import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class MyFileReaderWriter {
	
	
	public byte[] getByteArrayFromFile(String filePath){
		
		File file = new File(filePath);
		FileInputStream fileInpStr = null;
		byte []filecontent = null;
		
		try {			
			fileInpStr = new FileInputStream(file);
			filecontent = new byte[(int)file.length()];
			fileInpStr.read(filecontent);
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				fileInpStr.close();				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return filecontent;
	}

	public void writeFileFromByteArray(byte[] data, String outputFilePath){
		
		FileOutputStream fileOutpStr = null;
		
		try {
			fileOutpStr = new FileOutputStream(outputFilePath);
			fileOutpStr.write(data);
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				fileOutpStr.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}		
	}

	public void readAndPrintDataOfBinaryFile(String filePath){
		
		FileInputStream inputStream = null;
		byte[] buffer;

        try {
            buffer = new byte[1000];
            inputStream = new FileInputStream(filePath);
            
            while((inputStream.read(buffer)) != -1) {
                System.out.println(new String(buffer));
            }                   
        }
        catch(Exception e) {
        	e.printStackTrace();
        }finally {
        	 try {
				inputStream.close();
			} catch (IOException e) {
				e.printStackTrace();
			}   
		}
    }
	
}

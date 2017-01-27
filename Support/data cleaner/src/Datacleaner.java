import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import com.oracle.xmlns.internal.webservices.jaxws_databinding.ExistingAnnotationsType;




		
public class Datacleaner {

	
	public static void main(String[] args) {
		
		//System.out.println("lol");
		File file = new File("groceries.csv");
		 BufferedWriter bw = null;
 		FileWriter fw = null;
		try {
			fw = new FileWriter("finalrecords.csv");
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		bw = new BufferedWriter(fw);
		
		try {
			Scanner c = new Scanner(file);
			int counter = 0;
			while (c.hasNextLine()) {
	           String line = c.nextLine();
	           // System.out.println(counter + "   "+ line);
	            counter++;
	            
	           
	            String r = line.replace(",,","");
	            System.out.println( counter + "    " + r );
	            String complete = counter + "     "  + r;

	    			bw.write(r);
//	    			bw.append("/n");
	    			bw.newLine();
	    		
	        }
	        c.close();
	        
	        
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
			
		
	}
}

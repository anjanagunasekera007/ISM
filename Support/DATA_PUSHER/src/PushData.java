import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;


public class PushData {

	public static void main(String[] args) {
		
		
		File ifile = new File("all_items.txt");
		try {
			Scanner c = new Scanner(ifile);
			int counter = 1;
			while(c.hasNext())
			{
				String item = c.nextLine();
				System.out.println(item + " " + counter);
				counter++;
				addRecord(item, 200, 0);
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public static void addRecord(String itemName,int itemQty,int itemSold)
	{
		String rec = "INSERT INTO items (itemName, itemQTY,itemsSold )VALUES('"+itemName+"',"+itemQty+","+itemSold+");";
		
		BufferedWriter bw = null;
		FileWriter fw = null;
		String filename = "itemSQL.txt";
		try {
			bw = new BufferedWriter(new FileWriter(filename, true));
			bw.append(rec);
			bw.newLine();

			System.out.println("Done");

		} catch (IOException e) {

			e.printStackTrace();

		} finally {

			try {

				if (bw != null)
					bw.close();

				if (fw != null)
					fw.close();

			} catch (IOException ex) {

				ex.printStackTrace();

			}

		}
		
		
	}
}

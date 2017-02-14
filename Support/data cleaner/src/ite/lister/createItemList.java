package ite.lister;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class createItemList {
	
	public static void main(String[] args) {
		
		
		File ifile = new File("all_items.txt");
		try {
			String itemString = "";
			Scanner c = new Scanner(ifile);
			while(c.hasNext())
			{
				String r = c.nextLine();
				System.out.println(r);
				itemString = itemString + ","+r;
				
				
			}
			String h = itemString.substring(1, 2035);
			System.out.println(itemString);
			System.out.println(h);
			System.out.println(itemString.length());
			writeItems(h, "i.txt");
		}catch(Exception e){}
		
		
		}
	
	public static void writeItems(String asd ,String filename) {

		BufferedWriter bw = null;
		FileWriter fw = null;

		try {

//			String content = "This is the content to write into file\n";

//			fw = new FileWriter("Item List 9.txt");
			bw = new BufferedWriter(new FileWriter(filename, true));
			bw.append(asd);
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

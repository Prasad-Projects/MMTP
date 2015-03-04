import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class JSONDistanceCalculator {
 
	static String beg,end;
 static StringBuffer start=new StringBuffer(), stop=new StringBuffer();
 static float totDistance;
 public static void main(String args[])
 {
  JSONInterface ji=new JSONInterface();
  BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
  try
  {
   int perPerson = 3;  // 3Litres for 100km on one person
   int aviationFuelCost = 53;
   System.out.println("Enter the source place : ");
   beg=br.readLine();
   System.out.println("Enter the distance place : ");
   end=br.readLine();
   start.append(beg);
   stop.append(end);
   for(int i=0; i<start.length(); i++)
   {
    if(start.charAt(i)==' ')
    {
     start.deleteCharAt(i);
     start.insert(i, "%20");
    }
   }
   for(int i=0;i<stop.length();i++)
   {
    if(stop.charAt(i)==' ')
    {
     stop.deleteCharAt(i);
     stop.insert(i, "%20");
    }
   }
   totDistance=ji.calcDistance(start,stop);
   
   System.out.println("The distance between "+beg+" and "+end+" is = "+totDistance);
   float calc = (totDistance/100)*3*aviationFuelCost;
   System.out.println("The static price of a plane ticket = " + calc);
           
  }
  catch(IOException e)
  {
   System.out.println("Improper place value set..");
   e.printStackTrace();
  }
  catch(Exception e)
  {
   System.out.println("Json type exception");
   e.printStackTrace();
  }
 }
	
 
}
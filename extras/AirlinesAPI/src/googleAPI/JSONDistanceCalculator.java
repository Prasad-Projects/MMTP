package googleAPI;

/**
 * 
 * @author kartik
 *
 */
public class JSONDistanceCalculator {
 
	static String beg,end;
	static StringBuffer start=new StringBuffer(), stop=new StringBuffer();
	static float totDistance;
	public static void main(String args[])
	{
		JSONInterface ji=new JSONInterface();
		//BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		try
		{
			double perPerson = 1.55;  // 3Litres for 100km on one person
			int trainFuelCost = 58;
			//System.out.println("Enter the source place : ");
			//beg=br.readLine();
			//System.out.println("Enter the distance place : ");
			//end=br.readLine();
			Database_conn temp = new Database_conn();
			String[][] route = temp.getDetails();
			
			
			
			int j = 0;
			for(j=0;j<331830;j++)
			{	
				
				beg = route[j][0];
				end = route[j][1];
				
				//System.out.println(beg + " " + end);
				start.delete(0, start.length());
				start.append(beg);
				stop.delete(0, stop.length());
				stop.append(end);
				if(end.length()!=3){
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
								
				//System.out.println("The distance between "+start+" and "+stop+" is = "+totDistance);
				float calc = (totDistance/100)*3*trainFuelCost;
				System.out.println("The static price of a plane ticket = " + j+ calc);

				if(calc == 0.0) continue;
				temp.update(beg,end,totDistance,calc);
				}
			}
			temp.close_connection();
			}catch(Exception e)
			{
				System.out.println("Json type exception");
				e.printStackTrace();
			}
			
	}

}

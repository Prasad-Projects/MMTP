package googleAPI;

import java.sql.*;

public class Database_conn {

	final static String JDBC_Driver = "com.mysql.jdbc.Driver";
	final static String DB_URL = "jdbc:mysql://localhost/";
	
	//  Database credentials
	static final String USER = "newuser";
	static final String PASS = "password";
	Connection conn = null;
	Statement stmt = null;
	
	public Database_conn() throws ClassNotFoundException {
		// TODO Auto-generated constructor stub
		try{
			Class.forName("com.mysql.jdbc.Driver");
			//System.out.println("Error1");
			conn = DriverManager.getConnection(DB_URL,USER,PASS);
			//System.out.println("Connection Error");
			stmt = conn.createStatement();
		}catch(SQLException e){
			System.out.println("SQL Exception");
		}
	}
	String[][] getDetails() throws ClassNotFoundException, SQLException{
	
		String[][] route = new String[575][];
		//Use database
		String sql = "USE mmtp1";
		stmt.executeUpdate(sql);
		
		sql = "SELECT DISTINCT src,dest from airline";
		ResultSet res = stmt.executeQuery(sql);
		int i = 0;
		while(res.next()){
			String src = res.getString("src");
			String dest = res.getString("dest");
			route[i] = new String[2];
			//System.out.println(src + " " + dest);
			route[i][0] = src;
			route[i][1] = dest;
			i++;
		}
		return route;
	}
	void update(String beg,String end,float distance,float price)
	{
		String sql = "UPDATE airline SET distance = " + distance + " ,price = " + price + 
				" WHERE src = '" + beg + "' AND dest = '" + end + "'";
		//System.out.println(sql);
		try {
			stmt.executeUpdate(sql);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	void close_connection()
	{
		if(stmt!=null)
			try {
				stmt.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
		if(conn!=null)
			try {
				conn.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	}
	

}

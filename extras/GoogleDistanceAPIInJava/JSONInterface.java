/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package restcall;

/**
 *
 * @author anadi
 */
import java.io.*;
import java.net.URL;
import java.nio.charset.Charset;
import org.json.*;
public class JSONInterface {
    Integer tem;
 Float dist;


 private static String readAll(Reader rd) throws IOException 
 {
     StringBuilder sb = new StringBuilder();
     int cp;
     while ((cp = rd.read()) != -1) 
     {
       sb.append((char) cp);
     }
     return sb.toString();
  }
 
 public static JSONObject readJsonFromUrl(String url) throws IOException, JSONException 
 {
     InputStream is = new URL(url).openStream();
     try 
     {
       BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
       String jsonText = readAll(rd);
       JSONObject json = new JSONObject(jsonText);
       return json;
     }
     finally 
     {
       is.close();
     }
 }


 public float calcDistance(StringBuffer beg, StringBuffer end) 
 {
  JSONObject json=null;
  try 
  {
  
   json = readJsonFromUrl("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+beg+"&destinations="+end+"&mode=driving&sensor=false");
   json.get("rows");
   JSONArray arr=null;
   arr = json.getJSONArray("rows");
   tem=(Integer)arr.getJSONObject(0).getJSONArray("elements").getJSONObject(0).getJSONObject("distance").getInt("value");
   dist=(float)tem/1000;
  }
  catch (JSONException e) 
  {
   e.printStackTrace();
  } 
  catch (IOException e)
  {
      e.printStackTrace();
  }
 return dist;
 }
}

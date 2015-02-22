<html>
<h2>Result</h2>
<?php
	//Storing the variables passed from main page
	$Source = $_POST['src'];
	$Destination = $_POST['dest'];
	$costScale = (int)$_POST['fare'];
	$timeScale = (int)$_POST['time'];
	$seatScale = (int)$_POST['seat'];
	$isAC='false';
	printf("%s",$Source);
	printf("%s",$Destination);
	if(isset($_POST['isAC']))
	{
    $isAC='true';
    
	}
	
	$isSleeper = 'false';
	if(isset($_POST['isSleeper']))
	{
    $isSleeper='true';
	}
	printf("%s",$isAC);
	printf("%s",$isSleeper);
	//Connection to database
	$dbhost = '127.0.0.1';
	
	$conn = mysqli_connect("127.0.0.1","root","","buses");
	if(mysqli_connect_errno())
	{	
		die('Could not connect: ' . mysqli_connect_error());
	}
	$sql = "SELECT * from mytable where src_name='$Source' AND dest_name='$Destination' AND bus_isAC='$isAC' AND bus_isSlpr='$isSleeper';";
	$retval = mysqli_query($conn, $sql) or die ('Error1');
	//Computing upper and lower bounds for fare,travel time and available seats	
	$maxTime = 1;
	$minTime = 500000;
	$maxFare = 1;
	$minFare = 500000;
	$maxSeat = 1;
	$minSeat = 500000;
	$maxRating = 1.0;
	while($row = mysqli_fetch_array($retval, MYSQLI_ASSOC))
	{
	 	$maxTime = max($maxTime,$row['bus_duration']);
		$minTime = min($minTime,$row['bus_duration']);
	
		$maxFare = max($maxFare,$row['bus_fare']);
		$minFare = min($minFare,$row['bus_fare']);
		$maxSeat = max($maxSeat,$row['available_seat']);
		$minSeat = min($minSeat,$row['available_seat']);
		
		$maxRating = max($maxRating,$row['bus_rating']);
	} 
	$arr=array();
	//Computing U and adding it to the array, $arr
	$sql = "SELECT * from mytable where src_name='$Source' AND dest_name='$Destination' AND bus_isAC='$isAC' AND bus_isSlpr='$isSleeper';";
	$retval = mysqli_query($conn, $sql) or die ('Error2');
	while($row = mysqli_fetch_array($retval, MYSQLI_ASSOC))
	{
	 	$normTime = ($row['bus_duration'] - $maxTime)/($maxTime - $minTime);
		$normFare = ($row['bus_fare'] - $maxFare)/($maxFare - $minFare);
		$normSeat = ($row['bus_duration'] - $maxSeat)/($maxSeat - $minSeat);
		$normRating = $row['bus_rating']/$maxRating;
		$U = (11 - $row['bus_duration'])*1000*$normTime + $row['bus_fare']*$normFare + (1/$row['bus_rating']*$normRating);
		$U += $row['available_seat']*$normSeat;
		$arr[$row['bus_routeid']]=$U;
	}
	krsort($arr);
    	$key = $value = NULL;
    	$i=0;
    //Displaying top 3 results
    	foreach ($arr as $key => $value) {
        //echo "$key = $value\n";
    	$sql = "SELECT operator,src_name,dest_name,bus_starttime,bus_endtime,bus_fare,bus_isAc,bus_isNAc,bus_isSlpr FROM mytable WHERE bus_routeid = '$key';";
        $retval = mysqli_query($conn, $sql) or die ('Error');
        $row = mysqli_fetch_array($retval, MYSQLI_ASSOC) ;
        echo $row['operator'].'|'.$row['src_name'].'|'.$row['dest_name'].'|'.$row['bus_starttime'].'|'.$row['bus_endtime'].'|'.$row['bus_fare'];
        if($row['bus_isSlpr']=='true') print 'Sleeper | ';
        if($row['bus_isNAc']=='true') echo 'Non-AC';
        else echo 'AC';
        echo '--------------------------------------------------------------------';
        $i=$i+1;
        if($i >= 3)
            break;
		}
	//Freeing result and closing the connection
	mysqli_free_result($retval);
	mysqli_close($conn);
?>
</html>
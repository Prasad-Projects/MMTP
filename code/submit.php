<html>
<h2>Result</h2>
<?php
	//Storing the variables passed from main page
	$Source = $_POST['Source'];
	$Destination = $_POST['Destination'];
	$isAC = $_POST['isAC'];
	$isSleeper = $_POST['isSleeper'];
	$costScale = (int)$_POST['costScale'];
	$timeScale = (int)$_POST['timeScale'];
	$seatScale = (int)$_POST['seatScale'];
	
	//Connection to database
	$dbhost = '127.0.0.1';
	$dbuser = 'root';
	$dbpass = 'password';
	$dbname = 'MMTP'
	$conn = mysql_connect($dbhost, $dbuser, $dbpass, $dbname);
	if(! $conn )
	{	
		die('Could not connect: ' . mysql_error());
	}
	$sql = 'SELECT * from mytable where src_name=$Source AND dest_name=$Destination AND isAC=$isAC '.
		'AND isSlpr=$isSleeper;'
	$retval = mysql_query( $sql, $conn );
	
	//Computing upper and lower bounds for fare,travel time and available seats	
	$maxtime = 0;
	$mintime = 500000;
	$maxFare = 0;
	$minFare = 500000;
	$maxSeat = 0;
	$minSeat = 500000;
	$maxRating = 0.0;
	while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
	{
	 	$maxTime = max($maxTime,$row['bus_duration']);
		$minTime = min($minTime,$row['bus_duration']);
	
		$maxFare = max($maxFare,$row['bus_fare']);
		$minFare = min($minFare,$row['bus_fare']);

		$maxSeat = max($maxSeat,$row['available_seat']);
		$minSeat = min($minSeat,$row['available_seat']);
		
		$maxRating = max($maxRating,$row['bus_rating']);
	} 
	
	//Computing U
	$sql = 'SELECT * from mytable where src_name=$Source AND dest_name=$Destination AND isAC=$isAC '.
		'AND isSlpr=$isSleeper;'
	$retval = mysql_query( $sql, $conn );
	while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
	{
	 	$normTime = ($row['bus_duration'] - $maxTime)/($maxTime - $minTime);
		$normFare = ($row['bus_fare'] - $maxFare)/($maxFare - $minFare);
		$normSeat = ($row['bus_duration'] - $maxSeat)/($maxSeat - $minSeat);
		$normRating = $row['bus_rating']/$maxRating;
		$U = (11 - $row['bus_duration'])*1000*$normTime + $row['bus_fare']*$normFare + (1/$row['bus_rating']*$normRating);
		$U += $row['available_seat']*$normSeat;
	}
	mysql_close($conn); 
?>
</html>
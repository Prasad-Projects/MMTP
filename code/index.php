<!DOCTYPE html> 
<html>
	

<head>

<script>

function updateVar10(){
	var elem9 = document.getElementById("rat2");
	elem9.value = "10";
    }
function updateVar9(){
	var elem9 = document.getElementById("rat2");
	elem9.value = "9";
    }

function updateVar8(){
	var elem8 = document.getElementById("rat2");
	elem8.value = "8";
    }


function updateVar7(){
	var elem7 = document.getElementById("rat2");
	elem7.value = "7";
    }


function updateVar6(){
	var elem6 = document.getElementById("rat2");
	elem6.value = "6";
    }


function updateVar5(){
	var elem5 = document.getElementById("rat2");
	elem5.value = "5";
    }


function updateVar4(){
	var elem4 = document.getElementById("rat2");
	elem4.value = "4";
    }


function updateVar3(){
	var elem3 = document.getElementById("rat2");
	elem3.value = "3";
    }

function updateVar2(){
	var elem2 = document.getElementById("rat2");
	elem2.value = "2";
    }

function updateVar1(){
	var elem1 = document.getElementById("rat2");
	elem1.value = "1";
    }

</script>

<style>

#exec1 {
    width: 100%;
    height: 100%;
    background-color: #E9E581;
    color:#2B2B2B;
    position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
}


.spinner {
  color:#2B2B2B;
  margin:auto;
  width: 32px;
  height: 32px;
  position: absolute;
    top:0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
}

.cube1, .cube2 {
  background-color: #333;
  width: 10px;
  height: 10px;
  position: absolute;
  top: 0;
  left: 0;
 margin:auto;
  -webkit-animation: cubemove 1.8s infinite ease-in-out;
  animation: cubemove 1.8s infinite ease-in-out;
}

.cube2 {
  -webkit-animation-delay: -0.9s;
  animation-delay: -0.9s;
}

@-webkit-keyframes cubemove {
  25% { -webkit-transform: translateX(42px) rotate(-90deg) scale(0.5) }
  50% { -webkit-transform: translateX(42px) translateY(42px) rotate(-180deg) }
  75% { -webkit-transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5) }
  100% { -webkit-transform: rotate(-360deg) }
}

@keyframes cubemove {
  25% { 
    transform: translateX(42px) rotate(-90deg) scale(0.5);
    -webkit-transform: translateX(42px) rotate(-90deg) scale(0.5);
  } 50% { 
    transform: translateX(42px) translateY(42px) rotate(-179deg);
    -webkit-transform: translateX(42px) translateY(42px) rotate(-179deg);
  } 50.1% { 
    transform: translateX(42px) translateY(42px) rotate(-180deg);
    -webkit-transform: translateX(42px) translateY(42px) rotate(-180deg);
  } 75% { 
    transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5);
    -webkit-transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5);
  } 100% { 
    transform: rotate(-360deg);
    -webkit-transform: rotate(-360deg);
  }
}
</style>

<script>
/*
$('#myButton').click(function() {
  $('#exec1').toggle('slow', function() {
    // Animation complete.
  });
});
*/

function loadXMLDoc()
{
$("#exec1").show("slow");
};

</script>
		<link href="http://fonts.googleapis.com/css?family=Dancing+Script" rel="stylesheet" type="text/css">
		<link href="http://fonts.googleapis.com/css?family=Josefin+Sans" rel="stylesheet" type="text/css">

		<title>Multi Modal Trip Planner</title><br>

		<center><!--<img src="logo.png" style="width: 7%; height: 7%" alt="">--><h1 style="font-family: 'Dancing Script', Georgia, Times, serif;
    font-size: 39px;
    color: #FFFFFC;text-shadow: 2px 1px 0 rgba(0.2,0,0,0.2);
    line-height: 0px;">Multi Modal Trip Planner</h1></center>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
		
		<link rel="stylesheet" href="css/demo.css">
		<link rel="stylesheet" href="css/sky-forms.css">
		<link href="http://fonts.googleapis.com/css?family=Goudy+Bookletter+1911" rel="stylesheet" type="text/css">
		<!--[if lt IE 9]>
			<link rel="stylesheet" href="css/sky-forms-ie8.css">
		<![endif]-->
		
		<!--[if lt IE 10]>
			<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
			<script src="js/jquery.placeholder.min.js"></script>
		<![endif]-->		
		<!--[if lt IE 9]>
			<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
			<script src="js/sky-forms-ie8.js"></script>
		<![endif]-->
	</head>
	<body class="bg-blue" style="font-size:19px;">
	<div id="exec1" style="display:none;">
	<div class="spinner">
	  	<div class="cube1"></div>
	  	<div class="cube2"></div>
	</div><br><br><br><br><br><br><br><br><br>
<p><center><b>Executing the Map-Reduce Job</b></center></p>
</div>
		<div class="body">			
		
			<!-- Blue color scheme -->
			<form action="submit.php" method="post" class="sky-form">
				<header style="background: rgba(112,212,173,.7); color:white;"><center>Preference Form</center></header>
				
				<fieldset style="background: rgba(225,235,255,.9);">
					
					<section>
						<label class="label">Source</label>
						<label class="input">
							<input type="text" list="list"  name="src">
							<datalist id="list">
								<option value="Delhi"></option>
								<option value="Dadar"></option>
								<option value="Chennai"></option>
								<option value="Goa"></option>
								<option value="Mumbai"></option>
								<option value="Bangalore"></option>
								<option value="Hyderabad"></option>
								<option value="Visakhapatnam"></option>
							</datalist>
						</label>
						<div class="note"><strong>Note:</strong> Select from AutoComplete.</div>
					</section>
					<section>
						<label class="label">Destination</label>
						<label class="input">
							<input type="text" list="list" name="dest">
							<datalist id="list">
								<option value="Delhi"></option>
								<option value="Chennai"></option>
								<option value="Dadar"></option>
								<option value="Chandigarh"></option>
								<option value="Goa"></option>
								<option value="Mumbai"></option>
								<option value="Bangalore"></option>
								<option value="Hyderabad"></option>
								<option value="Mumbai"></option>
								<option value="Visakhapatnam"></option>
							</datalist>
						</label>
					</section>
				</fieldset>
				
				<fieldset style="background: rgba(225,235,255,.9);">
					<section>
						<label class="label">Low-Fare Preference</label>
						<label class="select">
							<select name="fare">
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>
								<option value="6">6</option>
								<option value="7">7</option>
								<option value="8">8</option>
								<option value="9">9</option>					
							</select>
							<i></i>
						</label>
					</section>
					
				</fieldset>
			
				<fieldset style="background: rgba(225,235,255,.9);">
					<section>
						<label class="label">Travel-Time Preference</label>
						<label class="select">
							<select name="time">
								<option value="1">1</option>
								<option value="2">2</option>
								<option value="3">3</option>
								<option value="4">4</option>
								<option value="5">5</option>
								<option value="6">6</option>
								<option value="7">7</option>
								<option value="8">8</option>
								<option value="9">9</option>					
							</select>
							<i></i>
						</label>
					<div class="note"><strong>Note:</strong> On a scale of 1-10 your preference to reach the earliest a the expense of other preferences.</div>
					</section>
					
				</fieldset>
				
				<fieldset style="background: rgba(225,235,255,.9);">
					<section>
						<label class="label">Seat-Availability Preference</label>
						<div class="row">
							<div class="col col-4">
								<label class="radio"><input type="radio" name="seat" value="1" checked><i></i>1</label>
								<label class="radio"><input type="radio" name="seat" value="2"><i></i>2</label>
								<label class="radio"><input type="radio" name="seat" value="3"><i></i>3</label>
							</div>
							<div class="col col-4">
								<label class="radio"><input type="radio" name="seat" value="4"><i></i>4</label>
								<label class="radio"><input type="radio" name="seat" value="5"><i></i>5</label>
								<label class="radio"><input type="radio" name="seat" value="6"><i></i>6</label>
							</div>
							<div class="col col-4">
								<label class="radio"><input type="radio" name="seat" value="7"><i></i>7</label>
								<label class="radio"><input type="radio" name="seat" value="8"><i></i>8</label>
								<label class="radio"><input type="radio" name="seat" value="9"><i></i>9</label>
							</div>
						</div>						
					</section>
					
				</fieldset>
				
				<fieldset style="background: rgba(225,235,255,.9);">
					<div class="row">
					
						
						<section class="col col-5">				
							<label class="label">Type-Preference</label>
							<br/>
							<label>Air Conditioned</label> &nbsp;&nbsp;&nbsp;<input type="checkbox" name="isAC" checked="checked" id="AC"/>
							<br/>
							<br/>
							<label>Sleeper</label>&nbsp; &nbsp; &nbsp; <input type="checkbox" name="isSleeper" id="SLPR"/>
						</section>
					</div>
				</fieldset>
				
				
				
				<footer style="background: rgba(225,235,255,.9);">
					<input type="submit" value="submit job" class="button" id="myButton">
					<button type="button" class="button button-secondary" onclick="window.history.back();">Back</button>
				</footer>
				<input type="hidden" id="rat2" name="rating_val" value="yoyoyo">
			</form>
			<center><img src="logo.gif" style="width: 30%; height: 20%; margin-top:10%;"></center>
			<!--/ Blue color scheme -->	
<br><br>		

		</div>

	</body>
<!-- Mirrored from voky.com.ua/showcase/sky-forms/examples/scheme-cyan.html by HTTrack Website Copier/3.x [XR&CO'2013], Thu, 27 Mar 2014 07:30:36 GMT -->
</html>

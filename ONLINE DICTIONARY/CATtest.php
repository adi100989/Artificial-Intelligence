<html>
<head>
<link href="act9_css.css" type="text/css" rel="stylesheet" />
<style type="text/css">
#clock { font-family: Arial, Helvetica, sans-serif; font-size: 0.8em; color: white; background-color: black; border: 2px solid purple; padding: 4px; }
</style>
<style type="text/css">

div.scroll_content {
height: 362px;
width: 782px;
overflow: auto;
border: 1px solid #666;
background-color: #ccc;
padding: 8px;
}
div.scroll_right {
height: 371px;
width: 259px;
overflow: auto;
border: 1px solid #666;
padding: 3px;
}
</style> 

<script type="text/javascript">
<!--

function init ( )
{
  timeDisplay = document.createTextNode ( "" );
  document.getElementById("clock").appendChild ( timeDisplay );
}

function updateClock ( )
{
  var currentTime = new Date ( );

  var currentHours = currentTime.getHours ( );
  var currentMinutes = currentTime.getMinutes ( );
  var currentSeconds = currentTime.getSeconds ( );

  // Pad the minutes and seconds with leading zeros, if required
  currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;
  currentSeconds = ( currentSeconds < 10 ? "0" : "" ) + currentSeconds;

  // Choose either "AM" or "PM" as appropriate
  var timeOfDay = ( currentHours < 12 ) ? "AM" : "PM";

  // Convert the hours component to 12-hour format if needed
  currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;

  // Convert an hours component of "0" to "12"
  currentHours = ( currentHours == 0 ) ? 12 : currentHours;

  // Compose the string for display
  var currentTimeString = currentHours + ":" + currentMinutes + ":" + currentSeconds + " " + timeOfDay;

  // Update the time display
  document.getElementById("clock").firstChild.nodeValue = currentTimeString;
}

// -->
</script>
</head>
<body onload="updateClock(); setInterval('updateClock()', 1000 )">

<div id="container">
<div id="lefthead">
<img src="extra/law-dictionary-roger.jpg" style="width:200px; height:120px"/>
</div>

  <div id="header">
    <b><h1>The Online Dictionary</h1>
   <h2> OnlineDictionary.com </h2> </b>
  </div>

<div id="rightheadtop">
<div style="width: 10em; text-align:center; margin: 20px auto;">
  <span id="clock">&nbsp;</span></div> 
</div>
<div id="rightheaddown">
<br /><form action="http://www.google.com/search.aspx" method="get" name="frmsearch">
<input type="text" value="" size="30px" name="searchbox" >
<center><input type="submit" value="search this site" name="search" /></center></form>
</div>
          <div id="menu">
<ul><center>  
  <li><a href="home.html">HOME</a>
    <ul>
      <li><a href="about_us.html">ABOUT US</a></li>
      <li><a href="contact.html">Contact Us</a></li>
      <li><a href="user_manual.html">User Manual</a></li>
    </ul>
    </li>


  <li><a href="#nogo">FACILITIES</a>
    <ul>
      <li><a href="dictionary.html">Browse The Dictionary</a></li>
      <li><a href="thesaurus.html">Thesaurus</a></li>
    </ul>
    </li>



  <li><a href="#nogo">TEST</a>
    <ul>
      <li><a href="sat.html">SAT</a></li>
      <li><a href="toefl">TOEFL</a></li>
      <li><a href="mba.html">MBA</a></li>
    </ul>
    </li>

<li><a href="#nogo">REFERENCES</a>
<ul>
<li><a href="database.html">Database source</a></li>
<li><a href="Word_builder.html">Word Builder Sources</a></li>

</ul>
</li>
<li><a href="#nogo">LINK</a>
<ul>
<li><a href="wordoftheday.html">Word Of The Day</a></li>
</ul>
</li></center>  
</ul> 
</div>
      
  <div id="leftBar">
<table name="lefttable" border="2" height="380px" width="269px" cellpadding="3"  >
<tr><td> <b><u>QUOTE OF THE DAY </u></b>
<BR />
My philosophy is that not only are you responsible for your life, but doing the best at this moment puts you in the best place for the next moment.
        Oprah Winfrey (1954 - )</td>
</tr>
   
<tr><td><u><b> WORD OF THE DAY</b></u><br />
equipoise
<br />


1. equality in distribution of weight, balance, or force; equilibrium: "They spent more than ten minutes shuffling items between their grocery bags to ensure equipoise for the long walk home."
<br />
2. an offsetting force or weight; counterpoise</td>
</tr>

<tr><td> <script LANGUAGE="javascript">
var mydate=new Date()
var year=mydate.getYear()
if (year < 1000)
year+=1900
var day=mydate.getDay()
var month=mydate.getMonth()
var daym=mydate.getDate()
if (daym<10)
daym="0"+daym
var dayarray=new Array("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
var montharray=new Array("January","February","March","April","May","June","July","August","September","October","November","December")
document.write("<small><font color='000000' face='Arial'><b>"+dayarray[day]+", "+montharray[month]+" "+daym+", "+year+"</b></font></small>")

</script><br /> <br /></td>
</tr>
</table>
</div>


  <div id="content">
 <div class="scroll_content">

       


<?php

if(!(isset($_SESSION['session_id'])=='user1'))
{
session_start();
//echo "checking details in CATtest.php in !issset()";
//print_r($_SESSION);

echo"\n";
$exam=$_SESSION['session_exam_type'];
$difficulty=$_SESSION['session_level'];

echo "\n";

echo "$difficulty      .....   $exam";
//$session_id=$_POST['username'];
//$exam=$_POST['exam'];
//$difficulty=$_POST['difficulty'];
//$_SESSION['session_exam_type']=$exam;
//$_SESSION['session_level']=$difficulty;
} 
else {
$exam=$_SESSION['session_exam_type'];
$difficulty=$_SESSION['session_level'];
}

       
     //   echo "the exam type chosen is $exam  and the dificulty level is  $difficulty";

$connection=mysql_connect("localhost","root","") or die(mysql_error());
$db=mysql_select_db("dictionary",$connection) or die(mysql_error());

$count=1;   

//while($count<=10)
//{
//$q=$_SESSION['session_ques_no']++;
$q1="select * from word_builder where level='$difficulty' and exam_type='$exam' ";
$res=mysql_query($q1) or die("can't display question");
while($rows=mysql_fetch_array($res))
{
  extract($rows);
  echo " <form method='post' action='CATtest_validate.php'>"; 
  echo " <table border='2' width='400' >";  // LINE20 
  echo " <tr><td colspan='2' ><input type='text' name='ques_no' value='$ques_no'/></td><tr>"; 
  echo " <tr><td colspan='2' >$question </td><tr>"; 
  echo " <tr><td><input type='radio' name='answer' value='option_a' /></td><td>$option_a</td></tr>"; 
  echo " <tr><td><input type='radio' name='answer' value='option_b' /></td><td>$option_b</td></tr>"; 
  echo " <tr><td><input type='radio' name='answer' value='option_c' /></td><td>$option_c</td></tr>"; 
  echo "<tr><td><input type='radio' name='answer' value='option_d' /></td><td>$option_d</td></tr>"; 
  echo "<tr><right><td colspan='2'><input type='submit' name='submit' value='submit' /></td></right></tr>"; 
  echo"</table>"; 
  echo"  </form>"; 
  break;
}
$count++;  


?>








 </div> 
  </div>
  <div id="rightBar">
<div class="scroll_right">
   <b> <h3><b> <u><center>SERVICES:</center></u></b> </h3> 	
 <hr />
 <h4><ul>
<li><a href="subscribe.html">SUBSCRIBE </a> </li> <br />
<li><a href="subscribe.html">FAVORITE LIST </a> </li> <br />
<li><a href="subscribe.html">MOST COMMON WORDS </a> </li> <br />
<li><a href="subscribe.html">FEEDBACK </a> </li> <br />
<li><a href="subscribe.html">CONTRIBUTIONS </a> </li> <br />
</UL></h4></div></div>
  <div id="footer" style="text-align:center">
<br />
<div id="br">    <h1>Browse The Web...
<a href="a.html" target="browse.html"> A   </a>
<a href="b.html" target="browse.html"> B   </a>
<a href="c.html" target="browse.html"> C   </a>
<a href="d.html" target="browse.html"> D   </a>
<a href="e.html" target="browse.html"> E   </a>
<a href="f.html" target="browse.html"> F   </a>
<a href="g.html" target="browse.html"> G   </a>
<a href="h.html" target="browse.html"> H   </a>
<a href="i.html" target="browse.html"> I   </a>
<a href="j.html" target="browse.html"> J   </a>
<a href="k.html" target="browse.html"> K   </a>
<a href="l.html" target="browse.html"> L   </a>
<a href="m.html" target="browse.html"> M   </a>
<a href="n.html" target="browse.html"> N   </a>
<a href="o.html" target="browse.html"> O   </a>
<a href="p.html" target="browse.html"> P   </a>
<a href="q.html" target="browse.html"> Q   </a>
<a href="r.html" target="browse.html"> R   </a>
<a href="s.html" target="browse.html"> S   </a>
<a href="t.html" target="browse.html"> T   </a>
<a href="u.html" target="browse.html"> U   </a>
<a href="v.html" target="browse.html"> V   </a>
<a href="w.html" target="browse.html"> W   </a>
<a href="x.html" target="browse.html"> X   </a>
<a href="y.html" target="browse.html"> Y   </a>
<a href="z.html" target="browse.html"> Z   </a>
</h1>
</div>
</div>
</div>
</body>
</html>
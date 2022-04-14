<?php
include "config.php";

$userid = 0;
if(isset($_POST['userid'])){
   $userid = mysqli_real_escape_string($con,$_POST['userid']);
}
$sql = "select names from person".$userid;
$result = mysqli_query($con,$sql);

$response = "<table border='0' width='100%'>";
while( $row = mysqli_fetch_array($result) ){
 $id = $row['id'];
 $names = $row['names'];
 $department = $row['department'];
 $designation = $row['designation'];
 $device = $row['device'];
 $otherDevice = $row['otherDevice'];
 $email = $row['email'];
 $macadd= $row['macadd'];
 $phoneNum = $row['phoneNum'];
 $facultyName = $row['facultyName'];
 
 $response .= "<tr>";
 $response .= "<td>Name : </td><td>".$names."</td>";
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>Salary : </td><td>".$department."</td>";
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>Gender : </td><td>".$designation."</td>";
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>City : </td><td>".$device."</td>";
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>City : </td><td>".$otherDevice."</td>";
 $response .= "</tr>";

 $response .= "<tr>"; 
 $response .= "<td>Email : </td><td>".$email."</td>"; 
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>City : </td><td>".$macadd."</td>";
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>City : </td><td>".$phoneNum."</td>";
 $response .= "</tr>";

 $response .= "<tr>";
 $response .= "<td>City : </td><td>".$facultyName."</td>";
 $response .= "</tr>";
}
$response .= "</table>";

echo $response;
exit;
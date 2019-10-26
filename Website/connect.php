<?php
    //connection
    $host = "sensordb.ctvaewxubied.us-east-2.rds.amazonaws.com:3306";
    $dbuser = "admin";
    $dbpassword = "nameless";
    $dbname = "testDB";

    $conn = new mysqli($host, $dbuser, $dbpassword, $dbname);


 if ($conn->connect_error){
   die("Connection failed: " . $conn->connect_error);
 }
 
     $acomment = $_POST['comment'];
    $sql = "INSERT INTO comments(comment)
    VALUES ('$acomment')";
  if($conn->query($sql) === TRUE){
    echo "NEW RECORD";
  }

 echo "Connected Successfully";

?>
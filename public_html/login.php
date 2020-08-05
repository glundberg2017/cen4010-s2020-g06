<?php
require_once './php/db_connect.php';
    
$id=$_POST['id'] ??'';
$email=$_POST['email'] ??'';
$password=$_POST['password'] ??'';

//login
if(isset($_POST['email']) && isset($_POST['password'])){

  // check if the user is already in the db
  $result = $db->query("SELECT id from users where email='$email'");
  if ($result->num_rows < 1)
  {
    $insertStmt = "INSERT INTO users (id,email,password) VALUES ('$id','$email', '$password')";
    $db->query($insertStmt);
  }

  // return the users id
  $result = $db->query("SELECT id from users where email='$email'");
  
  if ($result->num_rows > 0 ){
      $row = $result->fetch_assoc();
      echo $row["id"];
  }
  else {
    echo "-1";
  }
}
    
$db->close()
?>
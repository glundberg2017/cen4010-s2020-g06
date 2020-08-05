<?php
  require_once './php/db_connect.php';
    
    ?>

  
 <form style=text-align:center method="post">
    <p>
      <input type="text" name="email" id="email" />
        <input type="text" name="password" id="password" />
        <br>
        <br>
      <input type="submit" name ="first" id="submit" value="submit" />
      
    </p>
  </form>


<?php
    $id=$_POST['id'] ??'';
    $email=$_POST['email'] ??'';
    $password=$_POST['password'] ??'';
//login
    if(isset($_POST['email']) &&isset($_POST['password'])){
     $insertStmt = "INSERT INTO users (id,email,password) VALUES ('$id',' $email', '$password')";
        $db->query($insertStmt); 
        }
       
        
     
    
  
?>


<?php 
     $db->close() ?>
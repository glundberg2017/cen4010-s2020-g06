<?php
  require_once './php/db_connect.php';
    
    ?>
<table>
    
    
    
    
<?php
    $sender_id=$_POST['sender_id'] ??'';
     $recipient_id=$_POST['recipient_id'] ??'';
     $message=$_POST['message'] ??'';
    $timestamp=$_POST['timestamp'] ??'';
//login
    if(isset($_POST['sender_id']) &&isset($_POST['recipient_id'])&&isset($_POST['message'])){
     $insertStmt = "INSERT INTO messsages (timestamp,sender_id,recipient_id,message) VALUES ('$timestamp',' $sender_id', '$recipient_id','$message')";
    $db->query($insertStmt); 
        }
       
        ?>
    
    <?php 
     $db->close() ?>
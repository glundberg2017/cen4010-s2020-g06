<?php
  require_once './php/db_connect.php';
 
    $id1=$_POST['id1'] ??'';;
    $id2=$_POST['id2'] ??'';;
    $sql="SELECT message FROM messages WHERE(sender_id='$id1' or sender_id='$id2') AND (recipient_id='$id1' or recipient_id='$id2') order by timestamp";
    $result= $db->query($sql);
    
    if($result-> num_rows > 0 ){
        while($row=$result->fetch_assoc()){
            echo $row["message"] ."\n";
        }
    }
    else{
        echo "No chat history with this user";
    }
    
?>
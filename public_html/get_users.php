<?php
  require_once './php/db_connect.php';
    
    ?>
<table>
<?php
 
        
       
      $sql="SELECT id,email FROM users ORDER BY`id`DESC LIMIT 10";
    $result= $db->query($sql);
    
    if($result-> num_rows > 0 ){
        while($row=$result->fetch_assoc()){
            echo "<tr><td>" . $row["id"] ."</td><td>" .$row["email"]."</td><td>";
        }
        echo "</table>";
    }
    else{
        echo"0 result";
    }
    
    
    
?>

<?php 
     $db->close() ?>
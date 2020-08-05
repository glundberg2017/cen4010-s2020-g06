<?php
    require_once './php/db_connect.php';

    $id=$_POST['id'] ??'';

    $sql="SELECT id,email FROM users WHERE id<>$id ORDER BY`id`DESC";
    $result = $db->query($sql);

    if ($result->num_rows > 0 ){
        while($row=$result->fetch_assoc()){
            //echo "<tr><td>" . $row["id"] ."</td><td>" .$row["email"]."</td><td>";
            echo $row["id"] ."|". $row["email"] ."||";
        }
    }

    $db->close();
?>
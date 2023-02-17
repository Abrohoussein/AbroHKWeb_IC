<?php       
     $ressource = fopen('data.txt', 'rb');
     echo fread($ressource, filesize('data.txt'));        
     foreach ($ressource as $value){
         print($value);
     }
?>

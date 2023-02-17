<?php       
     $ressource = fopen('data.txt', 'rb');
     echo fread($ressource, filesize('data.txt'));        
?>

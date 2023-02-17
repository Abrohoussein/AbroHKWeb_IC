<?php       
     $ressource = fopen('test.txt', 'rb');
     echo fread($ressource, filesize('test.txt'));        
?>

<?php
echo '<div align="center"><font face="arial" size="5" color="grey"> Bonjour le monde !</font><br /> ';
echo '<img src="el.png" border="0" /></div> ';
$ressource = fopen('data.txt', 'rb');
echo fread($ressource, filesize('data.txt'));
?>

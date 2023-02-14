<?php
echo '<div align="center"><font face="arial" size="5" color="grey"> Bonjour le monde !</font><br /> ';
echo '<img src="el.png" border="0" /></div> ';
$ressource = fopen('data.txt', 'rb');
$_PUT = array();
parse_str(file_get_contents($ressource), $_PUT);
foreach ($_PUT as $key => $value)
  {
    echo $key . " : " . $value;
  }
?>

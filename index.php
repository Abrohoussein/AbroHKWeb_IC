<?php
echo '<div align="center"><font face="arial" size="5" color="grey"> Bonjour le monde !</font><br /> ';
echo '<img src="el.png" border="0" /></div> ';
$ressource = fopen('data.txt', 'rb');
$_PUT = array();
parse_str(file_get_contents("http://localhost/dolibarr/api/index.php/products?DOLAPIKEY=abr99&sortfield=t.ref&sortorder=ASC&limit=100"), $_PUT);
foreach ($_PUT as $key => $value)
  {
    echo $key . " : " . $value;
    echo '<div align="center"><font face="arial" size="5" color="grey"> $key . " : " . $value</font><br /> ';
  }
?>

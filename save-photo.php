<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $photoData = $_POST['photoData'];
  
  // Chemin du fichier de destination
  $filePath = 'capturetmp.jpg';

  // Enregistrer la photo sur le serveur
  if (file_put_contents($filePath, base64_decode(preg_replace('#^data:image/\w+;base64,#i', '', $photoData)))) {
    echo 'La photo a été enregistrée avec succès sur le serveur.';
  } else {
    echo 'Erreur lors de l\'enregistrement de la photo sur le serveur.';
  }
}
?>

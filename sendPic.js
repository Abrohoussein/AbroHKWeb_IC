// Accéder à la vidéo de la caméra
const video = document.getElementById('video');

// Accéder au bouton de capture de photo
const captureBtn = document.getElementById('capture-btn');

// Accéder au bouton d'analyse de photo
const processBtn = document.getElementById('process-btn');

// Accéder au canvas pour afficher la photo capturée
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

// Variable pour stocker la photo capturée
let capturedPhoto = null;

// Obtenir l'accès à la caméra
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    // Afficher la vidéo de la caméra dans l'élément vidéo
    video.srcObject = stream;
  })
  .catch(function(error) {
    console.log('Erreur lors de l\'accès à la caméra :', error);
  });

// Fonction pour capturer une photo
function capturePhoto() {
  // Dessiner la vidéo sur le canvas
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  
  // Obtenir la photo sous forme de base64
  const photoData = canvas.toDataURL('image/jpeg');
  
  // Stocker la photo capturée dans la variable
  capturedPhoto = photoData;
  
  // Afficher la photo capturée dans le canvas
  const img = new Image();
  img.onload = function() {
    context.clearRect(0, 0, canvas.width, canvas.height); // Effacer le contenu précédent du canvas
    context.drawImage(img, 0, 0, canvas.width, canvas.height); // Dessiner la nouvelle photo capturée
  };
  img.src = photoData;

  // Obtenir la photo sous forme de base64
  const photoSave = canvas.toDataURL('image/jpeg').replace(/^data:image\/jpeg;base64,/, '');

  // Écrire les données de la photo dans le fichier "photo.jpg"
  fs.writeFile('photo.jpg', photoSave, 'base64', function(err) {
    if (err) {
      console.log('Erreur lors de l\'écriture du fichier :', err);
    } else {
      console.log('Photo capturée et enregistrée avec succès dans "photo.jpg"');
    }
  });
}

// Fonction pour analyser la photo
function processPhoto() {
  // Vérifier si une photo a été capturée
  if (capturedPhoto === null) {
    console.log('Aucune photo capturée.');
    return;
  }
  
  // Construction de la commande pour exécuter le script Python avec la photo en entrée
  const command = `python main.py ${capturedPhoto}`;
  
  // Exécution du script Python avec la photo en entrée
  const { exec } = require('child_process');
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Erreur d'exécution du script Python : ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Erreur de sortie du script Python : ${stderr}`);
      return;
    }
    
    // Récupérer le résultat de la prédiction depuis stdout (à adapter en fonction de la sortie du script Python)
    const predictionResult = stdout;
    
    // Créer un objet contenant le résultat de la prédiction
    const predictionData = {
      prediction: predictionResult
    };
    
    // Convertir l'objet en chaîne JSON
    const predictionJSON = JSON.stringify(predictionData);
    
    // Créer un lien de téléchargement pour le fichier JSON
    const blob = new Blob([predictionJSON], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'prediction.json';
    link.click();
  });
}

// Ajouter des écouteurs d'événement aux boutons
captureBtn.addEventListener('click', capturePhoto);
processBtn.addEventListener('click', processPhoto);


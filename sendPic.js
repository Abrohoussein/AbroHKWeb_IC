// Accéder à la vidéo de la caméra
const video = document.getElementById('video');

// Accéder au bouton de capture de photo
const captureBtn = document.getElementById('capture-btn');

// Accéder au canvas pour afficher la photo capturée
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

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
  
  // Envoyer la photo au serveur pour traitement (par exemple, en utilisant une requête AJAX)
  // ...
}

// Ajouter un gestionnaire d'événement au bouton de capture de photo
captureBtn.addEventListener('click', capturePhoto);

const fs = require('fs');

// ...

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
  const childProcess = exec(command, (error, stdout, stderr) => {
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

  // Rediriger les sorties de la console vers un fichier
  const errorFile = fs.createWriteStream('erreur.txt');
  childProcess.stdout.pipe(process.stdout);
  childProcess.stderr.pipe(errorFile);
}

// ...

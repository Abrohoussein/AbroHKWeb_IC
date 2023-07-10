import sys
import dlib
import json
import math
import joblib
import argparse
import PIL.Image
import numpy as np
from imutils import face_utils

def transform(image, face_locations):
    coord_faces = []
    for face in face_locations:
        rect = face.top(), face.right(), face.bottom(), face.left()
        coord_face = max(rect[0], 0), min(rect[1], image.shape[1]), min(rect[2], image.shape[0]), max(rect[3], 0)
        coord_faces.append(coord_face)
    return coord_faces

def encode_face(image):
    face_locations = face_detector(image, 1)

    landmarks_list = []
    for face_location in face_locations:

        shape = pose_predictor_68_point(image, face_location)

        shape = face_utils.shape_to_np(shape)
        landmarks_list.append(shape)

    return landmarks_list

def easy_face_reco(image):
    rgb_small_frame = np.array(image)[:, :, ::-1]
    landmarks_list = encode_face(rgb_small_frame)

    axe_x = []
    axe_y = []
    for shape in landmarks_list:
        for (x, y) in shape:
            axe_x.append(x)
            axe_y.append(y)

    # Union des coordonnées
    union_coord = axe_x + axe_y

    return union_coord

def enterImage(photo):

  image = PIL.Image.open(photo)
  image = image.convert('RGB')  # Convertir l'image en format RGB
  image_array = np.array(image)
  face_encodings = encode_face(image_array.astype('uint8'))

  return face_encodings

# Récupérer le nom du fichier à partir des arguments de ligne de commande
if len(sys.argv) < 2:
    print("Veuillez spécifier le nom du fichier en tant qu'argument.")
    sys.exit(1)
    
def calculer_angle(point1, point2, point3):
    # Vecteurs entre les points
    vecteur1 = (point1[0] - point2[0], point1[1] - point2[1])
    vecteur2 = (point3[0] - point2[0], point3[1] - point2[1])

    # Calcul du produit scalaire
    produit_scalaire = vecteur1[0] * vecteur2[0] + vecteur1[1] * vecteur2[1]

    # Calcul des normes des vecteurs
    norme1 = math.sqrt(vecteur1[0] ** 2 + vecteur1[1] ** 2)
    norme2 = math.sqrt(vecteur2[0] ** 2 + vecteur2[1] ** 2)

    # Calcul de l'angle en radians
    angle_radians = math.acos(produit_scalaire / (norme1 * norme2))

    # Conversion de l'angle en degrés
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

def parcourCoord(liste):
    
    angles_pertinents = [
        [7, 3, 19],
        [6, 2, 20],
        [5, 1, 21],
        [4, 18, 22],
        [3, 19, 23],
        [10, 7, 4],
        [9, 6, 3],
        [8, 5, 2],
        [11, 8, 6],
        [10, 7, 5],
        [9, 6, 4],
        [23, 26, 16],
        [24, 27, 15],
        [25, 17, 14],
        [26, 16, 13],
        [27, 15, 12],
        [7, 1, 22],
        [18, 27, 11],
        [15, 11, 7],
        [11, 7, 1]
    ]

    liste_points = []
    liste_angles = []
    for j in range (0,28):
      liste_points.append((liste[0][j]))
            
    for points in range (0,len(angles_pertinents)):
        p1 = liste_points[angles_pertinents[points][0]]
        p2 = liste_points[angles_pertinents[points][1]]
        p3 = liste_points[angles_pertinents[points][2]]
        liste_angles.append(calculer_angle(p1,p2,p3)) 

    return liste_angles

parser = argparse.ArgumentParser(description='Easy Facial Recognition App')
parser.add_argument('-i', '--input', type=str, required=True, help='directory of input known faces')

pose_predictor_68_point = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_detector = dlib.get_frontal_face_detector()

# nom_fichier = sys.argv[1]
nom_fichier = "vieux.jpg"
list_coord = enterImage(nom_fichier) 

angles = parcourCoord(list_coord)
# Charger le modèle à partir du fichier
loaded_model = joblib.load('model_RFC_62.pkl')


# Effectuer une prédiction sur les angles donnés
prediction = loaded_model.predict([angles])

prediction_json = json.dumps(prediction.tolist())

# Écrire les données JSON dans un fichier
with open('prediction.json', 'w') as file:
    file.write(prediction_json)
prediction

import cv2
import dlib
import PIL.Image
import numpy as np
from imutils import face_utils
import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Easy Facial Recognition App')
parser.add_argument('-i', '--input', type=str, required=True, help='directory of input known faces')

pose_predictor_68_point = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_detector = dlib.get_frontal_face_detector()


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
    
nom_fichier = sys.argv[1]
print(enterImage(nom_fichier))

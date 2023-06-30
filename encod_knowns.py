import face_recognition
import cv2
import os
import pickle

img_dir = "res/Sajad Kamali"

encodings = []
img_files = os.listdir(img_dir)

for img_name in img_files:
    img_file = os.path.join(img_dir, img_name)
    img = cv2.imread(img_file)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    locs = face_recognition.face_locations(rgb, model='hog')
    encods = face_recognition.face_encodings(rgb, locs)
    
    encodings.append(encods[0])

name = "Sajad Kamali"
with open('known_face.pickle', 'wb') as f:
	pickle.dump([name, encodings], f)

cv2.destroyAllWindows()

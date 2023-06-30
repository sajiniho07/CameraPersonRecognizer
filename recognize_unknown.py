import face_recognition
import cv2
import pickle

with open('res/known_face.pickle', 'rb') as f:
	name, encodings = pickle.load(f)
	
RED = (0, 0, 255)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame =  cv2.flip(frame, 1)
	
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locs = face_recognition.face_locations(rgb, model='hog')
        encods = face_recognition.face_encodings(rgb, locs)

        for (loc, encod) in zip(locs, encods):
            top_left = loc[3], loc[0]
            bottom_right = loc[1], loc[2]

            results = face_recognition.compare_faces(encodings, encod, 0.4)

            for res in results:
                if res:
                    desc = f"This is {name}"
                    cv2.putText(frame, desc, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 1)
                    break

            cv2.rectangle(frame, top_left, bottom_right, RED, 2)

        cv2.imshow("temp_frame", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()

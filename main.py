import os, json, pickle, time
# from datetime import datetime
print("Face Detection system started ...........")

import cv2
import cvzone
import numpy as np
import face_recognition

# # ---------- CONFIG ----------------------------------------------------------
BACKGROUND_PATH = 'Resources/background_4.png'
MODES_PATH      = 'Resources/Modes'
STUDENTS_FILE   = 'students.json'      # local DB
PROFILE_IMG_DIR = 'Images'             # local profile pictures
ATTENDANCE_COOLDOWN = 30               # seconds before re‑counting same face
# # ---------------------------------------------------------------------------

def load_students():
#     """Load local student database"""
    if not os.path.exists(STUDENTS_FILE):
        return {}
    with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_students(data):
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# # 1️⃣  Load encodings
# print("Loading encodings …")
# with open('EncodeFile.p', 'rb') as f:
#     encodeListKnown, studentIds = pickle.load(f)
# print("✔ Encodings ready")

# # 2️⃣  Load resources
imgBackground = cv2.imread(BACKGROUND_PATH)

mode_images = [cv2.imread(os.path.join(MODES_PATH, p))
               for p in sorted(os.listdir(MODES_PATH))]
# /
# # 3️⃣  Database in memory
students = load_students()

# # 4️⃣  Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

modeType, counter, current_id = 0, 0, None
imgStudent = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️  Camera frame not received"); break

#     # Small RGB copy for recognition
    small = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)[:, :, ::-1]

    face_locations = face_recognition.face_locations(small)
    face_encodings = face_recognition.face_encodings(small, face_locations)

#     # Draw live frame + mode panel onto background
    view = imgBackground.copy()
    view[162:162+480, 55:55+640] = frame
    view[44:44+633, 808:808+414] = mode_images[modeType]

    for enc, loc in zip(face_encodings, face_locations):
        matches  = face_recognition.compare_faces(encodeListKnown, enc)
        dists    = face_recognition.face_distance(encodeListKnown, enc)
        idx      = np.argmin(dists)

#         if matches[idx]:
#             y1,x2,y2,x1 = [v*4 for v in loc]     # rescale to full frame
#             bbox = 55+x1, 162+y1, x2-x1, y2-y1
#             cvzone.cornerRect(view, bbox, rt=0)

#             current_id = studentIds[idx]
#             if counter == 0:
#                 counter  = 1
#                 modeType = 1       # “Loading…” screen

#     # -----------------------------------------------------------------------
#     if counter:
#         if counter == 1 and current_id:
#             info = students.get(str(current_id))
#             if not info:          # unknown id in DB
#                 print(f"ID {current_id} not in students.json"); counter=0; modeType=0; continue

#             # Load profile pic once
#             img_path = os.path.join(PROFILE_IMG_DIR, f"{current_id}.png")
#             imgStudent = cv2.imread(img_path) if os.path.exists(img_path) else None

#             # Attendance logic
#             last_seen = datetime.strptime(info['last_attendance_time'],
#                                           "%Y-%m-%d %H:%M:%S")
#             elapsed = (datetime.now() - last_seen).total_seconds()
#             if elapsed > ATTENDANCE_COOLDOWN:
#                 info['total_attendance'] += 1
#                 info['last_attendance_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 save_students(students)        # persist change
#                 print(f"✔ Attendance +1 for {current_id} ({info['name']})")
#             else:
#                 modeType = 3      # “Already counted”
#                 counter  = 0

#         if modeType != 3:         # not blocked by cooldown
#             if 10 < counter < 20: modeType = 2

#             if counter <= 10 and imgStudent is not None:
#                 # Overlay statistics and photo
#                 cv2.putText(view, str(info['total_attendance']), (861,125),
#                             cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
#                 cv2.putText(view, info['major'],      (1006,550),
#                             cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),1)
#                 cv2.putText(view, str(current_id),    (1006,493),
#                             cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255),1)
#                 cv2.putText(view, info['standing'],   (910,625),
#                             cv2.FONT_HERSHEY_COMPLEX, 0.6, (100,100,100),1)
#                 cv2.putText(view, info['year'],       (1025,625),
#                             cv2.FONT_HERSHEY_COMPLEX, 0.6, (100,100,100),1)
#                 cv2.putText(view, info['starting_year'], (1125,625),
#                             cv2.FONT_HERSHEY_COMPLEX, 0.6, (100,100,100),1)

#                 (w,_),_ = cv2.getTextSize(info['name'], cv2.FONT_HERSHEY_COMPLEX,1,1)
#                 cv2.putText(view, info['name'], (808+(414-w)//2, 445),
#                             cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),1)

#                 view[175:175+216, 909:909+216] = cv2.resize(imgStudent,(216,216))

#             counter += 1
#             if counter >= 20:
#                 counter, modeType, current_id = 0, 0, None
#                 imgStudent = None
#     # -----------------------------------------------------------------------

#     cv2.imshow("Face Attendance (Offline)", view)
#     if cv2.waitKey(1) & 0xFF == 27:   # ESC to quit
#         break

# cap.release()
# cv2.destroyAllWindows()

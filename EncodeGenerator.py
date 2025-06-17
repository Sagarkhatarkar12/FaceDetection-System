# """
# Generate EncodeFile.p =  [encodeListKnown, studentIds]

# Folder layout (same level as this script):
# .
# ├─ EncodeGenerator.py
# ├─ Images/
# │   ├─ 101.png
# │   ├─ 102.jpg
# │   └─ …
# """

import os, cv2, face_recognition, numpy as np, pickle
import dlib

# # --------------------------------------------------------------------------
FOLDER_PATH      = "Images"            # where all student photos live
# ENCODINGS_PICKLE = "EncodeFile.p"      # output file

# # --------------------------------------------------------------------------
imgList = []
studentIds = []
# isme file name nikale student ka save karte hai file path me save karte hai 
for fileName in  os.listdir(FOLDER_PATH):
    path = os.path.join(FOLDER_PATH,fileName)
    image = cv2.imread(path)
    if image is None :
        continue
    imgList.append(image)
    studentIds.append(os.path.splitext(fileName)[0])
encodeList = []
for img in imgList:
    # print("img",img)
    
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    rgb  = np.ascontiguousarray(rgb)
    # print("New rgb", rgb)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).copy(order="C")
    # img = face_recognition.load_image_file("Images/101.png")  # replace with real path
    # face_locations = face_recognition.face_locations(img)
#  if we face the error unsupporting 
 
    if rgb is not None:
        encodings = face_recognition.face_encodings(rgb)
        if encodings :
            encodeList.append(encodings[0])
            print("Encoding", encodings[0])
      # print(face)
        # encodings = face_recognition.face_encodings(rgb)
        print("Shape:", rgb.shape)

        print("Dtype:", rgb.dtype)
        
    # gray_image = gray_image.astype('uint8') 
    # print(encodings)
print("✅ Encoding complete. Total:", len(encodeList))       
with open("EncodeFile.p", "wb") as f:
    pickle.dump([encodeList, studentIds], f)

print("Encoded Generated .")




# # 1️⃣  Make sure Images/ exists
# if not os.path.isdir(FOLDER_PATH):
#     raise FileNotFoundError(
#         f"❌  '{FOLDER_PATH}' folder not found.\n"
#         f"Create it beside EncodeGenerator.py and add face images inside."
#     )

# # 2️⃣  Load every image
# image_files = [f for f in os.listdir(FOLDER_PATH)
#                if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# if not image_files:
#     raise RuntimeError(f"No *.png / *.jpg images found in '{FOLDER_PATH}'")

# img_list, student_ids = [], []

# for file in image_files:
#     path = os.path.join(FOLDER_PATH, file)
#     img  = cv2.imread(path)
#     if img is None:
#         print(f"⚠️  Skipped unreadable file: {file}")
#         continue

#     img_list.append(img)
#     student_ids.append(os.path.splitext(file)[0])   # filename sans extension

# print("🖼  Images loaded:", student_ids)

# # 3️⃣  Compute encodings
# encode_list = []
# print("🔄  Computing face encodings …")
# for idx, img in enumerate(img_list, start=1):
#     rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#     encodings = face_recognition.face_encodings(rgb)
#     if not encodings:
#         print(f"⚠️  No face found in {image_files[idx-1]}  —  skipped.")
#         continue

#     encode_list.append(encodings[0])

# if not encode_list:
#     raise RuntimeError("❌  No valid faces detected in any image.")

# print(f"✅  Encoded {len(encode_list)} faces.")

# # 4️⃣  Save to pickle
# with open(ENCODINGS_PICKLE, "wb") as f:
#     pickle.dump([encode_list, student_ids], f)

# print(f"💾  Saved encodings → {ENCODINGS_PICKLE}")

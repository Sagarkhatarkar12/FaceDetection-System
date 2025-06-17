# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# ref = db.reference('Students')

# data = {
#     "4006":
#         {
#             "name": "Ankit Kumar",
#             "major": "COMP-SCI",
#             "starting_year": 2023,
#             "total_attendance": 7,
#             "standing": "G",
#             "year": 3,
#             "last_attendance_time": "2022-12-11 00:54:34"
#         },
#     "4010":
#         {
#             "name": "Anupam",
#             "major": "HOD-CS",
#             "starting_year": 2021,
#             "total_attendance": 12,
#             "standing": "B",
#             "year": 1,
#             "last_attendance_time": "2022-12-11 00:54:34"
#         },
#     "4024":
#         {
#             "name": "Sager",
#             "major": "COMP-SCI",
#             "starting_year": 2020,
#             "total_attendance": 7,
#             "standing": "G",
#             "year": 2,
#             "last_attendance_time": "2022-12-11 00:54:34"
#         },
#     "4027":
#         {
#             "name": "Prince",
#             "major": "COMP-SCI",
#             "starting_year": 2020,
#             "total_attendance": 7,
#             "standing": "G",
#             "year": 2,
#             "last_attendance_time": "2022-12-11 00:54:34"
#         }
# }

# for key, value in data.items():
#     ref.child(key).set(value)


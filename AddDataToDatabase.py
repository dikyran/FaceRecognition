import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendacerealtime-c9a3b-default-rtdb.firebaseio.com/"

})

ref = db.reference('Students')

data = {
    "150603":
        {
            "name": "Diky Tarihoran",
            "major": "IT",
            "starting_year":2021,
            "total_attendance":6,
            "standing":"G",
            "year":4,
            "Last_attendance_time": "2023-03-15 00:53:34"
        },

    "123456":
        {
            "name": "Jokowi",
            "major": "Presiden",
            "starting_year":2019,
            "total_attendance":8,
            "standing":"6",
            "year":8,
            "Last_attendance_time": "2023-03-15 00:53:34"
        },

    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year":2017,
            "total_attendance":12,
            "standing":"F",
            "year":4,
            "Last_attendance_time": "2023-03-15 00:53:34"
        },

    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year":2015,
            "total_attendance":18,
            "standing":"B",
            "year":4,
            "Last_attendance_time": "2023-03-15 00:53:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
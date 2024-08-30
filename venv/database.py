import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://test-data-base-da118-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference("Human")

data = {
    "1111":
        {
            "name": "Obama",
            "major": "Precident",
            "starting-year":2012,
            "total-attendence": 9,
            "last-attendence-time": "2022-12-20 00:44:11"
        },
    "1112":
        {
            "name": "Donatrump",
            "major": "Precident",
            "starting-year":2012,
            "total-attendence": 8,
            "last-attendence-time": "2022-12-20 00:44:11"
        },
    "1113":
        {
            "name": "Beautyful",
            "major": "Precident",
            "starting-year":2012,
            "total-attendence": 10,
            "last-attendence-time": "2022-12-20 00:44:11"
        },
    "1114":
        {
            "name": "Hung",
            "major": "Precident",
            "starting-year":2012,
            "total-attendence": 6,
            "last-attendence-time": "2022-12-20 00:44:11"
        },
    "1115":
        {
            "name": "Hai",
            "major": "Child",
            "starting-year":2012,
            "total-attendence": 5,
            "last-attendence-time": "2022-12-20 00:44:11"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
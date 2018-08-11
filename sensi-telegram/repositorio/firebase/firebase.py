import pyrebase

config = {
    "apiKey": "AIzaSyCbP0TVFRtoHsYNgnmiQ0XBxrGikEi17Do",
    "authDomain": "telemetriahucam.firebaseapp.com",
    "databaseURL": "https://telemetriahucam.firebaseio.com",
    "projectId": "telemetriahucam",
    "storageBucket": "telemetriahucam.appspot.com",
    "messagingSenderId": "976363001658"
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

data = {
    "tag_ID": 123456789,
    "data": "data de hoje",
    "temperatura": -25.5,
    "umidade": 80,
    "bateria": 25,
}

db.child("banco_sangue_hucam").child("tag_2").child("registro3").set(data)

a = db.child("banco_sangue_hucam").child("tag_1").get().each()
for i in a:
    b = i.val()
    c = b.keys()
    for j in c:
        print(b[j])

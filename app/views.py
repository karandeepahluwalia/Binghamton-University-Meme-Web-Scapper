from app import app
from flask import render_template, request, redirect
import os
import face_recognition

Scheer = face_recognition.load_image_file("app/static/img/known_pics/Andrew Scheer.jpg")
Scheer_encoding = face_recognition.face_encodings(Scheer)[0]
Blanchette = face_recognition.load_image_file("app/static/img/known_pics/Blanchette.jpg")
Blanchette_encoding = face_recognition.face_encodings(Blanchette)[0]
May = face_recognition.load_image_file("app/static/img/known_pics/ELizabeth May.jpg")
May_encoding = face_recognition.face_encodings(May)[0]
Singh = face_recognition.load_image_file("app/static/img/known_pics/Jagmeet Singh.jpg")
Singh_encoding = face_recognition.face_encodings(Singh)[0]
Trudeau = face_recognition.load_image_file("app/static/img/known_pics/Justin Trudeau.jpg")
Trudeau_encoding = face_recognition.face_encodings(Trudeau)[0]
Bernier = face_recognition.load_image_file("app/static/img/known_pics/Maxine Bernier.jpg")
Bernier_encoding = face_recognition.face_encodings(Bernier)[0]
Trudeau_right = face_recognition.load_image_file("app/static/img/known_pics/Trudeau sideways.jpg")
Trudeau_right_encoding = face_recognition.face_encodings(Trudeau_right)[0]
Trudeau_left = face_recognition.load_image_file("app/static/img/known_pics/Trudeau_left_side.jpg")
Trudeau_left_encoding = face_recognition.face_encodings(Trudeau_left)[0]
filename = ""
resp = ""
known_faces = [
    Scheer_encoding,
    Blanchette_encoding,
    May_encoding,
    Singh_encoding,
    Bernier_encoding,
    Trudeau_encoding,
    Trudeau_right_encoding,
    Trudeau_left_encoding
]
app.config["IM_UPLOAD"] = "/Users/karandeepahluwalia/desktop/Flask/app/static/img/uploads"
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        if request.files:
            global resp
            global filename
            filename = ""
            resp =""
            image = request.files["image"]
            image.save(os.path.join(app.config["IM_UPLOAD"],image.filename))
            filename = image.filename
            print("Image saved")
            unknown_pic = face_recognition.load_image_file("app/static/img/uploads/"+filename)
            unknown_encodings = face_recognition.face_encodings(unknown_pic)
            for faces in unknown_encodings:
                results = face_recognition.compare_faces(known_faces, faces)
                if results[0]:
                    resp +="Andrew Scheer,"
                if results[1]:
                    resp +="Blanchette,"
                if results[2]:
                    resp +="Elizabeth May,"
                if results[3]:
                    resp +="Jagmeet Singh,"
                if results[4]:
                    resp +="Maxine Bernier,"
                if results[5] or results[6] or results[7]:
                    resp +="Justin Trudeau,"
            return redirect(request.url)
    return render_template("index.html")


@app.route("/result")
def result():
    global resp
    print(filename)
    return resp

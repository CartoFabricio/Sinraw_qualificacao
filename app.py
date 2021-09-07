from flask import Flask, Response
from flask import render_template
import cv2
import folium
import numpy as np

app = Flask(__name__)


@app.route("/")
def Capa():
    return render_template("Capa.html")


video = cv2.VideoCapture(0)
def gen(video):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/Estilos')
def Estilos():
    return render_template("Estilos.html")


@app.route('/Mapa3D', methods=['GET', 'POST'])
def Mapa3D():
  opcoes = ('mapbox://styles/mapbox/satellite-streets-v10', 'streets-v11', 'light-v10')

  mapbox_access_token = 'pk.eyJ1IjoiZmFicmljaW9hbW9yaW0iLCJhIjoiY2tsaWNsOHRkMmgwaDJucGN0NGJhd3psOSJ9.h665zPxHXNFNVIzh1cJeUQ'
  mapbox_basemap = 'mapbox://styles/mapbox/streets-v11'
  return render_template('Mapbox.html',
                    mapbox_basemap=mapbox_basemap,
                    mapbox_access_token=mapbox_access_token,
                    )


if __name__ == '__main__':
    app.run(debug=True, host= '192.168.0.108')

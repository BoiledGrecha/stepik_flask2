from flask import Flask, render_template
import data
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

app.config["SECRET_KEY"] = "super_secret_key"
toolbar = DebugToolbarExtension(app)

@app.route("/")
def first():
	return render_template("index.html", departures=data.departures, hotels=data.tours)

@app.route("/departures/<departure>")
def route_departures(departure):
  if departure in data.departures:
    a=dict()
    for i in data.tours.keys():
      if data.tours[i]["departure"] == departure:
        a[i] = data.tours[i]
    return render_template("departure.html", departures=data.departures, town=data.departures[departure], hotels = a)
  else:
    #add picture sorry we are not working from here
    return "Wrong city", 404

@app.route("/tours/<id>")
def route_tours(id):
  if int(id) in data.tours:
    return render_template("tour.html", departures=data.departures, tour=data.tours[int(id)])
  else:
    return "Not existing", 404
	
#if __name__ == "__main__":
	#app.run(host = "185.162.131.72", port=80)
app.run(debug = True)

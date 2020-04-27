from flask import Flask, json, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def home():
    return render_template("index.html")

cars = [
        {"id":1, "name":"BMW", "model":"112"},
        {"id":2, "name":"BMW", "model":"522"},
        {"id":3, "name":"BMW", "model":"X5"},
        {"id":4, "name":"Skoda", "model":"Octavia"},
        {"id":5, "name":"Skoda", "model":"Fabia"},
        {"id":6, "name":"Skoda", "model":"Superb"},
        {"id":7, "name":"Volvo", "model":"V40"},
        {"id":8, "name":"Volvo", "model":"S60"},
        {"id":9, "name":"Volvo", "model":"XC60"}
        ]

@app.route('/cars', methods=['GET'])
def get_cars():
    return json.dumps(cars)
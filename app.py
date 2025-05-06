from flask import Flask, request, redirect, render_template
app = Flask(__name__)

lista = [1, 2, 3, 4]

@app.route("/")
def index():
    return render_template("index.html", lista = lista)#lista = nome della lista che abbiamo dato noi

if __name__ == "__main__":
    app.run(debug=True)
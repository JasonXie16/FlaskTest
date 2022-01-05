from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():

    ListVersions =  ["v1: 1.1.21","v2: 2.2.22"]
    out = render_template("start.html", game="Minecraft",gameversions=ListVersions)


    return out




if __name__ == '__main__':
    app.run()
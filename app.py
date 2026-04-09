import flask
app = flask.Flask(__name__)


@app.route("/")
def home():
    return "Hello Cortex Cloud Demo!"

app.run(host="0.0.0.0", port=5000)
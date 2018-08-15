import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=5010, debug=True, host='0.0.0.0')
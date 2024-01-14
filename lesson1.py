import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello from Sergey</h1>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, url_for

app = Flask(__name__)

# Создадим два эндпоинта для главной страницы и для страницы профиля
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

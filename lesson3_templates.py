# Импортируем класс Flask, и функцию render_template
from flask import Flask, render_template

# Создаем наше приложение
app = Flask(__name__)


# Модифицируем наш метод для главной страницы
@app.route('/')
def index():
    #  Заменим html строку на функцию render_template.
    # Она принимает название html файла и переменные используемые в шаблоне
    return render_template('index.html', title='Мой сайт', menu=['Поспать', 'Поесть', 'Попить воды'])


# Запуск программы
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

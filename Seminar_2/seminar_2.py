from pathlib import PurePath, Path

import flask
from markupsafe import escape
from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def base():  # put application's code here
    return render_template('base.html')


# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени

@app.route('/next/')
def next_page():  # put application's code here
    return render_template('page_1.html')


# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

@app.route('/load_image/', methods=['GET', 'POST'])
def load_image():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',
                                    file_name))
        return f"Файл {escape(file_name)} загружен на сервер"
    context = {'task': 'Задание_2'}
    return render_template('page_2.html', **context)


# Задание №3
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой

@app.route('/submit/', methods=['GET', 'POST'])
def authorization():
    login = {'name': 'Alex',
             'auth_pass': "1"}
    if request.method == 'POST':
        name = request.form.get('name')
        auth_pass = request.form.get('auth_pass')
        if name == login["name"] and auth_pass == login['auth_pass']:
            return f'Hello {escape(name)}, вход выполнен успешно!'
        else:
            return 'Ошибка ввода данных'
    context = {'task': 'Задание_3'}
    return render_template('authorization.html', **context)


# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.
@app.route('/1111/', methods=['GET', 'POST'])
def text_counter():
    if request.method == 'POST':
        text = request.form.get('text')
        return f'Количество слов : {len(text.split())}'
    context = {'task': 'Задание_4'}
    return render_template('text_counter.html', **context)

# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.


if __name__ == '__main__':
    app.run(debug=True)

from pathlib import PurePath, Path

from markupsafe import escape
from flask import Flask, render_template, url_for, request, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def base():  # put application's code here
    return render_template('base.html')


@app.route('/submit/', methods=['GET', 'POST'])
def authorization():
    login = {}
    if request.method == 'POST':
        name = request.form.get('name')
        auth_email = request.form.get('auth_email')
        login['my_name'] = name
        response = make_response(render_template("hello.html", **login))
        response.set_cookie('name', name)
        response.set_cookie('email', auth_email)
        return response

    context = {'task': 'Задание_8'}
    return render_template('authorization.html', **context)


@app.route("/logout/")
def logout():
    response = make_response(render_template('authorization.html'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


@app.route('/about/')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/contact/')
def contacts():  # put application's code here
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
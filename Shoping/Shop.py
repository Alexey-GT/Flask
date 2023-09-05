from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def shop_base():  # put application's code here
    return render_template('index.html')


# @app.route('/clothes/')
# def clothes():  # put application's code here
#     return render_template('clothes.html')
#
#
# @app.route('/shoes/')
# def shoes():  # put application's code here
#     return render_template('shoes.html')
#
#
# @app.route('/clothes/jackets/')
# def jacket():  # put application's code here
#     return render_template('jackets.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = "secret key"

@ app.route('/hello/')
@ app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('main.html', name=name)

if __name__ == '__main__':
   app.run(debug=True)
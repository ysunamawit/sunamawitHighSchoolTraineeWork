from flask import Flask, render_template , jsonify, request             # we import the Flask class
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                                  # we create an instance of the Flask class with our module name
app.secret_key = "secret key"                          # for encrypting sessions; don't worry about this for now
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/cookie_tracker'
db = SQLAlchemy(app)

class Cookie (db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False, autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    rating = db.Column(db.Integer,nullable=False)

    def __inti__(self,name,rating):
        self.name=name
        self.rating=rating




@app.route('/cookies')                                 # route decorator tells Flask what URL should trigger this function
def list_cookies():                                    # we name the function list_cookies
    # data = [
    #     {"name": "chocolate chip", "rating": 5},
    #     {"name": "oatmeal raisin", "rating": 1},
    #     {"name": "snickerdoodle", "rating": 3}
    # ]
    data = Cookie.query.all()

    return render_template('main.html', cookies=data)  # we render main.html and pass data over under the param "cookies"

@app.route('/cookie', methods=['POST'])
def add_cookie():
    data = request.form
    print(data)
    if data["name"] == "":
        return jsonify({"message": "failed!"}), 400
    else:
        new_cookie = Cookie(name=data["name"], rating=data["rating"])
        db.session.add(new_cookie)
        db.session.commit()
        return jsonify({"message": "success!"}), 200


    # @app.route("")
# def add_cookie():
#     return jsonify({"message": "failed!"}), 400

if __name__ == '__main__':                            # check if we're running the "main" function
   app.run(debug=True)                                 # run on debug mode (this allows for hot reload)


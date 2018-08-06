from flask import Flask,render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/finalWeb'
db = SQLAlchemy(app)

class Projects(db.Model):
    id = db.Column(db.Integer,primary_key=True,nullable=False, autoincrement=True)
    Name = db.Column(db.String(255),nullable=False)
    StartDate =db.Column(db.String(255),nullable=False)
    EndDate =db.Column(db.String(255),nullable=False)
    Description = db.Column(db.Text,nullable=False)
    Links =db.Column(db.String(255),nullable=True)
    Picture = db.Column(db.String(255),nullable=True)
    def __init__(self,Name,StartDate,EndDate,Description,Links,Picture):
        self.Name= Name
        self.StartDate=StartDate
        self.EndDate=EndDate
        self.Description=Description
        self.Links=Links
        self.Picture=Picture




@app.route('/')
def mainfunction():
    projects = Projects.query.all()
    return render_template('main.html',projects=projects)


@app.route('/projects')
def show_projects():
    projects = Projects.query.all()
    return render_template('projects.html',projects=projects)

@app.route('/project', methods=['POST'])
def add_project():
    data = request.form
    if data["Name"] == "" or data["StartDate"] == "" or data["EndDate"] == "" or data["Description"] == "":
        return jsonify({"message": "failed!"}), 400
    else:
        project = Projects(Name=data["Name"], StartDate=data["StartDate"], EndDate=data["EndDate"], Description=data["Description"], Links=data["Links"], Picture=data["Picture"])
        db.session.add(project)
        db.session.commit()
        return jsonify({"message": "success!"}), 200

@app.route('/delete', methods=['POST'])
def delete_project():
    id = request.form["id"]
    project = Projects.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect("/")















if __name__ == '__main__':
    app.run(debug=True)
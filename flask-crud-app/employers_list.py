# Simple CRUD app with Flask(Employers list)

# Importing modules
import os

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask_sqlalchemy import SQLAlchemy

# Getting project path
project_dir = os.path.dirname(os.path.abspath(__file__))
# Here we are using sqlite database
database_file = "sqlite:///{}".format(os.path.join(project_dir,"employers.db"))

# Intializing flask object
app = Flask(__name__)
# Place to store database file
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# Intializing SQLAlchemy object and assigning it to db
db = SQLAlchemy(app)

# Employees class
class Employees(db.Model):
	# Creating emp_name column
	emp_name = db.Column(db.String(80), unique=True, nullable=False, primary_key = True)

	# Covnerting Employee object to string format
	def __repr__(self):
		return "<Emp_name: {}>".format(self.emp_name)


@app.route('/', methods=['GET','POST'])	# render a template
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			return redirect(url_for('home'))
		else:
			error = 'Invalid credentials. Please try again.'
	return render_template('login.html',error = error)

# Home page
@app.route("/create", methods=['GET','POST'])
# Defining home function
def home():
	employees = None
	if request.form:
		try:
			# Getting input form form tag and assigning it to employee variable
			employee = Employees(emp_name = request.form.get("emp_name"))
			# Adding employee to database db
			db.session.add(employee)
			# Commiting the changes
			db.session.commit()
		except Exception as e:
			print("Failed to add employee")
			print(e)
	# Retrieving all employers name from database
	employees = Employees.query.all()	
	# Rendering html file from templates folder
	return render_template('home.html',  employees = employees)

# Udation page
@app.route("/update",methods = ['POST'])
# Defining a function that updates the employers name in database
def update():
	try:
		# Getting new emp_name from the form tag
		newemp_name = request.form.get("newemp_name")
		# Getting old emp_name from the form tag
		oldemp_name = request.form.get("oldemp_name")
		# Fetching old emp_name from the form tag
		employee = Employees.query.filter_by(emp_name = oldemp_name).first()
		# Updating the new emp_name
		employee.emp_name = newemp_name
		# Commiting the changes
		db.session.commit()
	except Exception as e:
		print("Couldn't update employee name")
		print(e)
	return redirect("/create")

# Deletion page
@app.route("/delete",methods = ['POST'])
# Defining a function that deletes record from the table
def delete():
	# Getting employee name from the form tag to delete it
	emp_name = request.form.get("emp_name")
	# Fetching the requested emp_name in database
	employee = Employees.query.filter_by(emp_name = emp_name).first()
	# Deleting that employee
	db.session.delete(employee)
	# Commiting the changes
	db.session.commit()
	return redirect("/create")

# Checking whether this program directly running
if __name__ == "__main__":
	# Running the above code with debug mode on
	app.run(debug=True)

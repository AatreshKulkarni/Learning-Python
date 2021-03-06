# Generates a simple login page

# Importing modules from flask package
from flask import Flask, request, render_template, redirect, url_for

# Create the application object
app = Flask(__name__)

# Using decorators to link the func to a url
@app.route('/')
def index():	
	return "Hello World!"	# returns a string


@app.route('/login', methods=['GET','POST'])	# render a template
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			return redirect(url_for('index'))
	return render_template('login.html',error = error)


# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug = True)
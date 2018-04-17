from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App!"
 
#@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/")
def hello(name):
#    return name
    quotes = [  "Cricket is a team game. If you want fame for yourself, go play an individual game. -Gautam Gambhir",
				"If you play good cricket, a lot of bad things get hidden. - Kapil Dev",
    			"I've seen God. He bats at No.4 for India in Tests. - Matthew Hayden",
    			"I would go to war with Dhoni by my side - Gary Kirsten",
    			"On the off-side,first there is God, then Sourav Ganguly. - Rahul Dravid",
    			"Dravid could play attacking crickey like me,but I could never play like him. - Chris Gayle" 
    		]	
    randomNumber = randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
 
    return render_template(
        'test.html',**locals())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
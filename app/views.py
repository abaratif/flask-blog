from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Brian'}  # fake user
	posts = [  # fake array of posts
		{ 
			'author': {'nickname': 'John'}, 
			'body': 'Beautiful day in Portland!',
			'feeling' : 'Happy!',
			'date': 'Monday' 
		},
		{ 
			'author': {'nickname': 'Susan'}, 
			'body': 'The Avengers movie was so cool!',
			# 'feeling' : "Super.",
			'date': 'Monday'  
		}
	]
	return render_template("index.html",
						   title='Home',
						   user=user,
						   posts=posts)
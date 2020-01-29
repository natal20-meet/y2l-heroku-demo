from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html') 
	else: 
		Username = request.form['Username']
		Email = request.form['Email']
		Password = request.form['Password']
		add_user(Username,Email,Password,"")
		return render_template ('home.html')
@app.route('/recent_posts',methods=["GET","POST"])
def recent_posts():
	if request.method == "GET":
		posts = query_posts()
		return render_template('recent_posts.html', posts = posts)
	else:
		form = request.form['search']
		allposts = query_posts()
		posts = query_by_category(form)
		return render_template('recent_posts.html', posts = posts, allposts=allposts) 

@app.route('/profile')
def profile():
	return render_template('profile.html')

@app.route('/tutorial')
def tutorials():
	return render_template('tutorial.html')

@app.route('/moodboard/<int:ID>')
def moodboard(ID): 
	posts = save_post(ID)
	return redirect(url_for('genModd'))

@app.route('/moodboard')
def genModd():
	posts = query_moodboard()
	#query moodboard
	return render_template('moodboard.html' ,posts=posts)	

@app.route('/post',methods=['GET','POST'])
def post():
	if request.method == 'GET':
		return render_template('post.html') 
	else: 
		category = request.form['category']
		Picture = request.form['Picture']
		Description = request.form['description']
		add_post(category,Picture,Description)
		return redirect(url_for('recent_posts'))
	
@app.route('/tutorial')
def yt_tutorials():
	return render_template('tutorial.html')

@app.route('/about')
def about(): 
	return render_template('about.html')


#####################
if __name__ == '__main__':
    app.run(debug=True)
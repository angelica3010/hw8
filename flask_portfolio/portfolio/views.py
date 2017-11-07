from . import app
from flask import Flask, render_template, request


like_count = 0


comments = [{'name' :'Angel','message' : 'Hello'},
			{'name': 'Phillip', 'message': '$10 please!'}]

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        return render_template('photos.html')
    else:
        return render_template('index.html')


@app.route('/about', methods = ['POST','GET'])

def about():
    if request.method == 'POST':
        global like_count
        like_count += 1
        print(f'count is now {like_count}.')

    count = like_count
    return render_template('aboutangel.html', new_count = count)

@app.route('/photos', methods = ['GET', 'POST'])
def info():
	if request.method == 'POST':
		name1 = request.form['name']
		message1 = request.form['message']
		comments.append({'name' : name1, 'message': message1})

		print(comments)
		return render_template('/photos.html', messages = comments)
	else:
		print('get method')
		print(comments)
		return render_template('photos.html', messages= comments)

from . import app
from flask import Flask, render_template, request

like_count = 0

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

@app.route('/photos', methods = ['POST','GET'])
def picture():
    return render_template('photos.html')

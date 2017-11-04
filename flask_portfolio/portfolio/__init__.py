from flask import Flask, render_template, request
app = Flask('portfolio')

from . import views

"""@app.route('/')
def index():
    name = 'saroosh'
    day = 'thursday'
    return render_template('index.html', name = name, day = day)

@app.route('/about')
def about():
    return "About me page"

@app.route('/contact')
def contact():
    return "Contact page"

if __name__ == "__main__":
    app.run(debug=True)"""

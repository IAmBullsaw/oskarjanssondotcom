from flask import Flask, render_template, request, redirect, make_response
from card import Card
from data import Data
from logging.handlers import RotatingFileHandler
from random import randint
import jinja2
import logging

app = Flask(__name__)

d = Data()
@app.route('/')
def index():
    d.load_JSON('data.json')
    cards = d.get_cards()
    return render_template('index.html', cards = cards, n = None, c_length=len(cards))

@app.route('/linkedin/')
def linkedin():
    return redirect('https://www.linkedin.com/in/oskarjansson', code=302)

@app.route('/git/')
def git():
    return redirect('https://github.com/IAmBullsaw', code=302)

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/p/random/')
def random_card():
    d.load_JSON('data.json')
    cards = d.get_cards()

    r = randint(0, len(cards)-1)
    url = '/' + str(r)
    return redirect(url, code=302)

@app.route('/p/<project>')
def title(project):
    app.logger.info("User searched for <title>='{}'".format(title))
    d.load_JSON('data.json')
    cards = d.get_cards()

    try:
        # Searched with index
        n = int(project)
        if (n >= 0 and n < len(cards)):
            return render_template('index.html',cards = cards, n = -(n+1), c_length=len(cards))
        else:
            return error_404("404 - Not Found","Helpful tip: Try something more like 0 - {}.".format(len(cards)-1))
    except:
        if project == 'random':
            # If user requested a random page, redirect them
            return error_404("<project> = 'random'","Helpful tip: Don't forget the trailing slash!")
        else:
            # User searched for a project
            for c in cards:
                if c._title.lower() == project.lower():
                    return render_template('index.html',cards = cards, n = c._id, c_length=len(cards))
            return error_404("<project> = {}".format(project),"Helpful tip: My website isn't that large right now, try looking for it manually...")

@app.errorhandler(400)
def error_400(error, message = None):
    title = "400 - Bad Request"
    url = 'oskarjansson.com' + request.path

    app.logger.warning('{}, {}. URL={}'.format(title,error,url))
    return render_template('error.html', title = title, url = url, error = error, message = message),400

@app.errorhandler(404)
def error_404(error, message = None):
    title = "404 - Not Found"
    url = 'oskarjansson.com' + request.path

    app.logger.warning('{}, {}. URL={}'.format(title,error,url))
    return render_template('error.html', title = title, url = url, error = error, message = message),404

@app.errorhandler(405)
def error_405(error, message = None):
    title = "405 - Method Not Allowed"
    url = 'oskarjansson.com' + request.path

    app.logger.warning('{}, {}. URL={}'.format(title,error,url))
    return render_template('error.html', title = title, url = url, error = error, message = message),405

@app.errorhandler(500)
def error_500(error, message = None):
    title = "500 - Internal Server Error"
    url = 'oskarjansson.com' + request.path

    app.logger.warning('{}, {}. URL={}'.format(title,error,url))
    return render_template('error.html', title = title, url = url, error = error, message = message),500

if __name__ == '__main__':
    handler = RotatingFileHandler('log/flask_App.log', maxBytes=100000, backupCount=5)
    formatter = logging.Formatter("[%(asctime)s] {%(lineno)d} %(levelname)s - %(message)s")
    app.logger.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(debug = True)

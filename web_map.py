from flask import Flask, request, render_template
from main_1 import authorization, map
application = Flask(__name__)


@application.route("/")
def html_page():
    """
    This function makes an Html page
    """
    return render_template('Map_twitter.html')


@application.route("/twitter", methods=["GET", "POST"])
def making_map():
    """
    This function makes an app
    """
    account = request.form['tweecount']
    number = request.form['num_friends']
    n_map = map(authorization(account, number))
    return n_map


application.run(debug=True)
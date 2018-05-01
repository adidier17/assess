from . import frontend

from flask import render_template

@frontend.route('/', methods=('GET', 'POST'))
def index():
    """
    Returns the main page of the frontend.
    """

    return render_template('frontend/index.new.html')

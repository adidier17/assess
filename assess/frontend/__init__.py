from flask import Blueprint 
#from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__, template_folder='templates', 
                     static_folder='static')

from . import views

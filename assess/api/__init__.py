from flask import Blueprint
#from flask import Blueprint, jsonify, json

api = Blueprint('api', __name__)

from . import views

from flask import Blueprint

sign = Blueprint('sign', __name__)

from . import views
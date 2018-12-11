from flask import Blueprint

home = Blueprint('home', __name__)

from news.new.home import views
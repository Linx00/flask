from flask import Blueprint

admin = Blueprint('admin', __name__)

import news.new.admin.views

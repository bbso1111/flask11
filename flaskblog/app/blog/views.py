from flask import Blueprint,Flask

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('index/')
def index():
    return 'Hello Word'
from flask import (Blueprint, render_template)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return 'This is the pets index'

from flask import Blueprint
from app.api.v1 import bp as v1_bp

bp = Blueprint('api', __name__, url_prefix='/api')

bp.register_blueprint(v1_bp)
from flask import Blueprint

core_api = Blueprint('core_api', __name__, url_prefix="/")

from app.API import core

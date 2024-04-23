from quart import Blueprint
from chgk.views import index


game_blueprint = Blueprint('chgk', __name__, template_folder='templates', static_folder='static')
game_blueprint.add_url_rule('/', view_func=index)

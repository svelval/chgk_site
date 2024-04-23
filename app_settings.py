from quart import Quart
from chgk.urls import game_blueprint

app = Quart(__name__, static_folder=None)
app.register_blueprint(game_blueprint)

from flask import Flask
from config import Config
from controllers import auth_controller, puzzle_controller, leaderboard_controller, multiplayer_controller

app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(auth_controller.bp, url_prefix='/api/auth')
app.register_blueprint(puzzle_controller.bp, url_prefix='/api/puzzle')
app.register_blueprint(leaderboard_controller.bp, url_prefix='/api/leaderboard')
app.register_blueprint(multiplayer_controller.bp, url_prefix='/api/multiplayer')

@app.route('/')
def index():
        return "Welcome to Sitrix API"

    if __name__ == '__main__':
            app.run(debug=True)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import User
from .puzzle_model import Puzzle
from .solution_model import Solution
from .leaderboard_model import Leaderboard
from .achievement_model import Achievement
from .multiplayer_model import Multiplayer
from .socialshare_model import SocialShare


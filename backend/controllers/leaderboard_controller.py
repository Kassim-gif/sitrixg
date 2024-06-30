from flask import Blueprint, jsonify
from models import leaderboard_model

bp = Blueprint('leaderboard', __name__)

@bp.route('/', methods=['GET'])
def get_leaderboard():
        leaderboard = leaderboard_model.get_leaderboard()
            return jsonify(leaderboard), 200

        @bp.route('/achievement', methods=['GET', 'POST'])
        def achievements():
                if request.method == 'GET':
                            achievements = leaderboard_model.get_user_achievements(request.args.get('user_id'))
                                    return jsonify(achievements), 200
                                    elif request.method == 'POST':
                                                data = request.get_json()
                                                        leaderboard_model.add_achievement(data['user_id'], data['achievement'])
                                                                return jsonify({'message': 'Achievement added'}), 201


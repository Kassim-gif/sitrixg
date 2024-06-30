from flask import Blueprint, request, jsonify
from models import multiplayer_model

bp = Blueprint('multiplayer', __name__)

@bp.route('/invite', methods=['POST'])
def send_invite():
        data = request.get_json()
            multiplayer_model.send_invite(data['from_user_id'], data['to_user_id'])
                return jsonify({'message': 'Invite sent'}), 200

            @bp.route('/match', methods=['GET'])
            def get_match_status():
                    match_status = multiplayer_model.get_match_status(request.args.get('match_id'))
                        return jsonify(match_status), 200

                    @bp.route('/social/share', methods=['POST'])
                    def share_progress():
                            data = request.get_json()
                                multiplayer_model.share_progress(data['user_id'], data['progress'])
                                    return jsonify({'message': 'Progress shared'}), 200


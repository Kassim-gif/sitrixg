from flask import Blueprint, request, jsonify
from models import puzzle_model, solution_model

bp = Blueprint('puzzle', __name__)

@bp.route('/generate', methods=['GET'])
def generate_puzzle():
        # Generate a new puzzle (implement the logic)
            puzzle = puzzle_model.generate_puzzle(difficulty=request.args.get('difficulty', 'easy'))
                return jsonify(puzzle), 200

            @bp.route('/validate', methods=['POST'])
            def validate_solution():
                    data = request.get_json()
                        is_valid = solution_model.validate_solution(data['puzzle_id'], data['solution'])
                            return jsonify({'is_valid': is_valid}), 200

                        @bp.route('/hint', methods=['GET'])
                        def get_hint():
                                puzzle_id = request.args.get('puzzle_id')
                                    hint = puzzle_model.get_hint(puzzle_id)
                                        return jsonify({'hint': hint}), 200


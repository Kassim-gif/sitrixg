from . import db

class Solution(db.Model):
        id = db.Column(db.Integer, primary_key=True)
            puzzle_id = db.Column(db.Integer, db.ForeignKey('puzzle.id'), nullable=False)
                user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
                    solution_data = db.Column(db.Text, nullable=False)
                        is_valid = db.Column(db.Boolean, nullable=False)

                            @staticmethod
                                def validate_solution(puzzle_id, solution):
                                            # Implement your solution validation logic here
                                                    return True


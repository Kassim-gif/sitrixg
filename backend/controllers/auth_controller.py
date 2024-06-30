from flask import Blueprint, request, jsonify
from models import user_model
from utils import validation_utils
from werkzeug.security import generate_password_hash, check_password_hash


bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
        data = request.get_json()
            if not validation_utils.is_valid_registration(data):
                        return jsonify({'error': 'Invalid data'}), 400
                        
                        hashed_password = generate_password_hash(data['password'])
                            new_user = user_model.User(username=data['username'], email=data['email'], password=hashed_password)
                                
                                    # Save user to database
                                        # (You'll need to implement this part based on your specific ORM or database setup)
                                            
                                                return jsonify({'message': 'User registered successfully'}), 201

                                            @bp.route('/login', methods=['POST'])
                                            def login():
                                                    data = request.get_json()
                                                        user = user_model.User.query.filter_by(username=data['username']).first()
                                                            
                                                                if user and check_password_hash(user.password, data['password']):
                                                                            # Generate and return a session token (implement your own token generation logic)
                                                                                    return jsonify({'message': 'Login successful'}), 200
                                                                                    else:
                                                                                                return jsonify({'error': 'Invalid credentials'}), 401

                                                                                            @bp.route('/profile', methods=['GET'])
                                                                                            def profile():
                                                                                                    # Retrieve user profile based on session token (you'll need to implement session management)
                                                                                                        user_profile = {
                                                                                                                        'username': 'example_user',
                                                                                                                                'email': 'user@example.com'
                                                                                                                                    }
                                                                                                            return jsonify(user_profile)

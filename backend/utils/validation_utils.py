import re

def is_valid_email(email):
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            return re.match(regex, email) is not None

        def is_valid_registration(data):
                return (
                                'username' in data and
                                        'email' in data and
                                                is_valid_email(data['email']) and
                                                        'password' in data and
                                                                len(data['password']) >= 8
                                                                    )
                :wq


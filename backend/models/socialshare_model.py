from . import db

class SocialShare(db.Model):
        id = db.Column(db.Integer, primary_key=True)
            user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
                progress = db.Column(db.Text, nullable=False)

                    @staticmethod
                        def share_progress(user_id, progress):
                                    # Implement your progress sharing logic here
                                            pass


from . import db

class Achievement(db.Model):
        id = db.Column(db.Integer, primary_key=True)
            user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
                achievement = db.Column(db.String(200), nullable=False)

                    def __repr__(self):
                                return f'<Achievement {self.achievement}>'


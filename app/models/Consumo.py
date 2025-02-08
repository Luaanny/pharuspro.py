from datetime import datetime
from app.extensions.database import db

class Consumo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Define valor padrão
    potency = db.Column(db.Float, nullable=False)
    time_interval = db.Column(db.Float, nullable=False)
    tariff = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_consumo_user',ondelete="CASCADE"), nullable=False)
    consumo_mensal = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref='consumos_user')

    def __repr__(self):
        return f"<Consumo {self.id} - User {self.user_id}>"

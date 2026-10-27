"""
Account model and persistence helpers.
"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    """An account belonging to a customer."""

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)
    phone_number = db.Column(db.String(32), nullable=True)
    address = db.Column(db.String(256), nullable=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        """Serialize the account to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "date_joined": self.date_joined.isoformat() if self.date_joined else None,
        }

    def from_dict(self, data):
        """Populate the account from a dictionary."""
        for field in ("name", "email", "phone_number", "address"):
            if field in data:
                setattr(self, field, data[field])
        if "date_joined" in data and data["date_joined"]:
            value = data["date_joined"]
            if isinstance(value, str):
                value = datetime.fromisoformat(value.replace("Z", "+00:00"))
            self.date_joined = value

    def create(self):
        """Add the account to the database."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Commit pending changes to the database."""
        if not self.id:
            raise ValueError("Cannot update an account that has not been created")
        db.session.commit()

    def delete(self):
        """Delete the account from the database."""
        db.session.delete(self)
        db.session.commit()

from sqlalchemy.orm import relationship
from web_app import db

class Taxonomy(db.Model):
    __tablename__ = "Taxonomy"
    id = db.Column(db.Integer, primary_key=True)
    nm_taxonomy = db.Column(db.Text, nullable=False)
    sequence = relationship("Sequence", backref="Sequence", uselist=False)

    def __repr__(self):
	    return f'''Taxonomy(id = {self.id}, 
                            nm_taxonomy = {self.sequence}, 
                            sequence_id = {self.sequence.id})'''
from sqlalchemy.orm import relationship
from web_app import db
from web_app.enums.sequenceTypeEnum import SequenceTypeEnum

class Sequence(db.Model):
    __tablename__ = "Sequence"
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    taxonomy_id = db.Column(db.Integer, db.ForeignKey("Taxonomy.id"))
    taxonomy = relationship("Taxonomy", backref="Taxonomy", uselist=False)

    def __repr__(self):
	    return f'''Sequence(id = {self.id}, 
                            sequence = {self.sequence}, 
                            sequence_type = {self.type},
                            taxonomy_id = {self.taxonomy_id})'''
from sqlalchemy.orm import relationship
from web_app import db
from web_app.enums.sequenceTypeEnum import SequenceTypeEnum

class Sequence(db.Model):
    __tablename__ = "Sequence"
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    country_origin = db.Column(db.Text, nullable=False)
    external_database_id = db.Column(db.Text, nullable=False)
    taxonomy_id = db.Column(db.Integer, db.ForeignKey("Taxonomy.id"))
    taxonomy = relationship("Taxonomy", backref="Taxonomy", uselist=False)

    def __repr__(self):
	    return f'''Sequence(id = {self.id}, 
                            sequence = {self.sequence}, 
                            sequence_type = {self.type},
                            country_origin = {self.country_origin},
                            external_database_id = {self.external_database_id},
                            taxonomy_id = {self.taxonomy.id})'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# Falsk's gateway
app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Database
db = SQLAlchemy(app)

#Apis
api_path = app.config['API_PATH']
api = Api(app)

from web_app.apis.phylogenyApi import PhylogenyApi
from web_app.apis.sequenceAlignmentApi import SequenceAlignmentApi
from web_app.apis.taxonomySearchApi import TaxonomySearchApi

api.add_resource(SequenceAlignmentApi, f'{api_path}/sequence-alignment')
api.add_resource(TaxonomySearchApi, f'{api_path}/taxonomy')
api.add_resource(PhylogenyApi, f'{api_path}/phylogeny')
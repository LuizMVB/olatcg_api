from flask_restful import Api
from web_app import app
from web_app.apis.treeApi import TreeApi
from web_app.apis.sequenceAlignmentApi import SequenceAlignmentApi
from web_app.apis.taxonomySearchApi import TaxonomySearchApi

# Apis
def add_resources():
    api_path = app.config['API_PATH']
    api = Api(app)
    api.add_resource(SequenceAlignmentApi, f'{api_path}/sequence-alignment')
    api.add_resource(TaxonomySearchApi, f'{api_path}/taxonomy-search')
    api.add_resource(TreeApi, f'{api_path}/tree')
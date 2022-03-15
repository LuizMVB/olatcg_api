from web_app import api_path
from web_app.apis.phylogenyApi import PhylogenyApi
from web_app.apis.sequenceAlignmentApi import SequenceAlignmentApi
from web_app.apis.taxonomySearchApi import TaxonomySearchApi

# Apis
def add_resources():
    api.add_resource(SequenceAlignmentApi, f'{api_path}/sequence-alignment')
    api.add_resource(TaxonomySearchApi, f'{api_path}/taxonomy')
    api.add_resource(PhylogenyApi, f'{api_path}/phylogeny')
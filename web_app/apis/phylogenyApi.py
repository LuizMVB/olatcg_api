from flask_restful import Resource, reqparse
from web_app.models.phylogenyModel import PhylogenyModel

phylogeny_get_args = reqparse.RequestParser()
phylogeny_get_args.add_argument('encodedFastaFile', type=str)

class PhylogenyApi(Resource):
    def get(self):
        args = phylogeny_get_args.parse_args()
        return PhylogenyModel().getNewickFormat(args.encodedFastaFile)
        
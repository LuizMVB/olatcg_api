from flask_restful import Resource, reqparse
from web_app.enums.supportedDatabasesEnum import SupportedDatabasesEnum
from web_app.models.taxonomyModel import TaxonomyModel

homology_search_get_args = reqparse.RequestParser()
homology_search_get_args.add_argument('sequences', action='append')
homology_search_get_args.add_argument('database', type=SupportedDatabasesEnum, choices=list(SupportedDatabasesEnum).append(None))

class TaxonomySearchApi(Resource):
    def get(self):
        args = homology_search_get_args.parse_args()
        enum_default_db = SupportedDatabasesEnum.DEFAULT
        if args['database'] == enum_default_db or args['database'] == None:
            return TaxonomyModel().get_taxonomy_to_sequences(sequences=args['sequences'])
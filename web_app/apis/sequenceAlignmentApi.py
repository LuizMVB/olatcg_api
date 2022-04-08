from web_app.models.alignmentModel import AlignmentModel
from web_app.enums.alignmentTypesEnum import AlignmentTypesEnum
from flask_restful import Resource, reqparse, fields, marshal_with

alignment_get_args = reqparse.RequestParser()
alignment_get_args.add_argument('sequence_a', type=str, required=True)
alignment_get_args.add_argument('sequence_b', type=str, required=True)
#TODO: restringir tipo do database aos valores de um enumerador do sistema
alignment_get_args.add_argument('type', type=str, required=True)
alignment_get_args.add_argument('tool', type=str)
alignment_get_args.add_argument('match_score', type=float)
alignment_get_args.add_argument('mismatch_score', type=float)
alignment_get_args.add_argument('get_first', type=bool)

class SequenceAlignmentApi(Resource):
    def get(self):
        args = alignment_get_args.parse_args()
        if not args['tool']:
            if args['type'].upper() == AlignmentTypesEnum.GLOBAL.value.upper():
                return AlignmentModel().align(sequence_a=args['sequence_a'], sequence_b=args['sequence_b'], get_first=args['get_first'])     
            elif args['type'].upper() == AlignmentTypesEnum.LOCAL.value.upper():
                return AlignmentModel(mode=args['type']).align(sequence_a=args['sequence_a'], sequence_b=args['sequence_b'], get_first=args['get_first'])     



        
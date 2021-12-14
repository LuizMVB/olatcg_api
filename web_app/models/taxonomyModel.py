from web_app.enums.alignmentTypesEnum import AlignmentTypesEnum
from web_app.enums.supportedDatabasesEnum import SupportedDatabasesEnum
from web_app.models.alignmentModel import AlignmentModel
from web_app.schema.Sequence import Sequence


class TaxonomyModel:
    def __init__(self):
        self.database = SupportedDatabasesEnum.DEFAULT.value

    def get_taxonomy_to_sequences(self, sequences:list):
        bigger_score_alignment = {}
        input_sequence = ''
        match_sequence = {}
        annotated_sequences = []
        for user_sequence in sequences:
            for database_sequence in Sequence.query.all():
                alignment = AlignmentModel(mode=AlignmentTypesEnum.LOCAL.value).align(sequence_a=user_sequence, sequence_b=database_sequence.sequence, get_first=True)
                input_sequence = user_sequence
                match_sequence = database_sequence
                if bigger_score_alignment == {}:
                    bigger_score_alignment = alignment
                elif alignment['score'] > bigger_score_alignment['score']:
                    bigger_score_alignment = alignment['score']
            annotated_sequences.append({
                'input_sequence': input_sequence,
                'match_sequence': match_sequence.sequence,
                'input_alignment': bigger_score_alignment['alignment_a'],
                'match_alignment': bigger_score_alignment['alignment_b'],
                'taxonomy': match_sequence.taxonomy.nm_taxonomy,
                'score': bigger_score_alignment['score']
            })
            bigger_score_alignment = {}
        return self._format_taxonomy_to_sequence_response(annotated_sequences)

    def _format_taxonomy_to_sequence_response(self, annotated_sequence):
        return {"alignments": annotated_sequence}
        
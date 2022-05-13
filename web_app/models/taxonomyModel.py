from web_app.enums.alignmentTypesEnum import AlignmentTypesEnum
from web_app.enums.supportedDatabasesEnum import SupportedDatabasesEnum
from web_app.models.alignmentModel import AlignmentModel
from web_app.schema.Sequence import Sequence

class TaxonomyModel:
    def __init__(self):
        self.database = SupportedDatabasesEnum.DEFAULT.value

    def get_taxonomy_to_sequences(self, sequences:list):
        bigger_score_alignment = {}
        match_sequence = {}
        annotated_sequences = []
        for user_sequence in sequences:
            for database_sequence in Sequence.query.all():
                alignment = AlignmentModel(mode=AlignmentTypesEnum.LOCAL.value).align(sequence_a=user_sequence, sequence_b=database_sequence.sequence, get_first=True)
                if bigger_score_alignment == {} or alignment['similarity'] > bigger_score_alignment['similarity']:
                    match_sequence = database_sequence
                    bigger_score_alignment = alignment
            annotated_sequences.append({
                'input_sequence': user_sequence,
                'match_sequence': match_sequence.sequence,
                'input_alignment': bigger_score_alignment['alignment_a'],
                'match_alignment': bigger_score_alignment['alignment_b'],
                'taxonomy': match_sequence.taxonomy.nm_taxonomy,
                'external_database_id': match_sequence.external_database_id,
                'country_origin': match_sequence.country_origin,
                'score': bigger_score_alignment['score'],
                'similarity': bigger_score_alignment['similarity']
            })
            bigger_score_alignment = {}
        return self._format_taxonomy_to_sequence_response(annotated_sequences)

    def _format_taxonomy_to_sequence_response(self, annotated_sequence):
        return {"alignments": annotated_sequence}
        
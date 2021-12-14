from Bio.Align import PairwiseAligner, PairwiseAlignments
from config import DEFAULT_MATCH_SCORE, DEFAULT_MISMATCH_SCORE
from web_app.enums.alignmentTypesEnum import AlignmentTypesEnum

class AlignmentModel:
    def __init__(self, mode=AlignmentTypesEnum.GLOBAL.value, match_score=DEFAULT_MATCH_SCORE, mismatch_score=DEFAULT_MISMATCH_SCORE):
        self.mode = mode
        self.match_score = match_score
        self.mismatch_score = mismatch_score

    def align(self, sequence_a:str, sequence_b:str, get_first=False):
        '''Default API global alignment. Realize an alignment
        with Bio.Align.PairwiseAligner from Biopython
        
        Parameters:
        sequence_a(str): first sequence
        sequence_b(str): second sequence

        Returns:
        str: alignment_a
        str: alignment_b
        '''
        sequence_a = sequence_a.upper()
        sequence_b = sequence_b.upper()

        aligner = PairwiseAligner()
        aligner.mode = self.mode
        alignments = aligner.align(seqA=sequence_a, seqB=sequence_b)

        if get_first:
            return self._biopython_formated_str_alignment_to_list(alignment=alignments[0])
        else:
            return self._biopython_pairwise_alignments_to_list(alignments=alignments)
    
    def _biopython_formated_str_alignment_to_list(self, alignment):
        '''Return the aligned sequences of Biopython's alignment
        formated string as a dictionary of alignments

        Parameters:
        alignment(str): Biopython's alignment formated string

        Returns:
        dict: alignments
        '''
        alignments = str(alignment).split('\n')
        return {
            'alignment_a': alignments[0],
            'alignment_b': alignments[2],
            'score': alignment.score
        }
    
    def _biopython_pairwise_alignments_to_list(self, alignments:PairwiseAlignments):
        '''Return the aligned sequences of Biopython's object 
        PairwiseAlignments as a list of alignment's objects

        Parameters:
        alignments(str): PairwiseAlignments object from Biopython

        Returns:
        list: possible_alignments
        '''
        possible_alignments = []
        for alignment in alignments:
            possible_alignments.append(self._biopython_formated_str_alignment_to_list(alignment))
        return {'alignments': possible_alignments}

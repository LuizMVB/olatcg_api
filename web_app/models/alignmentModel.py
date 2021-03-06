from Bio.Align import PairwiseAligner, PairwiseAlignments
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
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
        aligner.mode = self.mode.lower()
        alignments = aligner.align(seqA=sequence_a, seqB=sequence_b)

        if get_first:
            return self._biopython_formated_str_alignment_to_list(alignment=alignments[0], score=alignments.score)
        else:
            return self._biopython_pairwise_alignments_to_list(alignments=alignments)

    def msa(self, sequences:list):
        maxlen = max(len(sequence['bases']) for sequence in sequences)
        sequenceRecords = list()
        for sequence in sequences:
            if len(sequence['bases']) != maxlen:
                sequenceWithRightLength = str(sequence['bases']).ljust(maxlen, '.')
                sequenceRecords.append(SeqRecord(Seq(sequenceWithRightLength), id=sequence['id']))
        return MultipleSeqAlignment(sequenceRecords);
    

    def _biopython_formated_str_alignment_to_list(self, alignment, score):
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
            'similarity': self._getSimilarity(alignments[0], alignments[2], score),
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
            possible_alignments.append(self._biopython_formated_str_alignment_to_list(alignment, alignment.score))
        return {'alignments': possible_alignments}

    def _getSimilarity(self, sequence_a, sequence_b, score):
        seqLength = min(len(sequence_a), len(sequence_b))
        return round((score / seqLength) * 100, 2)
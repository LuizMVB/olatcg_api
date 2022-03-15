import base64
import tempfile
from Bio.Align.Applications import ClustalwCommandline
from config import CLUSTALW2_PATH

class PhylogenyModel:
    def getNewickFormat(self, encodedFastaFile):
        decodedFastaFile = base64.b64decode(encodedFastaFile).decode('UTF-8')
        with tempfile.TemporaryDirectory() as outputedFileDir:
            unalignedFastaPath = outputedFileDir + '/unaligned.fasta'
            unalignedFasta = open(unalignedFastaPath, 'w+')
            unalignedFasta.write(decodedFastaFile)
            unalignedFasta.seek(0)
            clustalw2Cline = ClustalwCommandline(CLUSTALW2_PATH, infile=unalignedFastaPath)
            stdout, stderr = clustalw2Cline()
            nwk = open(outputedFileDir + '/unaligned.dnd', 'r').read().replace('\n', '')
        return nwk
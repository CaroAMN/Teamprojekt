import sys
import os
from pyopenms import *

os.system("""ProteomicsLFQ -in BSA1.mzML BSA2.mzML BSA3.mzML -ids BSA1_F1.idXML BSA2_F1.idXML BSA3_F1.idXML  -design experimental_design.tsv -fasta 18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta  -out_cxml BSA.consensusXML.tmp        -out_msstats BSA.csv.tmp        -out BSA.mzTab.tmp
 """)

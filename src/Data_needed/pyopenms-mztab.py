import sys
import os
from pyopenms import *

os.system("""ProteomicsLFQ -in BSA1.mzML BSA2.mzML BSA3.mzML -ids BSA1_OMSSA.idXML BSA2_OMSSA.idXML BSA3_OMSSA.idXML  -design experimental_design.tsv -fasta 18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta -Alignment:max_rt_shift 0    -targeted_only true     -transfer_ids false   -mass_recalibration false              -out_cxml BSA.consensusXML.tmp        -out_msstats BSA.csv.tmp        -out BSA.mzTab.tmp   -threads 1   -proteinFDR 0.3
""")

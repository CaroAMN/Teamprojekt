import sys
import os
from pyopenms import *


class ProteomicsLFQ:

     """
       

       ...

       Attributes
       ----------

       Methods
       -------

       """
    def run_console_ProteomicsLFQ():
        designer = "/home/caro/Documents/Teamprojekt/src/FRACTIONS/BSA_design.tsv"
        fasta_file = "/home/caro/Desktop/18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta"



        os.chdir("/home/caro/Documents/Teamprojekt/src/FRACTIONS")
        os.system("""ProteomicsLFQ -in BSA1_F1.mzML BSA1_F2.mzML BSA2_F1.mzML BSA2_F2.mzML BSA3_F1.mzML BSA3_F2.mzML -ids BSA1_F1.idXML BSA1_F2.idXML BSA2_F1.idXML BSA2_F2.idXML BSA3_F1.idXML BSA3_F2.idXML     -design """ + designer +   """ -fasta """ + fasta_file + """ -ini OpenPepXLLF_input2.ini -out_cxml BSA.consensusXML.tmp -out_msstats BSA.csv.tmp -out BSA.mzTab.tmp -threads 1 -proteinFDR 0.3""")

if __name__ == "__main__":
    ProteomicsLFQ.run_console_ProteomicsLFQ()

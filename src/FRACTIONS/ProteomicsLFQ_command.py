import sys
import os
from pyopenms import *


class ProteomicsLFQ_command: 

    # TODO: man gebe hier die Dateien in die Funktion mit. Also Aufruf von ProteomicsLFQ generisch machen 
    def run_console_ProteomicsLFQ():
        designer = "C:/Users/Alex/Desktop/TeamProjekt-ganzes-Team/src/FRACTIONS/BSA_design.tsv"
        fasta_file = "C:/Users/Alex/Desktop/TeamProjekt-ganzes-Team/src/FRACTIONS/18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta"


        
        os.chdir("/Users/Alex/Desktop/TeamProjekt-ganzes-Team/src/FRACTIONS")
        os.system("""ProteomicsLFQ -in BSA1_F1.mzML BSA1_F2.mzML BSA2_F1.mzML BSA2_F2.mzML BSA3_F1.mzML BSA3_F2.mzML -ids BSA1_F1.idXML BSA1_F2.idXML BSA2_F1.idXML BSA2_F2.idXML BSA3_F1.idXML BSA3_F2.idXML     -design """ + designer +   """ -fasta """ + fasta_file + """ -Alignment:max_rt_shift 0 -targeted_only true -transfer_ids false -mass_recalibration false -out_cxml BSA.consensusXML.tmp -out_msstats BSA.csv.tmp -out BSA.mzTab.tmp -threads 1 -proteinFDR 0.3""")


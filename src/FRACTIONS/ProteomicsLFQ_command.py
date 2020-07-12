import sys
import os
from pyopenms import *
import re


class ProteomicsLFQ_command:

    def run_console_ProteomicsLFQ():

        # extract file path
        path_for_mzTab = os.getcwd()[2:]
        # reverse string
        path_for_mzTab = path_for_mzTab[::-1]
        # remove last entry of the path for the directoy, to replace later on with "FRACTIONS" 
        path_for_mzTab = re.sub(r'^.*?\\', '', path_for_mzTab)

        # re-reverse string
        path_for_mzTab = path_for_mzTab[::-1]

        os.chdir(path_for_mzTab + r"\FRACTIONS")
        os.system("""ProteomicsLFQ -in BSA1_F1.mzML BSA1_F2.mzML BSA2_F1.mzML BSA2_F2.mzML BSA3_F1.mzML BSA3_F2.mzML -ids BSA1_F1.idXML BSA1_F2.idXML BSA2_F1.idXML BSA2_F2.idXML BSA3_F1.idXML BSA3_F2.idXML     -design BSA_design.tsv    -fasta 18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta -Alignment:max_rt_shift 0 -targeted_only true -transfer_ids false -mass_recalibration false -out_cxml BSA.consensusXML.tmp -out_msstats BSA.csv.tmp -out BSA.mzTab.tmp -threads 1 -proteinFDR 0.3""")

    def file_path_mzTab():
        try:
            # generic path to just created mzTab 
            path_to_mzTab = os.getcwd()[2:]
            open(path_to_mzTab + r"\BSA.mzTab.tmp")
            path = path_to_mzTab + r"\BSA.mzTab.tmp"
            return path
        except:
            return "error"

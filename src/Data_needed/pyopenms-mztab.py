import sys
from pyopenms import *

# loading spectrum data
exp = MSExperiment()
MzMLFile().load("BSA1_F1.mzML", exp)
# accessing spectrum data
spectrum_data = exp.getSpectrum(0).get_peaks()
print(spectrum_data)

# loadin protein data form idXML file
protein_ids = []
peptide_ids = []
IdXMLFile().load("BSA1_F1.idXML", protein_ids, peptide_ids)
# each protein/peptide object has Hit object
hits_listpro = protein_ids[0].getHits()
hits_listpep = peptide_ids[0].getHits()
# getting Accession and Sequence from the hit objects
print(hits_listpro[0].getAccession())
print(hits_listpep[0].getSequence())

# searching with databank and mzML File
# Prints result automatically
protein_ids2 = []
peptide_ids2 = []
SimpleSearchEngineAlgorithm().search(
    "BSA1_F1.mzML", "18Protein_SoCe_Tr_detergents_trace_target_decoy.fasta", protein_ids2, peptide_ids2)

# going trough the peptide list and printing MZ + RT from each pephit
for pep_id in peptide_ids2:
    print("the MZ: ", pep_id.getMZ())
    print("the RT: ", pep_id.getRT())

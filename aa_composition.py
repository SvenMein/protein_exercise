#### amino acid composition program ####

# read the protein sequences from the fasta file
# count the different amino acids from the sequences
# print out the name of the protein
# print out the amino acid composition

from collections import Counter 

def read_fasta(gfp.fasta): 
    """ 
    Read a FASTA file and return the sequences. 
    """
    sequences = {} 
    name = None 
    sequence = "" 

    with open(gfp.fasta, "r") as file: 
        for line in file: 
            line = line.strip() 
            if line.startswith(">"): 
                # Save previous sequence 
                if name is not None: 
                    sequences[name] = sequence 
                # Start new sequence 
                name = line[1:] 
                sequence = "" 
            else: 
                sequence += line 
            # Save last sequence 
        if name is not None: 
            sequences[name] = sequence 
    return sequences

def aa_composition(sequence): 
    """ 
    Count how often each amino acid occurs in a protein sequence. 
    """ 
    counts = Counter(sequence) 
    return counts

# Read the FASTA file 
proteins = read_fasta("gfp.fasta")

# Calculate amino acid composition 
for name, sequence in proteins.items():
    composition = aa_composition(sequence) 
    print(name, ": ", composition)
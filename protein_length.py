from Bio import SeqIO


# Read protein sequences from FASTA file
proteins = SeqIO.parse("gfp.fasta", "fasta")


# Calculate and print the length of each protein
for protein in proteins:

    protein_id = protein.id
    protein_length = len(protein.seq)

    print(f"Protein: {protein_id}")
    print(f"Length: {protein_length} amino acids")
    print("-" * 40)
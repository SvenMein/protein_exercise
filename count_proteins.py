from Bio import SeqIO


def count_proteins(fasta_file):
    count = 0

    for protein in SeqIO.parse(fasta_file, "fasta"):
        count += 1

    return count


protein_count = count_proteins("gfp.fasta")

print(f"Number of proteins: {protein_count}")

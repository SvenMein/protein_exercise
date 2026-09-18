def count_proteins(fasta_file):
    count = 0

    with open(fasta_file, "r") as file:
        for line in file:
            if line.startswith(">"):
                count += 1

    return count


protein_count = count_proteins("gfp.fasta")

print("Number of proteins:", protein_count)

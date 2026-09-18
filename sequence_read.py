from Bio import SeqIO


records = []
for rec in SeqIO.parse("gfp.fasta", "fasta"):
    description = rec.description[len(rec.id):].strip()
    records.append({
        "id": rec.id,
        "description": description,
        "sequence": str(rec.seq),
        "length": len(rec.seq),
    })

print(records)


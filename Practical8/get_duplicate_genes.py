import re
def fasta_read(input_file, output_file):
    with open(input_file, 'r', encoding="UTF-8") as infile, \
         open(output_file, 'w', encoding="UTF-8") as outfile:
        gene_name = None
        current_seq = []
        for line in infile:
            if line.startswith('>'):
                if gene_name and current_seq:
                    # Simplify gene names, assuming that the simplification rule is to keep to the first blank or before a specific identifier
                    clean_name = re.sub(r' *[._].*$', '', gene_name.strip())
                    outfile.write(f">{clean_name}_mRNA\n{"".join(current_seq).strip()}\n")
                current_seq.clear()
                gene_name = line.strip('>').strip()
            else:
                current_seq.append(line.strip())
        # Process end-of-file sequences
        if gene_name and current_seq:
            clean_name = re.sub(r' *[._].*$', '', gene_name.strip())
            outfile.write(f">{clean_name}_mRNA\n{"".join(current_seq).strip()}\n")


fasta_read("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "duplicate_genes.fa")

# If you need to validate the output, additionally read the validation
with open('duplicate_genes.fa', 'r', encoding="UTF-8") as of:
    print(of.read())
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
def repeat_count(seq):
    seq1='GTGTGT'
    seq2='GTCTGT'
    count=0
    for i in range(len(seq)):
          if seq[i:i+6]==seq1 or seq[i:i+6]==seq2:
           count+=1

    return count
print(f"Total counts: {repeat_count(seq)}")

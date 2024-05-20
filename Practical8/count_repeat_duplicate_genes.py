import re

def count_repeats(seq, repeat):
    return seq.count(repeat)

def write_sequence(f_out, name, seq, repeat_sequence, repeat_count):
    f_out.write(f">{name}_mRNA (Repeat Count: {repeat_count})\n{seq}\n")

def process_and_extract(input_file, output_file, target_sequence):
    current_sequence = []
    current_name = ''
    
    with open(input_file, 'r', encoding="UTF-8") as f_in, \
         open(output_file, 'w', encoding="UTF-8") as f_out:
        for line in f_in:
            line = line.strip()
            if line.startswith('>'):
                if current_name and current_sequence:  # Processing the previous sequence
                    seq_text = ''.join(current_sequence)
                    repeat_count = count_repeats(seq_text, target_sequence)
                    if repeat_count:
                        write_sequence(f_out, current_name, seq_text, target_sequence, repeat_count)
                current_name = line[1:].split(' ')[0]  # Simplified name processing
                current_sequence = []
            else:
                current_sequence.append(line)
        # Processing the last sequence
        if current_name and current_sequence:
            seq_text = ''.join(current_sequence)
            repeat_count = count_repeats(seq_text, target_sequence)
            if repeat_count:
                write_sequence(f_out, current_name, seq_text, target_sequence, repeat_count)

try:#Attempts to perform sequence extraction processing, outputs the save path when successful, and gives appropriate prompts when the file cannot be found or other exceptions occur.
    target_sequence = input("Enter the repeat sequence to search for (e.g., GTGTGT or GTCTGT): ")
    output_path = f'{target_sequence}_filtered_genes.fa'
    process_and_extract("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", output_path, target_sequence)
    print(f"Processing completed and saved to {output_path}.")
except FileNotFoundError:
    print("The specified input file was not found.")
except Exception as error:
    print(f"An error occurred: {error}")
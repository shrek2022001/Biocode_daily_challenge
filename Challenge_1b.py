import array

# Codon translation table
CODON_TABLE = {
    'AUG': 'Met', 'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'UAU': 'Tyr', 'UAC': 'Tyr',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGG': 'Trp', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu',
    'CUG': 'Leu', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'CAU': 'His',
    'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg',
    'CGG': 'Arg', 'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'ACU': 'Thr', 'ACC': 'Thr',
    'ACA': 'Thr', 'ACG': 'Thr', 'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 'GUU': 'Val', 'GUC': 'Val',
    'GUA': 'Val', 'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 'GGU': 'Gly', 'GGC': 'Gly',
    'GGA': 'Gly', 'GGG': 'Gly', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}

# Function to convert input string into upper case because the codon table is in uppercase
def to_upper(s):
    return s.upper()

# Function to split a string into codons
def split_seq(s):
    return [s[i:i+3] for i in range(0, len(s), 3)]

# Function to translate mRNA to a protein sequence, starting from the first AUG codon
def translate_mrna(mrna: str) -> list[str]:
    # Convert the input mRNA sequence to uppercase to match the codon table keys
    mrna = to_upper(mrna)
    # Find the start codon AUG's index
    start_index = mrna.find('AUG')
    if start_index == -1:
        return []  

    # We split the mRNA from the first AUG into codons
    codons = split_seq(mrna[start_index:])
    proteins = []
    for codon in codons:
        if codon in CODON_TABLE:
            protein = CODON_TABLE[codon]
            if protein == 'STOP':
                break
            proteins.append(protein)
    return proteins

# Example usage
input_string = "augaaaaaaggg"
translated_proteins = translate_mrna(input_string)
print("Translated proteins:", translated_proteins)

from textwrap import wrap
proteinas = {
            'AUG': 'Methionine', 'UUU': 'Phenylalanine',
            'UUC': 'Phenylalanine',
            'UUA': 'Leucine', 'UUG': 'Leucine',
            'UCU': 'Serine', 'UCC': 'Serine',
            'UCA': 'Serine', 'UCG': 'Serine',
            'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
            'UGU': 'Cysteine', 'UGC': 'Cysteine',
            'UGG': 'Tryptophan', 'UAA': 'STOP',
            'UAG': 'STOP', 'UGA': 'STOP',
            }

def proteins(strand):
    result = []
    for codon in wrap(strand,3):
        if proteinas[codon] == 'STOP':
            return result
        else: 
            result.append(proteinas[codon])
    return result
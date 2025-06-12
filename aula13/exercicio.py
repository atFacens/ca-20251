dna = input('Digite o DNA: ')

rna = dna.translate({ord('A'):'U', ord('T'):'A', ord('C'):'G', ord('G'):'C'})

print(rna)
amino_acids_str = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
print(len(amino_acids_str))

first_24_chars = amino_acids_str[0:24]
print(len(first_24_chars))
print("The first 24 characters are", first_24_chars)
with open("lsinsulin-seq-clean.txt","a") as file:
    file.write(first_24_chars)
    
    
next_25_chars = amino_acids_str[23:54]
print(len(next_25_chars))
print("The first 24 characters are", next_25_chars)
with open("bsinsulin-seq-clean.txt","a") as file:
    file.write(next_25_chars)
 
    
another_next_25_chars = amino_acids_str[54:89]
print(len(another_next_25_chars))
print("The first 24 characters are", another_next_25_chars)
with open("csinsulin-seq-clean.txt","a") as file:
    file.write(another_next_25_chars)
    
again_another_next_25_chars = amino_acids_str[89:110]
print(len(again_another_next_25_chars))
print("The first 24 characters are", again_another_next_25_chars)
with open("csinsulin-seq-clean.txt","a") as file:
    file.write(again_another_next_25_chars)
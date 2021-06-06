import random
import json

#Read and translate the codons in the list    
def translate_and_display(codons, codon_file):
    print("-------Amino Acids--------")
    codon_file.write("-------Amino Acids--------")
    codon_file.write('\n')
    
    for i in range(0, len(codons)):
        j = 0
        Found = False
        while(Found == False):
            
            #If the first letter in codons[i] starts with A
            if(codons[i][j] == 'A'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Lysine")
                        codon_file.write(codons[i])
                        codon_file.write(": Lysine \n")
                        Found = True
                    elif(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Asparagine")
                        codon_file.write(codons[i])
                        codon_file.write(" Asparagine \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Arginine")
                        codon_file.write(codons[i])
                        codon_file.write(" Arginine \n")
                        Found = True
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Serine")
                        codon_file.write(codons[i])
                        codon_file.write(": Serine \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] == 'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Threonine")
                        codon_file.write(codons[i])
                        codon_file.write(": Threonine \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'G'):
                        print(codons[i], ": Methionine")
                        codon_file.write(codons[i])
                        codon_file.write(": Methionine \n")
                        Found = True
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Isoleucine")
                        codon_file.write(codons[i])
                        codon_file.write(": Isoleucine \n")
                        Found = True
            
            #If the first letter in codons[i] starts with G
            if(codons[i][j] == 'G'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Glutamic Acid")
                        codon_file.write(codons[i])
                        codon_file.write(": Glutamic Acid \n")
                        Found = True
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Aspartic Acid")
                        codon_file.write(codons[i])
                        codon_file.write(": Aspartic Acid \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Glycine")
                        codon_file.write(codons[i])
                        codon_file.write(": Glycine \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Alanine")
                        codon_file.write(codons[i])
                        codon_file.write(": Alanine \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Valine")
                        codon_file.write(codons[i])
                        codon_file.write(": Valine \n")
                        Found = True
            
            #If the first letter in codons[i] starts with C
            if(codons[i][j] == 'C'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Glutamine")
                        codon_file.write(codons[i])
                        codon_file.write(": Glutamine \n")
                        Found = True
                    if(codons[i][j+2] == 'U' or codons[i][j+2] ==  'C'):
                        print(codons[i], ": Histidine")
                        codon_file.write(codons[i])
                        codon_file.write(": Histidine \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Arginine")
                        codon_file.write(codons[i])
                        codon_file.write(": Arginine \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Proline")
                        codon_file.write(codons[i])
                        codon_file.write(": Proline \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Leucine")
                        codon_file.write(codons[i])
                        codon_file.write(": Leucine \n")
                        Found = True
                        
            #If the first letter in codons[i] starts with U
            if(codons[i][j] == 'U'):
                if(codons[i][j+1] == 'A'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": STOP")
                        codon_file.write(codons[i])
                        codon_file.write(": STOP \n")
                        Found = True
                    if(codons[i][j+2] == 'U' or codons[i][j+2] ==  'C'):
                        print(codons[i], ": Tyrosine")
                        codon_file.write(codons[i])
                        codon_file.write(": Tyrosine \n")
                        Found = True
                if(codons[i][j+1] == 'G'):
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Cysteine")
                        codon_file.write(codons[i])
                        codon_file.write(": Cysteine \n")
                        Found = True
                    if(codons[i][j+2] == 'A'):
                        print(codons[i], ": STOP")
                        codon_file.write(codons[i])
                        codon_file.write(": STOP \n")
                        Found = True
                    if(codons[i][j+2] == 'G'):
                        print(codons[i], ": Tryptophan")
                        codon_file.write(codons[i])
                        codon_file.write(": Tryptophan \n")
                        Found = True
                if(codons[i][j+1] == 'C'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G' or codons[i][j+2] ==  'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Serine")
                        codon_file.write(codons[i])
                        codon_file.write(": Serine \n")
                        Found = True
                if(codons[i][j+1] == 'U'):
                    if(codons[i][j+2] == 'A' or codons[i][j+2] ==  'G'):
                        print(codons[i], ": Leucine")
                        codon_file.write(codons[i])
                        codon_file.write(": Leucine \n")
                        Found = True
                    if(codons[i][j+2] == 'C' or codons[i][j+2] ==  'U'):
                        print(codons[i], ": Phenylalanine")
                        codon_file.write(codons[i])
                        codon_file.write(": Phenylalanine \n")
                        Found = True
                
        
        
        
        
    #Display the number of codons along with writing the number to file results.txt
    codon_file.write('\n')
    print('\n')
    length = len(codons)
    print("Number of Codons: ", length)
    codon_file.write("Number of Codons: ")
    codon_file.write(str(length))
 
    
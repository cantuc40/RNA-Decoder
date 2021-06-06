#CS 1311 Final Project: Codon Extraction
#Objective: Input RNA Sequence, Output RNA Sequence, codons, and amino acids


#Chris Cantu - Extract Codons function, translate and display function, main function
#Eric Dominguez - Generate random RNA sequence function, export json file

import random
import json
from translate_and_display import *
from extract_codons import *

#Create new text file called results.txt
codon_file = open("results.txt" , "w+")



#Main Function. User selects a choice whether to manually input a sequence or generate a string randomly
def main():
    
    choice = "yes"
    while(choice == "yes"):
        print("------RNA Decoder-----")
        print("1. Manual Input")
        print("2. Generate String")
        selection = int(input("Select a number from one to two: "))
        if(selection == 1):
            RNA = input("Type the the RNA using the letters A, U, G, and C: ")
            extract_codons(RNA, codon_file)
        if(selection == 2):
            length = int(input("Type the length of the string: "))
            RNA = generate_string(length)
            print("RNA: ", RNA, '\n')
            codon_file.write("RNA: ")
            codon_file.write(RNA)
            codon_file.write('\n')
            extract_codons(RNA, codon_file)
        
        choice = input("Would you like to try again? Type yes to continue, type no to exit: ")
        
        #If choice equals to yes, the contents in results.txt is erased
        if(choice == 'yes'):
            codon_file.seek(0)
            codon_file.truncate()
    print("results.txt and codons.json has been written into the directory")
    print("Goodbye")
    codon_file.close()
    
            
#Randomly generate an RNA sequence using only the letters A, C, G, and U
def generate_string(N, alphabet='ACGU'):
    return ''.join([random.choice(alphabet) for i in range(N)])
    
    
           

main()


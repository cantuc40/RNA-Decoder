import json
from translate_and_display import *

#Take the RNA sequence and extract every codon that exists        
def extract_codons(RNA, codon_file):
    
    #Initialize Values and create a list called codons
    record = False
    char_1 = char_2 = char_3 = False
    record_off_switch_1 = record_off_switch_2 = record_off_switch_3 = False
    r_1 = r_2 = False
    ch_1 = ch_2 = ch_3 = False
    skip1 = skip2 = False
    record_off_lock = record_on_lock = False
    switch = switch2 = False
    begin_recording = False
    increment = increment2 = True
    skipagain = skipagain2 = False
    codons = []
    
    #Display and write the title into text file results.txt 
    print("----Codons----")
    codon_file.write('\n')
    codon_file.write("----Codons----")
    codon_file.write('\n')
    
    #Extraction begin
    for i in range(0, len(RNA)):
        
        #No codons are recorded 
        if(record == False and begin_recording == False):
            if(switch2 == False):
                #When A is encountered, the number is assigned to start and verification for AUG begins
                if(RNA[i] == 'A'):
                    start = i
                    char_1 = True
                    record_off_lock = True
            if(switch2 == True and record_off_lock == True):
                if(record_off_switch_1 == True and increment == True and skip1 == False):
                    char_2 = True
                if(record_off_switch_1 == record_off_switch_2 == True and increment == True and skip2 == False):
                    char_3 = True
                if(record_off_switch_1 == record_off_switch_2 == record_off_switch_3==True):
                    end = i
                    codon = RNA[start:end]
                    
                    #If codon is AUG, append AUG into list, begin recording                      
                    if(codon == "AUG"):
                        print(codon)
                        codon_file.write(codon)
                        codon_file.write('\t')
                        codons.append(codon)
                        record = True
                        record_off_switch_1 = record_off_switch_2 = record_off_switch_3 = False
                        char_1 = char_2 = char_3 = False
                        record_off_lock = False
                        switch2 = False
                        skip1 = skip2 = False
                    
                    #Else, record is off
                    else:
                        record_off_switch_1 = record_off_switch_2 = record_off_switch_3 = False
                        char_1 = char_2 = char_3 = False
                        record_off_lock = False
                        switch2 = False 
                        skip1 = skip2 = False
                        
            
            
            if(record_off_lock == True and char_1 == True):
                switch2 = True
            if(char_1 == True and record == False):
                record_off_switch_1 = True
                increment = True
            if(char_1 == char_2 == True and record == False):
                record_off_switch_2 = True
                skip1 = True
            if(char_1 == char_2 == char_3 == True and record == False):
                record_off_switch_3 = True
                skip2 = True
            
        #Codons are recorded    
        if(record == True and begin_recording == True):
            if(record_on_lock == False):
                start = i-1
                ch_1 = True
                record_on_lock = True
            if(switch == True and record_on_lock == True):
                if(r_1 == True and increment2 == True and skipagain == False):
                    ch_2 = True
                if(r_1 == r_2 == True and increment == True and skipagain2 == False):
                    end = i
                    codon = RNA[start:end]
                    
                    #if codon is equal to either UGA, UAA, or UAG, append into list, but stop recording
                    if(codon == "UGA" or codon == "UAA" or codon == "UAG"):
                        codons.append(codon)
                        print(codon)
                        codon_file.write(codon)
                        codon_file.write('\t')
                        record = False
                        r_1 = r_2 = False
                        ch_1 = ch_2 = ch_3 = False
                        record_on_lock = False
                        switch = False
                        skipagain = skipagain2 = False
                     
                    #Else, continue recording    
                    else:
                        codons.append(codon)
                        print(codon)
                        codon_file.write(codon)
                        codon_file.write('\t')
                        r_1 = r_2  = False
                        ch_1 = ch_2 = ch_3 = False
                        record_on_lock = False
                        switch = False
                        skipagain = skipagain2 = False
            
           
            if(record_on_lock == True and ch_1 == True):
                switch = True
            if(ch_1 == True and record == True):
                r_1 = True
                increment2 = True
            if(ch_1 == ch_2 == True and record == True):
                r_2 = True
                skipagain = True
            if(ch_1 == ch_2 == ch_3 == True and record == True):
                skipagain2 = True
        
        #Record Switch
        if(record == True):
            begin_recording = True
        if(record == False):
            begin_recording = False     
        
        
        
        
    #Create file called codons.json, which stores and displays the contents of the list codons    
    filename = 'codons.json'
    with open(filename, 'w+') as f_obj:
        json.dump(codons, f_obj)
    print('\n')
    codon_file.write('\n')
    codon_file.write('\n')
    
    #Translate the codon list
    translate_and_display(codons, codon_file)

                     
            
            
            
            
            
            
            
            
            

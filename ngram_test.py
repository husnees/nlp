#This program demonstrates steps to extract n-grams and save it in a file
import re

def ngram():

    #using "with" will close the file immediately after last call
    with open("c:/Users/Public/text-ngram.dat","r") as rfile:
        infile = rfile.readlines()

    unifile = open("c:/Users/Public/unigram.dat","w")
    bifile = open("c:/Users/Public/bigram.dat","w")
    trifile = open("c:/Users/Public/trigram.dat","w")   
    
    sent = [s for s in infile[0].split(".")]
   
    for line in sent:        
        for j in range(len(line.split())-1):
            uni = line.split()[j]
            bi = line.split()[j]+" "+line.split()[j+1]
            
            unifile = open("c:/Users/Public/unigram.dat","a")
            bifile = open("c:/Users/Public/bigram.dat","a")            
            unifile.write(str(uni)+"\n")
            bifile.write(str(bi)+"\n")            
            unifile.close()
            bifile.close()

        for k in range(len(line.split())-2):
            trifile = open("c:/Users/Public/trigram.dat","a")            
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            trifile.write(str(tri)+"\n")
            trifile.close()

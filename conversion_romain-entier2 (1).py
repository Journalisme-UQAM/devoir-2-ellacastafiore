#coding: utf-8

import csv

import re

def find_element_in_list(element, list_element):
    try:
        index_element = list_element.index(element)
        return index_element
    except ValueError:
        return -1



def rom_to_int(string):

    table=[['m',1000],['cm',900],['d',500],['cd',400],['c',100],['xc',90],['l',50],['xl',40],['x',10],['ix',9],['v',5],['iv',4],['i',1]]
    returnint=0
    for pair in table:


        continueyes=True

        while continueyes:
            if len(string)>=len(pair[0]):

                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False

    return returnint


fichier = "concordia1.csv"
f1 = open(fichier)

lignes = csv.reader(f1)



c=0



for ligne in lignes:

    longTitre = (len(ligne[2]))
    
    
    type = ligne[6]
          
    if ((type.find("Ph.") != -1) or type.find("D.") != -1):
         type = "doctorat" 
    elif ((type.find("M.") != -1)):
        type = "maitrise"

    pagaccr = ligne[5]
    #print pagaccr
    pagaccr = pagaccr.split(" ")

#    print pagaccr.index("leaves")

    
    #print str(find_element_in_list("leaves",pagaccr)) + " at " + str(c)
    c = c+1
    romain = rom_to_int(pagaccr[0])
    arabe = 0
    for elem in pagaccr:
        if (elem.isdigit()):
            arabe = int(elem)
            break
        
    nbpage = romain + arabe

    #print(longTitre)
    #print(type)
    #print(nbpage)
    #print("")

    if (c >1):
        article = "Le"

        if (type == "maitrise"):
            article = "La"
        
        print article + " " + type + " de " + ligne[1] + " " + ligne[0] + " compte " + str(nbpage) + " pages. Son titre est <<" + ligne[2] + ">>, comptant " + str(longTitre) + " carateres."
        print("")

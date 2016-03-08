__author__ = 'meldd'
#3.1 compute mirror, 3.2 reverse string, 3.3 verify validity



String2Mirror = "ACTGAT"
String2Mirror = str(input("enter your DNA string."))# "ACTGAT"


def mirrorDNA(String2Mirror):


    MirrorList = list(String2Mirror)  # make a list of the original chain
    print('original chain: ', MirrorList) # print that list
    newchain = []  # make an empty list to store the mirrored chain
    for i in MirrorList:  # for each piece of the chain in the list
        if i == "A" in String2Mirror:  # find the tide
            newchain.append('T')  # append to its mirror
        if i == "T" in String2Mirror:
            newchain.append("A")
        if i == "G" in String2Mirror: # use multiple ifs because if elif doesn't check all conditions
            newchain.append("C")
        if i == "C" in String2Mirror:
            newchain.append("G")
    print('mirrored chain: ', newchain)

mirrorDNA(String2Mirror) # print('mirrored : ',


DnaString = str(input("enter your DNA String."))
def reverseString(DnaString):
    reverseStr= (DnaString [::-1])
    print("reversed: ", reverseStr) # from end to beginning [  beginning, end, step ]
    #print ('reversed string: ', DnaString [::-1]) # prints the string,
reverseString(DnaString)

DnaString=1
def Validify(DnaString):
    import re
    while (True): # HAVE IN WHILE LOOP JUST FOR THIS STAGE SO AS NOT TO KEEP RUNNING
        DnaString = str(input('enter your polynucleotide chain code hooblah'))
        if (re.match('^([ACTG]+[ACTG]*)$', DnaString, flags=0)):
        #all(c in "ACGT" for c in DnaString ): # alternative way to identify correct inputs or not
            #  to match for teh correct bases in the input string using regex
                print ("valid chain.")
        else:
            print("invalid chain, please check your input.")
        if (DnaString.find("end") != -1): # TO EXIT THE LOOP TYPE END
            print("ohokaybye.")
            break
print(Validify(DnaString))
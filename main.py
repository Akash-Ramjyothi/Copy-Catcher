from difflib import SequenceMatcher
with open('code_A.c', errors='ignore') as fileA,open('code_B.c', errors='ignore') as fileB:
    fileAData = fileA.read()
    fileBData = fileB.read()
    similarity = SequenceMatcher(None, fileAData,fileBData).ratio()
    if similarity>0.8:
        print( "Plagiarism is: {0:.2f}".format(similarity*100),"%, Code is Plagiarized.")
    else:
        print("Plagiarism is: {0:.2f}".format(similarity*100),"%, Code is not Plagiarized.")
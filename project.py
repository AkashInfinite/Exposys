file1=open("train_1000label.txt",'r');
line=file1.readlines()
#line=["When is the show happening?","Is there a cab available for airport?"]
label=["what","when","is","will","do","what time"];
for i in line:
    j=i;
    i=i.lower()
    
    if("what time" in i):
        print(j+" Type: when")
    elif("when" in i):
        print(j+" Type: when")
    elif("what" in i):
        print(j+" Type: What")
    elif((i.find('is ')>-1 and i.find('is ')<7) or (i.find('will ')>-1 and i.find('will ')<7) or (i.find('do ')>-1 and i.find('do ')<7)):
        print(j+" Type: Affirmative")
    else:
        print(j+" Type: Unknown")

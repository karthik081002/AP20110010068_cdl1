s=input("enter a string")
v=['a','b']
for i in s:
    if i not in v:
        print("not accepted 'contains character which is not a or b'")
        exit(0)
inti=0
end=0
for i in s:
    if inti==0:
        if(i=='a'):
            inti=1
        else:
            inti=3
    elif inti==1:
        if(i=='a'):
            inti=0
        else:
            inti=2
    elif inti==2:
        if(i=='a'):
            inti=3
        else:
            inti=1
    elif inti==3:
        if(i=='a'):
            inti=2
        else:
            inti=0
if(end==inti):
    print("accepted")
else:
    print("not accepted")
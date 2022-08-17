s=input("enter a string:")
for i in s:
    if(i!='a' and i!='b'):
        print("not Accepted 'contains character which is not a or b'")
        exit()
st=0
for i in s:
    if st==0:
        if i=='a':
            st=1
        else:
            st=3
    elif st==1:
        if i=='a':
            st=2
        else:
            st=3
    elif st==2:
        if i=='a':
            st=2
        else:
            st=3
    elif st==3:
        if i=='a':
            st=1
        else:
            st=4
    elif st==4:
        if i=='a':
            st=1
        else:
            st=4
if st==2 or st==4:
    print("accepted")
else:
    print("not accepted")
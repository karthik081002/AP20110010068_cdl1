class table:
    def __init__(self,address,label,datatype):
        self.address=address
        self.label=label
        self.datatype=datatype

inp=[[] for _ in range(5)]

while True:

    print("\nMenu :\n")
    print("1.Insert the data")
    print("2.Search the data")
    print("3.Display the data")
    print("4.Exit")
    choice=int(input("\nEnter your choice :"))

    

    if choice==1:
        n=int(input("Enter the no of Symbols to be inserted in symbol table :"))
        for i in range(n):
            address=int(input("Enter the address of Symbol :"))
            label=input("Enter the label of Symbol :")
            datatype=input("Enter the datatype of Symbol :")
            print("\n\n")
            ht=len(label)%5
            inp[ht].append(table(address,label,datatype))

    elif choice==2:
        keylabel=input("\nEnter the label to be searched for : ")
        m=len(keylabel)%5
        flag=True
        for i in inp[m]:
            if i.label==keylabel:
                print("\nSymbol Found")
                print("\nAddress :",i.address)
                print("Datatype  :",i.datatype)
                print("Label     :",i.label,"\n\n")
                flag=False
                break
        if flag:
                print("\nSymbol not Found")

    elif choice==3:
        for i in inp:
            for j in i:
                print("\nAddress :",j.address)
                print("Datatype  :",j.datatype)
                print("Label     :",j.label,"\n\n")
    
    elif choice==4:
        print("Program ended")
        break;
        
    else:
        print("Choose valid option ")


class symbol:
    def __init__(self,address,label,datatype):
        self.label=label
        self.address=address
        self.datatype=datatype

    def display(self):
        print("Address    :",self.address)
        print("Label      :",self.label)
        print("Datatype   :",self.datatype)


    def search(self,label):
        
        if self.label==label:
            print("Symbol found")
            print("Address  : ",self.address)
            print("Label    : ",self.label)
            print("Datatype   :",self.datatype)
            return True

        return False



l=[]
while True:
    print("\nMenu:\n")
    print("1.Insert")
    print("2.Search")
    print("3.Display")
    print("4.Exit")
    choice=int(input("\nEnter your choice :"))

    if choice==1:
        n=int(input("\nEnter no of symbols to be inserted :"))
        for i in range(n):
            address=int(input("Enter the address for symbol :"))
            label=input("Enter the label for symbol :")
            datatype=input("Enter the datatype for symbol :")
            print("\n")
            k=symbol(address,label,datatype)
            l.append(k)

    elif choice==2:
        keylabel=input("\nEnter the label to be Searched for :")
        for symbol in l:
            if symbol.search(keylabel):
                break;
        else:
            print("Symbol not found")
            

    elif choice==3:
        if len(l)==0:
            print("Nothing to display")
            continue;
        for i in range(len(l)):
            print("\nSymbol :\n")
            l[i].display()
    elif choice==4:
        print("\nProgram ended")
        break;

    else:
        print("Choose valid option")
       

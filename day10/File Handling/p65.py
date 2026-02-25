with open("notes.txt","w") as file:
    note = input("enter a note: ")
    file.write(note)
    for i in range(2):
        note = input("enter a note: ")
        file.write("\n"+note)
with open("notes.txt","r") as file:    
    print(file.read())
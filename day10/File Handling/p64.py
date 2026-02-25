with open("bts.txt","w") as file:
    file.write("kim namjoon\n")
    file.write("kim taehyung\n")
    file.write("jeon jungkook\n")
    file.write("park jimin\n")
    file.write("min yoongi\n")
    file.write("kim seokjin\n")
    file.write("jung hoseok\n")
with open("bts.txt","r") as file:
    content=file.read()
    print(content)
with open("bts.txt","a") as file:
    file.write("\n v is handsome")
with open("bts.txt","r") as file:
    content=file.read()
    print(content)
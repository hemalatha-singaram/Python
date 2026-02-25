def search_in_file(file_name,word):
    with open(file_name,"r") as file:
        for line in file:
            if word in line:
                return True
    return False
search_in_file("bts.txt","v")
search_in_file("bts.txt","taylor swift")
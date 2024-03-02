with open("file1.txt","r+") as myfile: #r for read, w for write, a for append, r+ for read and write
    print (myfile.read())
    myfile.write("i am fine")
    myfile.close()

f = open("Mydata",'r')
#print(f.readline())
#print(f.readline(2)) # prints 2 charecters in that line

f1 = open("abc", 'w')

for data in f:  # writes data from Mydata to abc file
    f1.write(data)

#for data in f:     # reads the Mydata file and prints it
  #  print(data)

# We can also copy an image from one file to another as below:
#example:
file1 = open("IMG1",'rb') # rb stands for read binary as image contains the binary values and not charecters
file2 = open("IMG_copy",'wb') # wb stands for write binary used to write binary values to the new file
for i in file1:  # this for-loop copies the image file from old to new file
    file2.write(i)
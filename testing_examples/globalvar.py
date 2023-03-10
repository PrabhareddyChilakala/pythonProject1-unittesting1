'''global y
y=30
def demo():
    y=5
    print(y)
demo()
print(y)'''
#we can access global variables for the entire program
#when we change value of global variable in function it can change
'''**************************************************************'''
import os
dir="../testing_examples"
files=os.listdir(dir)
for f in files:
    print(f.title())
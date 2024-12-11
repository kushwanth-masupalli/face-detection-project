from register import *
from train_recognizer import *

while(True):
    a = int(input("enter :0  for registration 1 for taking attendence 3 for exit"))
    if(a==3):
        break
    elif a==1 :
        register()
    else :
        prepare_images()
        train_recognizer()

        

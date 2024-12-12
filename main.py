from taking_attendence import test_recognizer
from register import register
from train_recognizer import prepare_images,train_recognizer

from converting_to_excel import create_excel
while(True):
    a = int(input("enter :0  for registration 1 for taking attendence 3 for exit"))
    if(a==2):
        break
    elif a==0 :
        register()
    else :
        prepare_images()
        train_recognizer()
        test_recognizer()
        create_excel()
        print("successfully attendence taken")
    

        

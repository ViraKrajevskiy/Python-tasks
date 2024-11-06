import json

def user_input():
    user_email = input("Enter your email adress: ")
    user_password = input("Enter your password: ")

    with open('user_regist.json','r' )as f:
        data = json.load(f)
    







import json
import random
check = False
print("welcome to the quiz")
print("for login enter-1\nfor signup enter-2")
choice=int(input("login or signup: "))
if choice!=1 and choice!=2:
    print("invalid choice")
def login():
    global user_name,password,check
    user_name=input("enter username: ")
    password=input("enter password: ")
    with open('details1.csv', 'r') as f:
        readable=f.read()
        lines=readable.splitlines()
        user=list(filter(lambda l:l.split(",")[0]==user_name and l.split(",")[1]==password,lines)) 
        if user:
            print("Login successful")
            check="yes"
        else:
            print("Login failed. Wrong Username or Password.")
            check="no"
        f.close()
def signup():
    global user_name,password,check,re
    user_name=input("enter username: ")
    with open('u.txt', 'r') as f:
        readable=f.read()
        lines=readable.splitlines()
        user=list(filter(lambda l: user_name,lines)) 
    if user_name not in user:
        user.append(user_name)
    else:
        print("username already exists enter a new username")
        while user_name in user:
            user_name=input("enter username: ")
            if user_name not in user:
                break
        user.append(user_name)
    password=input("enter password: ")
    cpassword=input("re-enter password: ")
    if(password == cpassword):
        print("Registration successfully.")
        u=open("u.txt","a")
        u.write(user_name+"\n")
        u.close()
        with open('details1.csv', 'a') as f:      
            f.write("\n" + user_name + "," + password)
        check="yes" 
        re="yes"  
    else:
        print("Registration failed! Please confirm your Password correctly.")
        check="no"
        re="no"
if choice==1:
    login()
if choice==2:
    signup()
    if re=="yes":
        print("login again")
        login()
if check=="yes":
    fp=open("quiz_questions.json","rb")
    quiz_questions=json.load(fp)
    print("for python quiz enter-1\nfor social quiz enter-2\nfor sports quiz enter-3")
    your_choice=input("Enter your choice(python_quiz/social_quiz/sports_quiz):")
    list_ques= quiz_questions[your_choice]
    score=0
    for i in range(20):
        k= random.choice(list_ques)
        list_ques.remove(k)
        question=""
        for i in k:
            print(i)
            question=i
            for options in k[question][0]:
                print(options)
            l=['a','b','c','d']
            answer=input()
            if answer not in l:
                while answer not in l:
                    print("invalid option enter correct option")
                    answer=input()
                    if answer in l:
                        break
            if answer==k[question][1]:
                score+=1
    if your_choice=='1':
        print("PYTHON SCORE BOARD:")
        s=open("python_score.txt","a")
        s.write(user_name+":"+str(score)+"\n")
        s.close()
        print(user_name,":",score)
        print("do you want to view other user scores\nif yes enter-1\nif no enter-2")
        view=input()
        if view=='1':
            s=open("python_score.txt","r")
            r=s.read()
            s.close()
            print(r)
            print("quiz completed")
        elif view=='2':
            print("quiz completed")
        else:
            print("invalid option")
    if your_choice=='2':
        print("SOCIAL SCORE BOARD:")
        s=open("social_score.txt","a")
        s.write(user_name+":"+str(score)+"\n")
        s.close()
        print(user_name,":",score)
        print("do you want to view other user scores\nif yes enter-1\nif no enter-2")
        view=input()
        if view=='1':
            s=open("social_score.txt","r")
            r=s.read()
            s.close()
            print(r)
            print("quiz completed")
        elif view=='2':
            print("quiz completed")
        else:
            print("invalid option")
    if your_choice=='3':
        print("SPORTS SCORE BOARD:")
        s=open("sports_score.txt","a")
        s.write(user_name+":"+str(score)+"\n")
        s.close()
        print(user_name,":",score)
        print("do you want to view other user scores\nif yes enter-1\nif no enter-2")
        view=input()
        if view=='1':
            s=open("sports_score.txt","r")
            r=s.read()
            s.close()
            print(r)
            print("quiz completed")
        elif view=='2':
            print("quiz completed")
        else:
            print("invalid option")
    print("please give your feedback")
    f=input("enter your feedback: ")
    a=open("feedback.txt","a")
    a.write(user_name+"-"+f+"\n")
else:
    print("compile again")
import json
import re
import time
class quizmania():


    fp=open('quizdata.json','r')
    content=fp.read()
    quizData=json.loads(content)

    dp=open('superusers.json','r')
    content1=dp.read()
    superUsers=json.loads(content1)


    kp=open('users.json','r')
    content2=kp.read()
    users=json.loads(content2)


    pp=open('quizattempties.json','r')
    content3=pp.read()
    quizattempties=json.loads(content3)

    #superUsers={'sk@gmail.com':['skp','sk','9999999999']}
    #users={'dk@gmail.com':['dkp','dk','9999999999']}    
    #quizattempties={'history':[]}
    @classmethod
    def register(cls,kind='user'):
        print("----REGISTRATION PAGE----")
        usertype=kind
        print("Enter your email: ")
        email=input()
        pwd=input("Enter your password: ")
        mobmatch='^[0-9]{10}$'
        mloop=False
        while(mloop==False):        
            mob=input("Enter the mobile no: ")
            if re.match(mobmatch,mob):
                mloop=True
            else:
                print('Enter mobile no correctly')
        name=input("Enter the name: ")        
        if usertype=='super':
            cls.superUsers[email]=[pwd,name,mob]
            print("superUser added successfuly")
            dump_data1=json.dumps(cls.superUsers)
            ep=open('superusers.json','w')
            ep.write(dump_data1)
            ep.close()
        else:
            if email in cls.users:
                print("Email id already exists")
            else:
                cls.users[email]=[pwd,name,mob]
                print("User added successfully")
                dump_data2=json.dumps(cls.users)
                qp=open('users.json','w')
                qp.write(dump_data2)
                qp.close()
    @classmethod
    def superUsersPage(cls):
        userid=input("Enter your email address: ")
        if userid in cls.superUsers:
            pwd=input("Enter your password: ")
            if cls.superUsers[userid][0]==pwd:
                # print("---SuperUser page---")
                # print("Button        Function")
                # print("-----------------------")
                # print("1             Create new Super user")
                # print("2             Set up new quiz")
                # print("3             Edit a quiz")
                # print("4             superUser logout")
                inp1loop=False
                while(inp1loop==False):
                    print("---SuperUser page---")
                    print("Button        Function")
                    print("-----------------------")
                    print("1             Create new Super user")
                    print("2             Set up new quiz")
                    print("3             Edit a quiz")
                    print("4             View quizes")
                    print("5             View Test taker's")
                    print("6             superUser logout")
                    inp1=input("Enter any fuction button: ")
                    if inp1 not in ['1','2','3','4','5','6']:
                        print("Wrong input")
                    else:
                        #inp1loop=True
                        if inp1=='1':
                            kind='super'
                            cls.register(kind)
                        elif inp1=='2':
                            topic1=input("Enter the topic: ").lower()
                            if topic1 not in cls.quizData.keys():
                                cls.quizData[topic1]={'hard':[],'medium':[],'easy':[]}
                                cls.quizattempties[topic1]=[]
                            else:
                                print("Topic already exist. Adding new questions")


                            addqst=False
                            while(addqst==False):                                
                                qst=input('Enter the question: ')
                                a=input("Option a: ")
                                b=input("Option b: ")
                                c=input("Option c: ")
                                d=input("Option d: ")
                                qsttst=False
                                while(qsttst==False):
                                    answer=input("Enter the correct option: ")
                                    if answer.lower() not in ['a','b','c','d']:
                                        print("Enter the option correctly")
                                    else:
                                        qsttst=True
                                print("Enter difficulty level")
                                print("Button      Function")
                                print("--------------------")
                                print("1:           Hard")
                                print("2:           Medium")
                                print("3:           Easy")
                                hardtst=False
                                while(hardtst==False):
                                    difficulty=input("Enter the Button: ")
                                    if difficulty not in ['1','2','3']:
                                        print("Enter the option correctly")
                                    else:
                                        hardtst=True
                                        if difficulty=='1':
                                            diff='hard'                                        
                                        elif difficulty=='2':
                                            diff='medium'
                                        else:
                                            diff='easy'
                                cls.quizData[topic1][diff].append([qst,{'a':a,'b':b,'c':c,'d':d},answer])
                                nextqst=input("Press 1 if you need to enter another question: ")
                                if nextqst !='1':
                                    addqst=True
                        elif inp1=='3':
                            print("-------QUIZ EDITING PAGE-------")
                            print("Choose topic you want to edit")
                            for topic in cls.quizData:
                                print(topic.capitalize())
                            edittst=False
                            while(edittst==False):
                                topic2=input("Enter th topic: ")
                                if topic2.lower() not in cls.quizData:
                                    print("No such topic exist. Enter topic correctly")
                                else:
                                    edittst=True
                                    print("Press 1 to delete the topic completetely")
                                    print("Press any other key to see other options")
                                    topicdelete=input()
                                    if topicdelete=='1':
                                        print("topic deleted successfully")
                                        cls.quizData.pop(topic2)
                                    else:

                                        # print("Do you want to edit question-wise or difficulty-wise")
                                        # print("press 1 for question-wise")
                                        # print("press 2 for difficulty-wise")
                                        # edittype=input()
                                        n=1
                                        qstcount={}
                                        for diff in cls.quizData[topic2]:
                                            n1=0
                                            for question in cls.quizData[topic2][diff]:
                                                print(n,')',question[0],'Difficulty:',diff)
                                                qstcount[str(n)]=[diff,n1]
                                                print('a)',question[1]['a'])
                                                print('b)',question[1]['b'])
                                                print('c)',question[1]['c'])
                                                print('d)',question[1]['d']) 
                                                print("Correct answer: ",question[2])
                                                n+=1          
                                                n1+=1
                                        print("Enter 1 to add new question")
                                        print("Enter 2 to edit existing question")                                        
                                        test11=False
                                        while(test11==False):
                                            newinput=input()
                                            if newinput not in ['1','2']:
                                                print("Enter correctly")
                                            else:
                                                test11=True                                                
                                                if newinput=='1':
                                                    test12=False
                                                    while(test12==False):
                                                        qst=input('Enter the question: ')
                                                        a=input("Option a: ")
                                                        b=input("Option b: ")
                                                        c=input("Option c: ")
                                                        d=input("Option d: ")
                                                        qsttst=False
                                                        while(qsttst==False):
                                                            answer=input("Enter the correct option: ")
                                                            if answer.lower() not in ['a','b','c','d']:
                                                                print("Enter the option correctly")
                                                            else:
                                                                qsttst=True
                                                        print("Enter difficulty level")
                                                        print("Button      Function")
                                                        print("--------------------")
                                                        print("1:           Hard")
                                                        print("2:           Medium")
                                                        print("3:           Easy")
                                                        hardtst=False
                                                        while(hardtst==False):
                                                            difficulty=input("Enter the Button: ")
                                                            if difficulty not in ['1','2','3']:
                                                                print("Enter the option correctly")
                                                            else:
                                                                hardtst=True
                                                                if difficulty=='1':
                                                                    diff='hard'                                        
                                                                elif difficulty=='2':
                                                                    diff='medium'
                                                                else:
                                                                    diff='easy'
                                                        cls.quizData[topic2][diff].append([qst,{'a':a,'b':b,'c':c,'d':d},answer])
                                                        print("Do you want to add another question. If yes press 1")
                                                        kkinput=input()
                                                        if kkinput!='1':
                                                            test12=True

                                                    pass
                                                elif newinput=='2':                                                    
                                                    test1=False
                                                    while(test1==False):                             
                                                        qstinput=input("Enter question no you want to edit")
                                                        if qstinput not in qstcount:
                                                            print("Enter question number correctly")
                                                        else:
                                                            test1=True
                                                            # quizdata['history'][qstcount[sk][0]][qstcount[sk][1]][0]
                                                            # print(cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][0])
                                                            editqstn=cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]]
                                                            print(editqstn[0])
                                                            for pair in editqstn[1].items():
                                                                print(pair[0],')',pair[1])
                                                            print("Answer",editqstn[2])
                                                            print("----------------------")
                                                            test2=False
                                                            while(test2==False):
                                                                # print("Button           Function")
                                                                # print("   1             Edit question ")
                                                                # print("   2             Edit options")
                                                                # print("   3             Edit answer")
                                                                # print("   4             Delete question")
                                                                # print("   5             Exit edit window")
                                                                # #print("Enter your button")
                                                                # test3=False
                                                                # while(test3==False):
                                                                print("Button           Function")
                                                                print("   1             Edit question ")                                                
                                                                print("   2             Edit options")
                                                                print("   3             Edit answer")
                                                                print("   4             Delete question")
                                                                print("   5             Exit edit window")
                                                                editinput=input("Enter your button: ")
                                                                if editinput not in ['1','2','3','4','5']:
                                                                    print("Enter correct button")
                                                                else:
                                                                    #test3=True
                                                                    if editinput=='1':
                                                                        newqstn=input("Enter the question: ")
                                                                        cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][0]=newqstn                                                    
                                                                    elif editinput=='2':
                                                                        test4=False
                                                                        while(test4==False):
                                                                            
                                                                            print("Enter option to edit [a,b,c,d]:")  
                                                                            print("Enter 1 to exit option edit")                                                          
                                                                            option=input()
                                                                            if option not in ['a','b','c','d','1']:
                                                                                print("Enter option correctly")
                                                                                print("Enter 1 to exit option edit")  
                                                                            else:                                                                    
                                                                                if option=='a':
                                                                                    newa=input("Enter option a: ")
                                                                                    cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][1]['a']=newa
                                                                                    
                                                                                elif option=='b':
                                                                                    newb=input("Enter option b: ")
                                                                                    cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][1]['a']=newb
                                                                                    
                                                                                elif option=='c':
                                                                                    newc=input("Enter option c: ")
                                                                                    cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][1]['a']=newc
                                                                                    
                                                                                elif option=='d':
                                                                                    newd=input("Enter option d: ")
                                                                                    cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][1]['a']=newd
                                                                                    
                                                                                else:
                                                                                    test4=True



                                                                        pass
                                                                    elif editinput=='3':
                                                                        test6=False
                                                                        while(test6==False):
                                                                            newanswer=input("Correct answer: ")
                                                                            if newanswer.lower() not in ['a','b','c','d']:
                                                                                print("Enter the option correctly")
                                                                            else:
                                                                                test6=True
                                                                                cls.quizData[topic2][qstcount[qstinput][0]][qstcount[qstinput][1]][2]=newanswer
                                                                        
                                                                    elif editinput=='4':
                                                                        cls.quizData[topic2][qstcount[qstinput][0]].pop(qstcount[qstinput][1])
                                                                        print("Question deleted")
                                                                        
                                                                    elif editinput=='5':
                                                                        test2=True
                                                            
                        elif inp1=='4':
                            print("----LIST OF QUIZES----")
                            print("Quiz Topics")
                            print("-----------")
                            for top in cls.quizData:
                                print(top)
                            print("-----------") 
                            test7=False
                            while(test7==False):                          
                                viewtopic=input("Enter topic you want to see: ")
                                if viewtopic.lower() not in cls.quizData:
                                    print("Enter the topic correctly")
                                else:
                                    test7=True
                                    nv=0
                                    for diff in cls.quizData[viewtopic]:                                            
                                            for question in cls.quizData[viewtopic][diff]:
                                                print(nv,')',question[0],'Difficulty:',diff)
                                                print('a)',question[1]['a'])
                                                print('b)',question[1]['b'])
                                                print('c)',question[1]['c'])
                                                print('d)',question[1]['d']) 
                                                print("Correct answer: ",question[2])                                             
                                                nv+=1   
                                    
       
                                    time.sleep(2)

                        elif inp1=='5':
                            for section in cls.quizattempties:
                                count=1
                                print("-----Topic-----")
                                print("No     Email     Score    Percentage")
                                for attentie in cls.quizattempties[section]:
                                    print(count,attentie[0],'     ',attentie[1],'     ',attentie[2])

                            
                        elif inp1=='6':
                            print("Logged out successfully")
                            dump_data=json.dumps(cls.quizData)
                            jp=open('quizdata.json','w')
                            jp.write(dump_data)
                            jp.close()
                            inp1loop=True




                
                
                
            else:
                print("Incorrect password")
        else:
            print("No user with this email exists")

    @classmethod
    def user(cls):
        print("-------USER PAGE-------")        
        user=input("Enter email address: ")
        if user not in cls.users:
            print("Email address do not exist")
        else:
            password=input("Enter password: ")
            if cls.users[user][0]!=password:
                print("Incorrect password")
            else:
                test8=False
                while(test8==False):                    
                    print("--------------")
                    print("Button      Function")
                    print("  1         Show topic")
                    print("  2         Logout")
                    quizinp=input("Enter the button: ")
                    if quizinp not in ['1','2']:
                        print("Enter button correctly")
                    else:
                        if quizinp=='1':
                            print("---QUIZ TOPICS---")
                            for to in cls.quizData:
                                print(to)
                            print("----------")
                            test9=False
                            while(test9==False):
                                attempt=input("Enter the topic: ")
                                if attempt.lower() not in cls.quizData:
                                    print("Enter topic correctly")
                                else:
                                    test9=True
                                    print("----QUIZ SECTION----")
                                    answers=[]
                                    optionselected=[]
                                    nf=1
                                    for diff in cls.quizData[attempt]:                                            
                                            for qs in cls.quizData[attempt][diff]:
                                                print(nf,')',qs[0])
                                                print('a)',qs[1]['a'])
                                                print('b)',qs[1]['b'])
                                                print('c)',qs[1]['c'])
                                                print('d)',qs[1]['d'])
                                                print("enter 's' to skip question")
                                                print("Enter your option")
                                                test10=False
                                                while(test10==False):
                                                    answer=input()
                                                    if answer.lower() not in ['a','b','c','d','s']:
                                                        print("Invalied entry")
                                                    else:
                                                        if answer=='s':
                                                            optionselected.append("Not answered")
                                                        else:
                                                            optionselected.append(answer)
                                                        test10=True
                                                        if answer==qs[2]:
                                                            answers.append(True)
                                                        elif answer=='s':
                                                            answers.append(0)
                                                        else:
                                                            answers.append(False)


                                                nf+=1
                                    correct=answers.count(True)
                                    wrong=answers.count(False)
                                    unanswered=answers.count(0)
                                    score=(correct*1)-(wrong*0.25)
                                    totalmarks=len(answers)
                                    percentage=round(((score/totalmarks)*100),2)
                                    print("Calculating final score......")
                                    time.sleep(1)
                                    print("Totalmarks: ",totalmarks)
                                    print("Your score: ",score)
                                    print("Percentage: ",percentage)
                                    cls.quizattempties[attempt].append([user,score,percentage])
                                    print("Question sheet")
                                    time.sleep(3)
                                    ng=0
                                    for diff in cls.quizData[attempt]:                                            
                                            for qs in cls.quizData[attempt][diff]:
                                                print(ng+1,')',qs[0])
                                                print('a)',qs[1]['a'])
                                                print('b)',qs[1]['b'])
                                                print('c)',qs[1]['c'])
                                                print('d)',qs[1]['d'])
                                                print("Correct answer: ",qs[2])
                                                print("Option marked: ",optionselected[ng])
                                                ng+=1



                        elif quizinp=='2':
                            test8=True
                            print("Logged out successfully")
                            dump_data3=json.dumps(cls.quizattempties)
                            ip=open('quizattempties.json','w')
                            ip.write(dump_data3)
                            ip.close()


    

def main():
    foo = quizmania()
    foo.user()
    


if __name__ == "__main__":
    main()
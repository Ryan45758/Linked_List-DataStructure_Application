import json
import sys

try:
    with open('data.json','r') as json_data:    #讀data.json檔
        data = json.load(json_data)
except FileNotFoundError:               #例外處理:FileNotFoundError
    print('File not found!\n')

def print_list():
    count = 0
    print("學生列表")
    print('%-15s %-15s' % ('NAME', 'NUMBER'))
    ## print the line -------------------------
    for i in range(25):
        print('-', end='')
    print()
    for i in range(len(data['姓名/學號'])):
        print('%-17s %-15d' %(data['姓名/學號'][i][0],data['姓名/學號'][i][1]))
        count = count + 1
    for i in range(25):
        print('-', end='')
    print()
    print('Total %d record(s) found\n' % count)


class UserData:                             
    def __init__(self,name,number,friendList,postsList):
        self.name = name
        self.number = number
        self.friendList = friendList
        self.postsList = postsList
        self.next = None
        
class Post:
    def __init__(self,postNumber,likesList):
        self.postNumber = postNumber
        self.likesList = likesList
        self.next = None
        
userPtr = UserData(None,None,None,None)        
userCurrent =UserData(None,None,None,None)  
userPrev = UserData(None,None,None,None)  
userHead = UserData(data['姓名/學號'][0][0],data['姓名/學號'][0][1],data['朋友清單']['1'],data['發表過的文章編號']['1'])


postPtr = Post(None,None)
postCurrent = Post(None,None)
postPrev = Post(None,None)
postHead = Post('1A',data['文章按讚表']['1A'])

def creatUserList():
    global userCurrent
    global userPrev
    global userHead
    global userPtr
    
    for i in range(len(data['姓名/學號'])):
        j=i+1
        userCurrent = UserData(data['姓名/學號'][i][0],data['姓名/學號'][i][1],data['朋友清單']['%s' %j],data['發表過的文章編號']['%s' %j])
        if i==0:
            userPtr.next = userHead
            userHead.next = userCurrent
        else:
            userPrev.next = userCurrent
        userCurrent.next = None
        userPrev = userCurrent
    
def creatUserPostList():
    global postPtr
    global postCurrent
    global postPrev
    global postHead
    
    for i in range(len(data['姓名/學號'])):
        k=i+1
        for j in range(len(data['發表過的文章編號']['%s' %k])):
            a=data['發表過的文章編號']['%s' %k][j]
            postCurrent =Post( str(data['發表過的文章編號']['%s' %k][j]),data['文章按讚表']['%s' %a])
            if a=='1A':
                postPtr.next = postHead
                postHead.next = postCurrent
            else:
                postPrev.next = postCurrent
            postCurrent.next = None
            postPrev = postCurrent
    
def displayUserList():          #return 搜尋到的節點
    global userHead
    global userCurrent
    count = 0
    userCurrent = userHead.next
    while userCurrent != None:
        print ("姓名:",userCurrent.name,"學號:",userCurrent.number,"朋友清單:",userCurrent.friendList,"發表過的文章編號:",userCurrent.postsList,"\n")
        count = count +1
        userCurrent = userCurrent.next
    print("\n",count,"個人")
    
def displayUserPostList():
    global postHead
    global postCurrent  
    count = 0
    postCurrent = postHead.next
    while postCurrent != None:
        print("文章編號:",postCurrent.postNumber,"文章按讚表:",postCurrent.likesList)
        count = count + 1
        postCurrent = postCurrent.next
    print("\n",count,"篇文章")
    
def searchUser(name_user):
    global userHead
    global userCurrent    
    
    userCurrent = userHead.next
    while userCurrent != None:
        if name_user.isdigit():
            if userCurrent.number == int(name_user):
                return userCurrent
                break
        elif userCurrent.name == str(name_user):
            return userCurrent
            break

        userCurrent = userCurrent.next
    print("無此用戶資料")
    return False

def searchUser_relation(name_user):
    global userHead
    global userCurrent    
    
    userCurrent = userHead.next
    while userCurrent != None:
        if userCurrent.name == name_user or userCurrent.number == name_user:
            return userCurrent
            break
        userCurrent = userCurrent.next
    print('無此USER')
    return False

def searchAuthor(id_Article):

    global userHead
    global userCurrent
    
    userCurrent = userHead.next
    while userCurrent != None:
        if id_Article in userCurrent.postsList:
            return userCurrent
            break
        userCurrent = userCurrent.next
    print("無此篇文章")
    return False
    
def searchPost(id_Article):
    global postHead
    global postCurrent      
    
    postCurrent = postHead.next
    while postCurrent != None:
        if postCurrent.postNumber == id_Article:
            return postCurrent
            break
        postCurrent = postCurrent.next
    print("無此篇文章\n")
    return False
def searchPraise(number):
    global postHead
    global postCurrent 
    
    postCurrent = postHead.next
    while postCurrent != None:
        if number in postCurrent.likesList:
            print(postCurrent.postNumber," ")
        postCurrent = postCurrent.next
    print("\n\n")
    
def intersection(number):

    relation = []
    a =[]
    for i in range(1,31):
        if i == number:
            continue
        count = 0
        for j in range(len(data['朋友清單']['%s' %number])):
            if data['朋友清單']['%s' %number][j] in data['朋友清單']['%s' %i]:
                count = count + 1
        a.append(count)
        relation.append([i,count])
    print("\n關係最密切1:\n",relation[a.index(max(a))][0],"號，共同好友",relation[a.index(max(a))][1],"個")
    a.remove(a[a.index(max(a))])
    relation.remove(relation[a.index(max(a))])
    print("關係最密切2:\n",relation[a.index(max(a))][0],"號，共同好友",relation[a.index(max(a))][1],"個\n")

        
def main():
    creatUserList()
    creatUserPostList()
    print_list()
    while True:
        print('**************功能選單***************')
        print('        <1> 對文章按讚           ')
        print('        <2> 取消按讚過的文章           ')
        print('        <3> 顯示學生按過讚的文章 ')
        print('        <4>顯示該文章有哪些人按過讚')
        print('        <5>顯示關係最密切的兩人')
        print('        <6>離開程式')
        print('*************************************')
        
        try:
            option = int(input('請輸入(1~6)選擇功能 : '))
        except ValueError:
            print('輸入錯誤')
            print('請重新輸入\n')
        if option == 1:
            UserInputName = input('請輸入您的姓名或學號:')
            target_user = searchUser(UserInputName)
            if target_user == False:
                continue
            UserInputArticle = input('請輸入想按讚的文章編號:')
            target_author = searchAuthor(UserInputArticle)
            
            if target_author == False:
                continue
            
            if target_author.number in target_user.friendList:      #判斷是否為朋友
                target_post = searchPost(UserInputArticle)
                if target_user.number in target_post.likesList:
                    print("你們是朋友且你已經按過贊了\n\n")
                    continue

                print("\n\n你們是朋友可以按讚\n原先按讚人數:",target_post.likesList)
                target_post.likesList.append(target_user.number)
                print("後來按讚人數:",target_post.likesList,"\n\n")
            else:
                print("不是朋友,無權限")
                
        elif option == 2:
            UserInputName = input('請輸入您的姓名或學號:')
            target_user = searchUser(UserInputName)
            if target_user == False:
                continue
            UserInputArticle = input('請輸入想取消讚的文章編號:')
            target_author = searchAuthor(UserInputArticle)
            
            if target_author == False:
                continue
            try:
                
                if target_author.number in target_user.friendList:      #判斷是否為朋友
                    target_post = searchPost(UserInputArticle)
                    print("\n\n你們是朋友可以取消讚\n原先按讚人數:",target_post.likesList)
                    target_post.likesList.remove(target_user.number)
                    print("取消後的按讚人數:",target_post.likesList,"\n\n")
                else:
                    print("不是朋友,無權限")
            except ValueError:
                print("你本來就沒有對該篇文章按讚哦!\n")
            
        elif option == 3:
            UserInputName = input('請輸入您的姓名或學號:')
            target_user = searchUser(UserInputName)
            if target_user == False:
                continue
            print("\n您所按過讚的文章如下:")
            searchPraise(target_user.number)
            
        elif option == 4:
            UserInputArticle = input('請輸入文章編號:')
            target_post = searchPost(UserInputArticle)
            if target_post == False:
                continue
            print("\n\n此篇文章按讚資訊",target_post.likesList)
            
        elif option == 5:
            UserInputName = input('請輸入您的姓名或學號:')  
            target_user = searchUser(UserInputName)
            if target_user == False:
                continue
            intersection(target_user.number)
        
        elif option == 6:
            sys.exit(0)
            
main()







    

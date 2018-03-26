import itchat
import time

itchat.auto_login(True)
friendList = itchat.get_friends(update=True)[0:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    print(friend['DisplayName'])
    print(friend['NickName'])
    print(friend['UserName'])
    time.sleep(.5)

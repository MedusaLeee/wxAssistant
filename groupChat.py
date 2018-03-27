import random
import itchat
import time
from itchat.content import *

groupName = '测试1'


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    time.sleep(random.randrange(15, 50))
    msg.user.send('收到私聊消息，发送人为：%s，类型为：%s，内容为：%s' % (msg.user.nickName, msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    if msg.user.nickName == groupName:
        msg.download('./resources/' + msg.fileName)
        time.sleep(random.randrange(15, 50))
        replyStr = '收到群（%s）附件消息，附件已下载，发送人为：%s，文件类型：%s，文件名：%s' % (msg.user.nickName, msg.actualNickName, msg.type, msg.fileName)
        msg.user.send(replyStr)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    time.sleep(random.randrange(15, 50))
    msg.user.send('Hi，你好，我叫你不知道的我都知道！')


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def text_reply(msg):
    print(msg)
    if msg.user.nickName == groupName:
        time.sleep(random.randrange(15, 50))
        msg.user.send('收到群（%s）消息，发送人为：%s，类型为：%s，内容为：%s' % (msg.user.nickName, msg.actualNickName, msg.type, msg.text))


itchat.auto_login(True, enableCmdQR=2)
itchat.run(True)

import itchat
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    msg.user.send('收到私聊消息，发送人为：%s，类型为：%s，内容为：%s' % (msg.user.nickName, msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    msg.download(msg.fileName)
    msg.user.send('附件已下载，发送人为：%s，文件类型：%s，文件名：%s' % (msg.actualNickName, msg.type, msg.fileName))


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Hi, 你好，我叫你不知道的我都知道!')


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def text_reply(msg):
    msg.user.send('收到群消息，发送人为：%s，类型为：%s，内容为：%s' % (msg.actualNickName, msg.type, msg.text))


itchat.auto_login(True)
itchat.run(True)

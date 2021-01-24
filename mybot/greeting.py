from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
   TextSendMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate,MessageAction, VideoSendMessage
)
line_bot_api = LineBotApi('Uq8VsNCmQ4k9JSdoscX32V7OGyGzD8Miso4KjjDV35QqdLd0WWrSHO8uItEoi76ZTJhz8M8DLVmS5bDEouYkWLRbAAR55p47VmFKzzsSk2TCBLbLlSQCbpvgl7q5gHJ4/IJkVsVitXyCNRFWoeIuuAdB04t89/1O/w1cDnyilFU=')
#----------  這裡放 Greeting code ---------------
for order in range(14):
    vsm= VideoSendMessage(
        original_content_url= "https://henrytrueheart.github.io/CTY12/prize_video/" + str(order) + ".mp4",
        preview_image_url= "https://henrytrueheart.github.io/CTY12/prize_video/" + str(order) + ".jpg"
    )

#----------  這裡放 Greeting code ---------------
    line_bot_api.push_message('U259ac17deb5aeedae29a145939ab7174',vsm)
# Sandra 的ID: 'U259ac17deb5aeedae29a145939ab7174'
# Henry 的 ID: 'U652e8808b20f146a4dbfc2cf07b8dc42'


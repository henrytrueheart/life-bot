
# encoding: utf-8

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,StickerSendMessage,VideoSendMessage
)

import random



app = Flask(__name__)

# 填入你的 message api 資訊
line_bot_api = LineBotApi('Uq8VsNCmQ4k9JSdoscX32V7OGyGzD8Miso4KjjDV35QqdLd0WWrSHO8uItEoi76ZTJhz8M8DLVmS5bDEouYkWLRbAAR55p47VmFKzzsSk2TCBLbLlSQCbpvgl7q5gHJ4/IJkVsVitXyCNRFWoeIuuAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0ffa3269103ae7fc9aa558321fc810c4')



# 設定你接收訊息的網址，如 https://YOURAPP.herokuapp.com/callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    content= event.message.text
    order= random.randint(0,13)
    if "吃囉" == content:
        video_url= "https://henrytrueheart.github.io/CTY12/prize_video/" + str(order) + ".mp4"
        preview_url= "https://henrytrueheart.github.io/CTY12/prize_video/" + str(order) + ".jpg"
        
        content="很乖很乖，給你點獎勵！"
        msg=TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token,[msg,VideoSendMessage(original_content_url=video_url, preview_image_url=preview_url)])
    if "還沒" == content:
        line_bot_api.reply_message(event.reply_token,[
                                    TextSendMessage(text= "快點吃！"),
                                    StickerSendMessage(
                                        package_id='11537', sticker_id='52002767'
                                    )
                                ]
        )
    if "測試" == content:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.user_id))
        
import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])

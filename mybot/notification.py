from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate,MessageAction
line_bot_api = LineBotApi('Uq8VsNCmQ4k9JSdoscX32V7OGyGzD8Miso4KjjDV35QqdLd0WWrSHO8uItEoi76ZTJhz8M8DLVmS5bDEouYkWLRbAAR55p47VmFKzzsSk2TCBLbLlSQCbpvgl7q5gHJ4/IJkVsVitXyCNRFWoeIuuAdB04t89/1O/w1cDnyilFU=')
#push message to one user

# ----------這邊放Redis 碼------------
import redis 

redisHost = config['redis']['redis-16381.c14.us-east-1-3.ec2.cloud.redislabs.com'] 
redisPort = config['redis']['16381'] 
redisPwd = config['redis']['t2V9X3ilzlHVUAWnBN2rO8YgrqKm6NOk'] 

useRedis = redis.Redis ( 
  host = redisHost, 
  port = redisPort, 
  password = redisPwd 
) 
useRedis.set("key", "hello, world") 
print(useRedis.get("key")) 





# ----------這裡放選單------------
tsm= TemplateSendMessage(
    alt_text="confirm temlate",
    template=ConfirmTemplate(
        text="吃藥時間到囉！有乖乖準時吃藥嘛？",
        actions=[
            MessageAction(
                label='吃囉', text='吃囉'
            ),
            MessageAction(
                label='還沒', text='還沒'
            )
        ]
    )
)
#    # ----------這裡放選單------------
line_bot_api.push_message('U652e8808b20f146a4dbfc2cf07b8dc42',tsm)
# Sandra 的ID: 'U259ac17deb5aeedae29a145939ab7174'
# Henry 的 ID: 'U652e8808b20f146a4dbfc2cf07b8dc42'



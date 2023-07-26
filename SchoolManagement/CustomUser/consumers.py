import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("INTO CONNECT")
        self.room_group_name = 'LENDI'
        await self.accept()
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        print(self.room_group_name, self.channel_name)
        self.send(text_data=json.dumps({'status': 'Connected Established Successfully'}))
        
    async def disconnect(self , close_code):
        print("2222222222222222222222222222222222222222222222222222")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print("33333333333333333333333333333333333333333333333333")
        text_data_json = json.loads(text_data)
        print("text_data_json",text_data_json)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type" : "sendMessage" ,
                "message" : message ,
                "username" : username ,
            }
        )

    async def sendMessage(self , event):
        print("444444444444444444444444444444444444444444444444444444")
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message": message, "username": username}))

import json
import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from chat.models import Message

class ChatRoomConsumer(AsyncWebsocketConsumer):

   async def connect(self):
      self.room_group_name = "YILab_player_chat"

      user = self.scope["user"]

      await self.channel_layer.group_add(self.room_group_name, self.channel_name)

      if user.is_authenticated:
         await self.accept()
      else:
         print("Not Authenticated!")
         await self.close()


   async def disconnect(self, code):
      await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


   async def receive(self, text_data):
      try:
         data = json.loads(text_data)
         message_text = data.get('message')
         user = self.scope["user"]

         if user.is_anonymous:
            await self.send(text_data=json.dumps({"error": "User not Authenticated!"}))
            return
         
         message = await self.create_message(user, message_text)

         await self.channel_layer.group_send(
            self.room_group_name,
            {
               "type": "chat_message",
               "message": message_text,
               "sender": user.name,
               "timestamp": str(message.timestamp),
            }
         )

      except json.JSONDecodeError:
         await self.send(text_data=json.dumps({"error": "Invalid JSON"}))


   async def chat_message(self, event):
      await self.send(text_data=json.dumps({
         "message": event["message"],
         "sender": event["sender"],
         "timestamp": event["timestamp"],
      }))

   @database_sync_to_async
   def create_message(self, user, message):
      return Message.objects.create(sender=user, content=message)
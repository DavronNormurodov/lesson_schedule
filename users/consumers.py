import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import action, ObserverModelInstanceMixin
from channels.db import database_sync_to_async

from users.models.user import User
from django.utils.timezone import now


class ConnectConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    group_room_name = None

    async def connect(self):
        self.user = self.scope['user']

        await database_sync_to_async(User.objects.filter(id=self.user.id).update)(
            is_online=True
        )
        await self.accept()
        await self.send_rooms(True)
        await self.down_the_count(self.user.id)
        # await self.join_to_rooms()

        if self.user.is_authenticated:
            await self.channel_layer.group_add(f"user__{self.user.id}", self.channel_name)
        else:
            await self.close()

    async def disconnect(self, code):
        time = now()
        await database_sync_to_async(User.objects.filter(id=self.user.id).update)(
            is_online=False,
            last_activity=time
        )
        await self.channel_layer.group_discard(f"user__{self.user.id}", self.channel_name)
        return await super().disconnect(code)


class ChatConsumer(AsyncWebsocketConsumer):
    groups = ["general"]

    async def connect(self):
        await self.accept()
        if self.scope["user"] is not AnonymousUser:
            self.user_id = self.scope["user"].id
            await self.channel_layer.group_add(f"{self.user_id}-message", self.channel_name)

    async def send_info_to_user_group(self, event):
        message = event["text"]
        await self.send(text_data=json.dumps(message))

    async def send_last_message(self, event):
        last_msg = await self.get_last_message(self.user_id)
        last_msg["status"] = event["text"]
        await self.send(text_data=json.dumps(last_msg))

    @database_sync_to_async
    def get_last_message(self, user_id):
        message = User.objects.filter(id=user_id).last()
        return message.first_name

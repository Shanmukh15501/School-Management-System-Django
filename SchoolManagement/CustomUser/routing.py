from django.urls import path , include
from CustomUser.consumers import ChatConsumer

# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
	path("test/" , ChatConsumer.as_asgi()) ,
]


print("websocket_urlpatterns",websocket_urlpatterns)
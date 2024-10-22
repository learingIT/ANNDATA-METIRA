from django.urls import path
from .views import home, chatbot, chat_api

urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('chat_api/', chat_api, name='chat_api'),  # Ensure this is correct
]

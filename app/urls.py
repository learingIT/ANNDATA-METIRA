from django.urls import path
from .views import (
    home, 
    chatbot, 
    chat_api,
    register,
    login_view,
    dashboard,
    get_suggestions,
    update_product,
    delete_product
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('chat_api/', chat_api, name='chat_api'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('get_suggestions/', get_suggestions, name='get_suggestions'),
    path('product/update/<int:product_id>/', update_product, name='update_product'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

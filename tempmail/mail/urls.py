# mail/urls.py

'''from django.urls import path
from .views import home, message_detail

urlpatterns = [
    path('',home, name='home'),
    path('message/<str:domain>/<str:login>/<int:message_id>/', message_detail, name='message_detail'),
]
'''
# mail/urls.py
from django.urls import path
from .views import home, message_detail

urlpatterns = [
    path('', home, name='home'),
    path('message/<str:domain>/<str:login>/<int:message_id>/', message_detail, name='message_detail'),
]

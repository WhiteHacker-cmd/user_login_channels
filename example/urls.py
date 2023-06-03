from django.urls import path
from example.views import user_list, log_in, log_out, sign_up, create_room, user_list1, chat_view


urlpatterns = [
    path('chat/<str:pk>/', chat_view, name='chat'),
    path('user1/', user_list1, name='user1'),
    path("room/", create_room, name='room'),
    path('', user_list, name='user_list'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('sign_up/', sign_up, name='sign_up'),
    path('user1/log_out/', log_out, name='log_out')
]

app_name = 'example'
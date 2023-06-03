from channels import Group
import json
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import Room, Message
from channels.sessions import channel_session

@channel_session_user_from_http
@channel_session
def ws_connect(message):
    
    prefix, label = message['path'].strip('/').split('/')
    print(prefix)
    print(label)
    print(message['path'])
    if prefix == 'chat':
        
        room = Room.objects.get(label=label)
        messages = Message.objects.filter(room=room)
        Group('chat' + label).add(message.reply_channel)
        message.reply_channel.send({"accept": True})
        # Group('chat').send({
        #     'text': json.dumps({
        #         "messages": "helloworld"
        #     })
        # })
        message.channel_session['chat'] = room.label
    else:
        Group('users').add(message.reply_channel)
        Group('users').send({
            'text': json.dumps({
                'username': message.user.username,
                'is_logged_in': True
            })
        })



@channel_session_user
def ws_disconnect(message):
    label = message.channel_session['chat']
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)
    Group('chat'+ label).discard(message.reply_channel)
    print("disconnecting...!")




@channel_session_user
@channel_session
def ws_recieve(message):
    label = message.channel_session['chat']
    print(message['text'])
    print(message.user.username)
    Group('chat' + label).send({
        'text': json.dumps({
            'username': message.user.username,
            "messages": message['text'],
            
        })
    })
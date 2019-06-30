#! coding:utf-8

from django.shortcuts import render
from massage.models import UserMessage

# Create your views here.
def getstart(request):
    # all_message = UserMessage.objects.filter(name='xiaobai', address= 'guangzhou')
    # for message in all_message:
    #     print(message.name)

    # user_message = UserMessage()
    # user_message.name = 'niubi'
    # user_message.message = 'test'
    # user_message.address = 'guangzhou'
    # user_message.objects_id = '2'
    # user_message.save()

    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     message = request.POST.get('message', '')
    #     user_message = UserMessage()
    #
    #     user_message.name = name
    #     user_message.email = email
    #     user_message.address = address
    #     user_message.message = message
    #     user_message.object_id = '123'
    #     user_message.save()

    # all_message = UserMessage.objects.filter(name='niubi', message='test')
    # all_message.delete()
    #
    # for message in all_message:
    #     message.delete()

    # message回填到前端
    message = None
    all_message = UserMessage.objects.filter(name='fanlei')
    print(all_message[0])
    if all_message:
        message = all_message[0]
    return render(request,'start.html', {'my_message':message})
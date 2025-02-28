from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from djchat.models import room, message,signup,Feedback
from django.http import HttpResponse,JsonResponse
from django.contrib import auth





# Create your views here.
def house(request):
    

    return render(request, 'house.html')





def signup(request):
   if  request.method=='POST':
        username=request.POST.get('username')
        
        password=request.POST.get('password')
        if not username or not password:
            messages.error(request, "Username and password are required")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.info(request,'username taken')
            return redirect('signup')
        
        
        user=User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('/')
        

   return render(request, 'signup.html')
  
  

def rom(request, room_name):
    username=request.GET.get('username')
    room_details=room.objects.get(name=room_name)
    return render(request, 'rom.html', {'username': username,'room_details': room_details,'room_name': room_name})

def checkview(request):
    roomname=request.POST['room_name']
    username=request.POST['username']
    passwords=request.POST['password']

    user =auth.authenticate(username=username,password=passwords)

    if user is not None:
            auth.login(request,user)
            if room.objects.filter(name=roomname).exists():
                return redirect('/'+roomname+'/?username='+username)
            else:
               new_room=room.objects.create(name=roomname)
               new_room.save()
               return redirect('/'+roomname+'/?username='+username) # This line redirects the user to the home page
    else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    
    

def send(request):
    username=request.POST['username']
    roomname=request.POST['roomname']
    messages=request.POST['message']
    new_message=message.objects.create(value=messages,user=username,room=roomname)
    new_message.save()
    return HttpResponse('message sent successfully')

def get_messages(request, room_name):
    room_details=room.objects.get(name=room_name)
    messages = message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')   
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')    
            return redirect('signin')
    else:
      return render(request, 'signin.html')
    



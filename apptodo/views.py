from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .utils import send_email
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Task
# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        Confirmpassword=request.POST.get('confirmpassword')
        Email=request.POST.get('email')

        if CustomUser.objects.filter(username=Username).exists():
            error_msg="username alredy exist.. "
            return render(request,'register.html',{'error_msg':error_msg})
        if CustomUser.objects.filter(email=Email).exists():
            errormsg="username alredy exist.. "
            return render(request,'register.html',{'errormsg':errormsg})
        if Confirmpassword == Password :
            user=CustomUser.objects.create_user(username=Username,password=Password ,email=Email)
            send_email(user.email)
            return redirect('Userlogin')

    return render(request,'register.html')
def Userlogin(request):
    if request.method=="POST":
        Username=request.POST.get('username')
        Password=request.POST.get('password')

        user=authenticate(request,username=Username,password=Password)
        if user is not None:
            message="sucessfully logined"
            login(request,user)
            return render(request,'home.html',{'message':message})
        else:
            errormessage="username password missmathch or not registerd"
            return render(request,'Userlogin.html',{'errormessage':errormessage})
    return render(request,'Userlogin.html')
@login_required
def addtask(request):
    if request.method =="POST":
        Title=request.POST.get('title')
        Description=request.POST.get('description')
        current_user=request.user                       # how
        data=Task(
            title=Title,
            description=Description,
            user=current_user
        )
        data.save()
    return render(request,'addtask.html')

def UserLogout(request):
    logout(request)
    return redirect('Userlogin')

@login_required
def viewtask(request):
    task=Task.objects.filter(user=request.user)
    
    return render(request,'viewtask.html',{'tasks':task})
@login_required
def edittask(request,task_id ):
    if request.method=="POST":
        Title=request.POST.get('title')
        Description=request.POST.get('description')
        current_user=request.user

        task=Task(
            id=task_id,
            title=Title,
            description=Description,
            user=current_user
        )
        task.save()
        return redirect('viewtask')
        
    return render(request,'edittask.html',{'task_id':task_id})
@login_required
def deletetask(request,task_id):
    tasks=get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        tasks.delete()
        return redirect('viewtask')
    else:
        return render(request,'viewtask.html',{'task':tasks})
    
        

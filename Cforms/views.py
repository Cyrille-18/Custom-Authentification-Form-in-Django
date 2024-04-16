from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import MyAuthentificationForm, SignUpForm

# Create your views here.
def login_page(request):
    return render(request,'Cforms/Login.html')

def index(request):
    return render(request, 'Cforms/index.html')

def log(request):
    if request.method == 'POST':
        form = MyAuthentificationForm(request,request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = MyAuthentificationForm()
    return render(request,'Cforms/Login.html',{'form':form})

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            newpassword = form.cleaned_data['newpassword']
            confirmpassword = form.cleaned_data['confirmpassword']

            if newpassword != confirmpassword:
                messages.error(request,"les mots de passes ne sont pas identiques")
                            
            user = User.objects.create_user(username=name, email=email, password=newpassword)

            messages.success(request, "compte crée avec succès.vous pouvez vous connecter")

            return redirect('log')
    else:
        form = SignUpForm()
    return render(request, 'Cforms/Login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('log')
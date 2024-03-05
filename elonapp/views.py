from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# Create your views here.


# Robert did manual #

def signin(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        
        user = authenticate(request=request, email = email, pwd = pwd)
        
        if user is not None:
            login(request, user)
            return redirect("homepage/")
        else:
            # return HttpResponse("email and password is matching")
            messages.error(request=request, message="email or password is incorrect.")
            

    
    return render(request=request, template_name="signin.html")
    
    

def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        conpwd = request.POST.get('confirmpassword')
        
        if pwd != conpwd:
            # return HttpResponse("username or password is incorrect.")
            messages.error(request=request, message="password and con_password is not matching.")
                
        else:
            my_user = User.objects.create_user(username, email, pwd)
            my_user.save()

            return redirect("signin")    
        
        # print("username:",username)
        # print("email:",email)
        # print("pas:",pwd)
        # print("conpwd:",conpwd)
        
        
    return render(request=request, template_name="signup.html")



def forgotpassword(request):
    
    return render(request=request, template_name="forgotpassword.html")



def coverpage(request):
    
    return render(request=request, template_name="coverpage.html")


# @login_required
def homepage(request):
    
    return render(request=request, template_name="homepage.html")


def logout(request):
    logout(request)
    return redirect('login')


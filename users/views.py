#from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.

#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):

    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f' Your account has been created! Now you can login!')
        #messages.success(request, f'Account created for {username}!')
        #return redirect('itreporting-home')
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})

def profile(request):
    return render(request, 'users/profile.html')

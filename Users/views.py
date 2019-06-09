from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterationForm,UserUpdationForm,ProfileUpdationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):

    if request.method=='POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'user successfully created')
            return redirect('login')
        else:
            messages.warning(request, f'invalid entries')

    else:
        form = UserRegisterationForm()
    return render(request,'Users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        UUForm=UserUpdationForm(request.POST,instance=request.user)
        PUForm=ProfileUpdationForm(request.POST,instance=request.user.profile)
        if UUForm.is_valid() and PUForm.is_valid():
            UUForm.save()
            PUForm.save()
            messages.success(request, f'profile successfully updated ')
            return redirect('profile')
    else:
        UUForm = UserUpdationForm(instance=request.user)
        PUForm = ProfileUpdationForm(instance=request.user.profile)
    return render(request,'Users/profile.html',{'UUForm':UUForm,'PUForm':PUForm})
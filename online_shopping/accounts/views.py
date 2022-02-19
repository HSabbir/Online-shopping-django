from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    print(form.data)
    if form.is_valid():
        user_obj = form.save()
        return redirect('login')

    context = {"form":form}
    return render(request, 'account/register.html', context)

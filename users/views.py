from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from users.forms import CustomUserCreationForm
from django.contrib import messages


@login_required
@user_passes_test(lambda user: user.is_authenticated)
def dashboard(request):
    user = request.user
    return render(request, template_name='users/dashboard.html', context={
        'username': user.username,
        'is_staff': user.is_staff,
        'is_admin': user.is_admin
        })


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        messages.success(request, 'Registration successful.')
        return render(request, template_name='users/dashboard.html', )
    return render(request=request, template_name="users/register.html", context={'form':form})
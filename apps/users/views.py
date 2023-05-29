from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

from .forms import (RegistrationForm, LoginForm)


class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'apps/auth/register.html'
    success_url = 'login'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'register_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1
                    )
                    user.save()
                    return redirect(self.success_url)
            else:
                messages.error(request, 'Passwords are not equal!')
                return redirect('register')
        return render(request, "apps/auth/login.html", {'register_form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    redirect_url = '/'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(self.redirect_url)
        else:
            print('Username or password not found')
            return redirect('login')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('index')

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.views.generic.edit import FormView
from .forms import UserForm
from .models import User


class HomeView(View):
    def get(self, request):
        user_list = User.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(user_list, 10)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'apps/crud/index.html', {'users': users})


class AddPersonView(FormView):
    template_name = 'apps/crud/add.html'
    form_class = UserForm

    def form_valid(self, form):
        form.save()
        return redirect('/')


class UpdatePersonView(View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        context = {'user': user}
        return render(request, 'apps/crud/edit.html', context)

    def post(self, request, pk):
        user = User.objects.get(id=pk)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/')


class DeletePersonView(View):
    def get(self, request, pk):
        user = User.objects.filter(id=pk)
        user.delete()
        return redirect('/')

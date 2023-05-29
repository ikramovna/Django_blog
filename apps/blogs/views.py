from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from apps.blogs.forms import CommentForm, ContactForm
from apps.blogs.models import Post, Contact
from apps.blogs.tasks import send_email_customer


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'apps/blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 3


class PostDetailView(View):
    template_name = 'apps/blog/post_detail.html'

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        comment_form = CommentForm()

        return render(request, self.template_name, {'post': post,
                                                    'comments': comments,
                                                    'comment_form': comment_form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        comment_form = CommentForm(data=request.POST)
        new_comment = None

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

        return render(request, self.template_name, {'post': post,
                                                    'comments': comments,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form})


class SendEmailView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'apps/blog/contact.html'

    def form_valid(self, form):
        form.save()
        print(form.instance.email)
        send_email_customer.delay(form.instance.email, form.instance.message)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



import slug as slug
from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
# Create your views here.
from .forms import CommentForm
from .models import Post, Comment, Contact
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404

#def HomeView(request):
    #return render(request, 'shop.html')

def HomeView(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'index2.html', context)

def CateView(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'index.html', context)

def ShoesView(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'shoes.html', context)



def AboutView(request):
    product = Post.objects.all()
    context = {
        'pr':product
    }
    return render(request, 'about.html', context)

#def ShirtsView(request):
   # product = Post.objects.all()
  ##  context = {
      #  'pr':product
   # }
  #  return render(request, 'post.html', context)




class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post.html'



class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')



def ContactView(request):
        if request.POST:
            new_contact = Contact.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                message=request.POST['message']
            )

        return render(request, "contact.html", {})

def entry_not_found(request, exception, template_name='404.html'):
    return render(request, template_name)
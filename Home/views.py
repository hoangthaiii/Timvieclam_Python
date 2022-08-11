from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import auth, User, Group

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Catalogy, User, Post_cv
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect,Http404
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user,password=password)

        if(user is not None):
            auth.login(request, user)
            return redirect('/')
    else:
        category= Catalogy.objects.all()
        return render(request, 'pages/login.html',{'category':category})


def register(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password']
        user = User.objects.create_user(username=username1, email=email1, password=password1)
        path_group = Group.objects.get(name='nguoidung')
        path_group.user_set.add(user)
        user.save();
        messages.success(request, "Dang ki thanh cong!!")
        return redirect('register')
    else:
        return render(request, 'pages/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register_tuyendung(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password']
        name_company = request.POST['nameCompany']
        user = User.objects.create_user(username=username1, email=email1, password=password1, first_name=name_company)
        path_group = Group.objects.get(name='nhatuyendung')
        path_group.user_set.add(user)
        user.save();
        messages.success(request, "Dang ki thanh cong");
        return redirect('re_tuyendung')
    else:
        return render(request, 'pages/register_tuyendung.html')

class ListJob(ListView):
    model = Post
    template_name = 'pages/Home.html'
    def get_context_data(self,*args,**kwargs):
        context = super(ListJob,self).get_context_data(*args,**kwargs)
        theloai = Catalogy.objects.all()
        context['theloai'] = theloai
        return context
    #template_name = 'pages/base.html'

class Job_details(DetailView):
    model = Post
    template_name = 'pages/post_details.html' 
    def get_context_data(self,*args,**kwargs):
        context = super(Job_details,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_care = stuff.total_care()
        theloai = Catalogy.objects.all()
        context['theloai'] = theloai
        context['total_care'] = total_care
        return context
    
class AddJobView(CreateView):
    model = Post
    form_class = FormPost
    template_name = 'pages/add_post.html'
    success_url = '/'
    #fields = '__all__'
    #fields = ('nameJob','catalogy' ,'nhatuyen','date','salary', 'diachi','motacv','phucloi','yeucaucv')

class managePost(ListView):
    model = Post
    template_name = 'pages/managePost.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'pages/update_post.html'
    #fields = '__all__'

class DeletePost(DeleteView):
    model = Post
    template_name = 'pages/delete_post.html'
    success_url = reverse_lazy('home')

def categoryView(request, pk):
    category_posts = Post.objects.filter(catalogy=pk)
    return render(request,'pages/categories.html', {'pk':pk, 'category_posts':category_posts})

def JobView(request, nameCompany):
    jobs_company = Post.objects.filter(nhatuyen_id=nameCompany)
    return render(request,'pages/jobs.html', {'nameCompany':nameCompany, 'jobs_company':jobs_company})

class Up_LoadCV(CreateView):
    model = Post_cv
    form_class = CV_Form
    template_name = 'pages/upcv.html'
    success_url = '/'

class CV_Manage(ListView):
    model = Post_cv
    template_name = 'pages/manage_CV.html'
    def get_context_data(self,*args,**kwargs):
        context = super(CV_Manage,self).get_context_data(*args,**kwargs)
        theloai = Catalogy.objects.all()
        post = Post.objects.all()
        context['theloai'] = theloai
        context['post'] = post
        return context

def CV_POST(request, pk):
    cv_post = Post_cv.objects.filter(post_id=pk)
    return render(request,'pages/post_cv.html', {'pk':pk ,'cv_post':cv_post})

def Search_post(request):
    if request.method == "POST":
        search = request.POST['search']
        post = Post.objects.filter(nameJob__contains=search)
        catalogy = Catalogy.objects.all()
        return render(request, 'pages/search_post.html',{'post':post, 'search':search, 'catalogy':catalogy})
    else:
        return render(request, 'pages/search_post.html')
def CareView(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        post.care.add(request.user)
        return HttpResponseRedirect(reverse('post_details',args=[str(pk)]))


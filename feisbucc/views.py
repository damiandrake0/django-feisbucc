from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from .forms import SignupForm, LoginForm, PostForm,EditProfile
from .models import Profile,Post

# Create your views here.
def feisbucc(request):
    listFriend = Profile.objects.all()
    listPost = Post.objects.all()
    

    context = {
        'listFriend':listFriend,
        'listPost':listPost}
    
    return render(request, 'feisbucc/home.html',context)

def user_login(request):
    if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)    
                    return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    
    return render(request, 'register/register.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def like(request,id_post):
    # profilo = Profile.objects.get(user=request.user)
    post = Post.objects.get(pk=id_post)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')

# def following(request,id_profile):
    
#     profile = Profile.objects.get(pk=id_profile)
#     if request.user in profile.follows.all():
#         profile.follows.remove(request.user)
#     else:
#         profile.follows.add(request.user)
    
#     return redirect('home')

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('home')
    else:
        form = PostForm
    return render(request, 'add_post/add_post.html',{'form':form})

def profileV(request,profile_id):
    if int(profile_id) == 9999999999:
        profiloL = Profile.objects.get(user=request.user)
        listPost = Post.objects.filter(author=profiloL.user)
    else:
        profiloL = Profile.objects.get(pk=profile_id)
        listPost = Post.objects.filter(author=profiloL.user)
    
    if request.method == "POST":
        current_user_profile = request.user.profile
        action = request.POST.get("follow")

        if action == "follow":
            current_user_profile.follows.add(profiloL)
        elif action == "unfollow":
            current_user_profile.follows.remove(profiloL)
        current_user_profile.save()

    n = listPost.count()

    if request.user == profiloL.user:
        logg = True
    else:
        logg = False

    context = {
        'profiloL':profiloL,
        'listPost':listPost,
        'numeroPost':n,
        'logg':logg
        }
    
    return render(request, 'prof/profilo.html',context)

def edit_profile(request,profile_id):
    profilo = Profile.objects.get(pk=profile_id)
    form = EditProfile(request.POST or None,request.FILES,instance=profilo)
    if form.is_valid():
        form.save()
        redirect('home')
    return render(request, 'edit_profile/edit_profile.html',{'form':form,'profile':profilo})

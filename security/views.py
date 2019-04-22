from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
import operator
from .models import Entry
from .forms import EntryForm




def home(request):
    return render(request,'security/home.html',{})

def log_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have been logged in!'))
            return redirect('home')

        else:
            messages.success(request,('ERROR logging in please try again'))
            return redirect('login')

    else:
        return render(request,'security/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged OUT!...'))
    return redirect('home')


def reg_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('You have registered...'))
            return redirect('home')
            
    else:
        form=SignUpForm()
    context={'form':form}  
    return render(request,'security/register.html',context)

def count(request):
    return render(request,'security/count.html')

def count1(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'security/count1.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})


def secondhome(request):
    return render(request,'security/secondhome.html')


def index(request):
    entries = Entry.objects.order_by('-date_posted')

    context = {'security' : entries}

    return render(request, 'security/index.html', context)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')       
    else:
        form = EntryForm()

    context = {'form' : form}

    return render(request, 'security/add.html', context)


def submit(request):
    return render(request,'security/index.html')

def about(request):
    return render(request, 'security/about.html')

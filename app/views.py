from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client, Question, Book
from .forms import QuestionForm
from .forms import DonationForm

# Create your views here.

def Home(request):
    asked_question = Question.objects.all()
    context = {'asked_question':asked_question}
    return render(request, 'app/home.html', context)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Client.objects.filter(username=username).exists():
                messages.error(request, 'Username exist')
                return redirect('register')
            elif Client.objects.filter(email=email).exists():
                messages.error(request, 'Email exist')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()

                client_details = Client.objects.create(first_name=first_name, last_name=last_name, username=username, email=email)
                client_details.save()

                messages.info(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password not same')
            return redirect('register')
    else:    
        return render(request, 'app/register.html')   
    return render(request, 'app/register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password,)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid details')
            return redirect('login')
    else:
        return render(request, 'app/login.html')
    return render(request, 'app/login.html')

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'app/logout.html')

def Location(request):
    return render(request, "app/location.html")

@login_required(login_url = 'register')
def Ask_question(request, pk):
    owner = User.objects.get(id=pk)
    form = QuestionForm(initial={'owner':owner})
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, initial={'owner':owner})
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = QuestionForm()
    context = {'form':form}
    return render(request, 'app/ask_question.html', context)    

@login_required(login_url = 'register')
def bookVisit(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        mobile_no = request.POST['phone']
        number = request.POST['number']
        location = request.POST['location']

        visitor = Book.objects.create(full_name=full_name, mobile_no=mobile_no, number=number, location=location)
        visitor.save()
        messages.info(request, 'Thanks for booking a visit at our childrens home, we will schedule the date of visit and contact you.')
        return redirect('thanks')
    else:
        return render(request, 'app/book_visit.html')
    return render(request, 'app/book_visit.html')

def Thanks(request):
    return render(request, 'app/thanks.html')

def Contact(request):
    return render(request, 'app/contact.html')

@login_required(login_url = 'register')
def Donate(request):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_visit')
        else:
            form = DonationForm()
    context = {'form':form}
    return render(request, 'app/donate.html', context)

def Accountdetails(request, pk):
    client = Client.objects.get(id=pk)
    client = User.objects.get(id=pk)
    context = {'client':client}
    return render(request, 'app/account.html', context)
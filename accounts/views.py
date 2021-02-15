from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):
    if request.method == "POST":
        # Get Form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if password doesn't match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Sorry, Username Already Used')
                return redirect('register')
            else:
                # check email already exist
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Sorry, Email Already Used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now Logged in')
                    user.save()
                    messages.success(request, 'you are now register and can log in')
                    return redirect('login')
        else:
            messages.error(request, "sorry, password doesn't match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        # Get Form values
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are Now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('display_page')

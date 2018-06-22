from django.shortcuts import render,reverse
from django.views.generic import UpdateView, ListView
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# from .models import home
from .forms import RegistrationForm



def index(request):
	# model = home()
	# form = LoginForm()
	return render(request, 'index.html')
	# if form.is_valid():
	# 	message.success(request, 'Login Successful')



#register method
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST) #from our registration form class in form.py, we get the request method

        if form.is_valid():
            form.save()

            email = request.POST.get('email')
            password = request.POST.get('password1')


            user = authenticate(
                request,
                email = email,
                password = password
            )
            login(request, user)
            return redirect(reverse('home:index'))
    else:
        form = RegistrationForm()
    context = {'form':form} 
    return render(request, 'home/reg_form.html',context)


# change password method
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Your new password has been saved")
            update_session_auth_hash(request,form.user)
            return redirect(reverse('home:index'))

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request,'home/change_password.html', context) 




# def user_login(request):
# 	if request.method == 'POST':
# 		print(request.POST)
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			cd = form.cleaned_data
# 			user = authenticate(username=cd['username'],password=cd['password'])
# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
					
# 					return HttpResponseRedirect(reverse('home'))
# 					# return HttpResponse('Login successfully')				
# 				else:
# 					return HttpResponse('Invalid login')
# 			else:
# 				form = LoginForm()
# 			return render(request, 'account/login.html', {'form': form})
# 	form = LoginForm()
# 	return render(request, 'account/login.html', {'form': form})



# def log_out(request):
# 	logout(request)
# 	return HttpResponseRedirect(reverse('login'))
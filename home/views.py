from django.shortcuts import render
from django.views.generic import UpdateView, ListView
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import home
from .forms import LoginForm



def index(request):
	model = home()
	form = LoginForm()
	return render(request, 'index.html', {'form':form})
	if form.is_valid():
		message.success(request, 'Login Successful')




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
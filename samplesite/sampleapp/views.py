from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

''' 
home view: an example of function based views. 
also demonstrates how to render templates from view function.
it displays how to get and set session variables 
'''
def home(request):
	
	# try to get a value from session, get 0 if none exists/none set
	visit_count = request.session.get("visit_count", 0)
	visit_count += 1  # increase the visit count
	request.session['visit_count'] = visit_count # set the visit count to session
	
	# render the home.html template, pass the visit_count variable to it
	return render(request, "home.html", {"visit_count": visit_count})


""" 
Demonstrate use of login_required decorator. 
If user is not logged in, it'll redirect to login page.
After logging in there, user will be brought here back 
"""
@login_required	
def profile(request):
	return render(request, "profile.html")


''' 
This is a demonstration on how to use function based views. This is not used right now.
The class based views of this function is being used. It performs same functions as RegisterView
'''
def register(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST) # this is a built in form class provided by django
		if form.is_valid():
			form.save() # also inserts data to database
			return redirect('/register/done') # redirect to the /register/done
	
	else:
		form = UserCreationForm() # An unbound form
		
	return render(request, "register.html",{"form": form}) # render the register.html with the provided form


''' 
This is a demonstration on how to use class based views. 
This does exactly same task as register(request) function
'''
class RegisterView(View):
	form_class = UserCreationForm # reference to the form class
	template_name = 'register.html'
	
	def get(self, request): # this function will be called when a GET request is received
		form = self.form_class() # initialize the form class, Unbound now
		return render(request, self.template_name, {'form': form}) # passing the form class to template

	def post(self, request, *args, **kwargs): # this will be called when POST request is received
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save() # insert data to database
			return redirect('/register/done')

		return render(request, self.template_name, {'form': form}) # redisplay the form in case of errors
		

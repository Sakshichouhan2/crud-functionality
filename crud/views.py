from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrations
from .models import User

# Create your views here.

#this function will add new item and show all item
def add_show(request):
	if request.method == 'POST':
		fm = StudentRegistrations(request.POST)
		if fm.is_valid():
			nm = fm.cleaned_data['name']
			em = fm.cleaned_data['email']
			pw = fm.cleaned_data['password']
			reg = User(name=nm, email=em, password=pw)
			reg.save()
			fm = StudentRegistrations()
	else:
		fm = StudentRegistrations()
	stud = User.objects.all()
	return render(request, 'crud/addandshow.html', {'form':fm ,'stu':stud})

#this function will update
def update_data(request, id):
	if request.method == 'POST':
		pi = User.objects.get(pk=id)
		fm = StudentRegistrations(request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		pi = User.objects.get(pk=id)
		fm = StudentRegistrations(instance=pi)
	return render(request, 'crud/update.html', {'form':fm})
#this function will delete
def delete_data(request, id):
	if request.method == 'POST':
		pi = User.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')

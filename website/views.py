from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
import calendar

@login_required
def home(request):
	# Get current month and year, or from request parameters
	year = int(request.GET.get('year', datetime.now().year))
	month = int(request.GET.get('month', datetime.now().month))

	# Create calendar
	cal = calendar.monthcalendar(year, month)
	month_name = calendar.month_name[month]

	# Calculate previous and next month
	prev_month = month - 1 if month > 1 else 12
	prev_year = year if month > 1 else year - 1
	next_month = month + 1 if month < 12 else 1
	next_year = year if month < 12 else year + 1

	context = {
		'calendar': cal,
		'month': month,
		'month_name': month_name,
		'year': year,
		'prev_month': prev_month,
		'prev_year': prev_year,
		'next_month': next_month,
		'next_year': next_year,
		'today': datetime.now().day if month == datetime.now().month and year == datetime.now().year else None,
	}
	return render(request, 'home.html', context)

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Invalid username or password.')
	return render(request, 'login.html')

def logout_view(request):
	logout(request)
	return redirect('home')

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

@login_required
def day_detail(request, year, month, day):
	from .models import Task
	from datetime import date

	selected_date = date(year, month, day)
	tasks = Task.objects.filter(user=request.user, date=selected_date)

	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description', '')
		if title:
			Task.objects.create(
				user=request.user,
				date=selected_date,
				title=title,
				description=description
			)
			messages.success(request, 'Task added successfully!')
			return redirect('day_detail', year=year, month=month, day=day)

	context = {
		'date': selected_date,
		'tasks': tasks,
		'year': year,
		'month': month,
		'day': day,
	}
	return render(request, 'day_detail.html', context)

@login_required
def toggle_task(request, task_id):
	from .models import Task
	if request.method == 'POST':
		task = Task.objects.get(id=task_id, user=request.user)
		task.completed = not task.completed
		task.save()
		messages.success(request, 'Task updated!')
		return redirect('day_detail', year=task.date.year, month=task.date.month, day=task.date.day)
	return redirect('home')

@login_required
def delete_task(request, task_id):
	from .models import Task
	if request.method == 'POST':
		task = Task.objects.get(id=task_id, user=request.user)
		task_date = task.date
		task.delete()
		messages.success(request, 'Task deleted!')
		return redirect('day_detail', year=task_date.year, month=task_date.month, day=task_date.day)
	return redirect('home')
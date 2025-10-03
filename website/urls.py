from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('register/', views.register_view, name='register'),
	path('day/<int:year>/<int:month>/<int:day>/', views.day_detail, name='day_detail'),
	path('task/toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
	path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]

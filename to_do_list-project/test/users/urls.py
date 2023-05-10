from django.urls import path
from users import views

urlpatterns = [
    path('',views.manepage,name='task_list'),
    path('register', views.register, name='register'),
    path('login/', views.log, name='login'),
    path('exit/', views.sign_out, name='exit'),
    path('delete/<str:username>/<int:id>/', views.delete,name='delete'),
    path('edit/<str:username>/<int:id>/', views.edit,name='edit'),
]

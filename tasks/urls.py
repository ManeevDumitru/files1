from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('destroy/<int:question_id>', views.destroy, name='destroy'),
    path('create', views.create, name='create'),
]
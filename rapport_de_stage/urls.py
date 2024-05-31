from django.urls import path
from .views import index
from.import views

urlpatterns = [
    
    path('',index),
    path('rapports/create/', views.rapport_create, name='rapport_create'),
    path('rapports/', views.rapport_list, name='rapport_list'),
    #path('', template.views.login_page, name='login'),

]

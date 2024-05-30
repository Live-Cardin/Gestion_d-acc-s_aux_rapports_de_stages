from django.urls import path
from .views import index
from.import views

urlpatterns = [
    
     path('',index),
    path('rapports/',views.rapport_list,name='rapport_list'),
    #path('', template.views.login_page, name='login'),

]

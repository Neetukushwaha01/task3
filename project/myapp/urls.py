from django.urls import path
from . import views
urlpatterns = [

    path('clients/',views.ClientList.as_view()),
    path('clients/<pk>',views.ClientDetails.as_view()),

# ClientDetails.get(pk)


    path('projects/',views.ProjectList.as_view()),

]
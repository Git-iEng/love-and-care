from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('view/', views.public_view, name='public_view'),
    path('navbar.html', views.navbar, name='navbar'),
    path('footer.html', views.footer, name='footer'), 

    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('project/', views.project, name='project'),
    path('team/', views.team, name='team'),
   path('contact/', views.contact_us, name='contact_us'),
]

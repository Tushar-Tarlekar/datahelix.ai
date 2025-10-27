
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import (
    AboutView,
   
    ContactView,
    
    HomeView,
      ResearchView,
    ResearchAreaView,
    ServicesView,
    
    TermsAndConditionsView,
     error_404,
    error_500,
    pki,
   
    
)
handler404 = 'index.views.error_404'
handler500 = 'index.views.error_500'

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
    path(
        'terms-and-conditions/',
        TermsAndConditionsView.as_view(), name='terms'),
          path('services/', ServicesView.as_view(), name='services'),
              path('contact-us/', ContactView.as_view(), name='contact'),
                 path('about/', AboutView.as_view(), name='about'),
        path('research-areas/', ResearchAreaView.as_view(), name='research-areas'),
    path('research/', ResearchView.as_view(), name='research'),
   
     path('.well-known/pki-validation/4C9A034B553DA5F76D9EF5851892591B.txt', pki, name="pki-validation"),
    path('', HomeView.as_view(), name='home'),
   




  
]
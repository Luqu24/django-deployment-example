from django.urls import path
from relative_urls import views

app_name = 'relative_urls'

urlpatterns = [
    path('', views.home,name='home'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative')
]

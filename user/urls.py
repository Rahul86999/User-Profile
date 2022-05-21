from django.urls import  path
from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views
from .import views 

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('profile', views.UserProfileView.as_view(), name='profile'),
    path('delete/',views.DeleteProfile.as_view(), name='delete_profile'),
    path('update/',views.UpdateDoctor.as_view(), name='update_get_profile'),
    path('user-validate',views.user_validate, name='user_validate'),
]

from django.contrib.auth.urls import urlpatterns
from rest_framework.urls import app_name,path
from .views import SignUpView,ProfileViewSet,SignInView
from rest_framework.routers import DefaultRouter


app_name = 'User'
router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
urlpatterns=[
    path('signin/',SignInView.as_view(),name='sign_in'),
    path('signup/',SignUpView.as_view(),name='sign_up'),

]
urlpatterns += router.urls
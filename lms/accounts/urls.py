from django.urls import path

from accounts.views import ProfileView, SignUpView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', view.SignUpView.as_view(), name='signup'),
]

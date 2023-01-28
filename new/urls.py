from django.urls import path
from .views import *

urlpatterns = [
    path('', AboutView.as_view(), name="main"),
    path('thanks', SubmitedView.as_view(), name="submited"),
]

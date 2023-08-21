from django.urls import path
from users.views import (
    AuthView,
    VerificationView,
)

app_name = 'accounts'
urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('verify/', VerificationView.as_view(), name='verification'),
]
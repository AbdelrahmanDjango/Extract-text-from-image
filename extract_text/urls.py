from django.urls import path
from .views import extract_text
app_name = 'extract_text'

urlpatterns = [
    path('extract_text/', extract_text, name='extract_text'),
    # Add other paths as needed
]
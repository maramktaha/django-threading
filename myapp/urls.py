
from django.urls import path
from .views import TestImport
urlpatterns = [
    
    path('import/',TestImport.as_view()),
    
    
]

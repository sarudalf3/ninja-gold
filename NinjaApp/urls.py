from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process_money/<str:source>', views.process),  # r'^process_money/(?P<source>\w+)$'
    path('reset', views.reset),
]

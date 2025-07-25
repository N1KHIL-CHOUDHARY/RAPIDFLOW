from django.urls import path
from .views import HelloView,AgentView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('agent/', AgentView.as_view(), name='agent'),

]

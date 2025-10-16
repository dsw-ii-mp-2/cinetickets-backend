from django.urls import path
from .views import TicketListCreateView, TicketDetail

urlpatterns = [
    path("", TicketListCreateView.as_view(), name="ticket-list-create"),
    path("<int:pk>/", TicketDetail.as_view(), name="ticket-detail"),
]

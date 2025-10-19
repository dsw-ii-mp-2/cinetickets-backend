from rest_framework import generics, pagination
from .models import Ticket
from .serializers import TicketSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 10

    def get_queryset(self):
        queryset = Ticket.objects.all().order_by("-created_at")
        user = self.request.query_params.get("bought_by")
        if user:
            queryset = Ticket.objects.filter(posted_by__id=user).order_by("-created_at")
        return queryset

    def perform_create(self, serializer):
        serializer.save(bought_by=self.request.user)


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
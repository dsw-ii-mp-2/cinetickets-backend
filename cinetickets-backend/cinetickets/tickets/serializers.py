from rest_framework import serializers
from .models import Ticket
from users.models import User


class TicketUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
        read_only_fields = fields


class TicketSerializer(serializers.ModelSerializer):
    bought_by = TicketUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            "id",
            "movie",
            "function",
            "seat",
            "bought_by",
            "created_at",
        ]
        read_only_fields = ["id", "bought_by", "created_at"]

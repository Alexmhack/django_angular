from rest_framework import generics

from .serializers import LeadSerializer
from accounts.models import Lead

class AccountListAPIView(generics.ListCreateAPIView):
	serializer_class = LeadSerializer
	queryset = Lead.objects.all()

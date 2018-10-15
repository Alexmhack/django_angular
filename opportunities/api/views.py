from rest_framework import generics

from .serializers import AccountSerializer
from accounts.models import Opportunity

class AccountListAPIView(generics.ListCreateAPIView):
	serializer_class = OpportunitySerializer
	queryset = Opportunity.objects.all()

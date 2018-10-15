from rest_framework import generics

from .serializers import ContactSerializer
from accounts.models import Contact

class AccountListAPIView(generics.ListCreateAPIView):
	serializer_class = ContactSerializer
	queryset = Contact.objects.all()

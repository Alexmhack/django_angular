from rest_framework import serializers

from contacts.models import Contact

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = "__all__"

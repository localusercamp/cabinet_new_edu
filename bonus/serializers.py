from rest_framework import serializers
from .models import *


class AccountPaymentServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountPaymentService
        fields = ["supplier_name", "service_name"]

class AccountPaymentSerializer(serializers.ModelSerializer):
    account_payment_services = AccountPaymentServiceSerializer(source='accountpaymentservice_set', many=True)

    class Meta:
        model = AccountPayment
        fields = ["account_payment_services", 'account_number']

class BonusTransactionSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField()
    account_payment = AccountPaymentSerializer()

    class Meta:
        model = BonusTransaction
        fields = ["id", "user", "value", "note", "date_created", 'account_payment']
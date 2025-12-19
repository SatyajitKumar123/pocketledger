from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer
    
    @action(detail=False, methods=['delete'])
    def clear_all(self, request):
        Transaction.objects.all().delete()
        return Response({'message': 'History cleared successfully'})
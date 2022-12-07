from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.views import DataView
# Create your views here.
import requests

url = "https://app.bluevine.com/api/v3/partners/file-upload/?external_register_token=PLATFORMFUNDING-7fc07fad174b43af8df49921b8d66214&pid_login=0182857"

payload = {'category': 'bank_statement',
           'user_slug': 'de07c9ff474741c08fe9bbc66b0a4f84',
           'original_filename': 'bank_statement.pdf',
           'upload_for': 'user_registration'}
files = [
    ('file', ('Partner Web Service documentation v15 08112021docx (2).pdf',
     open('API//sample.pdf', 'rb'), 'application/pdf'))
]
headers = {
    'Authorization': 'Bearer 00D740000008fzN!AQ8AQHS7fDz.qmufo3XflnMxuBlnKiM3yLKttVo.5SnnWm8O3OBtFL5ACGo3CMiU90Fm6HHpUCNwQYHYfjIkW1cZWom4oG2d',
    'Cookie': 'visid_incap_1229188=8IRMcS7nQpydPS3z5tz1+K0cx2IAAAAAQUIPAAAAAADaWEH7q9vA/dx2lwrcytyn'
}

class HelloAuthView(generics.GenericAPIView):
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)
        return Response(data={response}, status=status.HTTP_200_OK)

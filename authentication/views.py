from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
# Create your views here.
import requests

url = "https://app.bluevine.com/api/v3/partners/file-upload/?external_register_token=PLATFORMFUNDINGTEST-2a1e0af3691a4667a2b6658db3dfce62&pid_login=0182857"

payload = {'category': 'bank_statement',
           'user_slug': '42d352d75d41473580bc89a1f64d9da1',
           'original_filename': 'bank_statement.pdf',
           'upload_for': 'user_registration'}
files = [
    ('file', ('Partner Web Service documentation v15 08112021docx (2).pdf', open(
        'API/uploads/sample.pdf', 'rb'), 'application/pdf'))
]
headers = {
    'Authorization': 'Bearer 00D740000008fzN!AQ8AQHS7fDz.qmufo3XflnMxuBlnKiM3yLKttVo.5SnnWm8O3OBtFL5ACGo3CMiU90Fm6HHpUCNwQYHYfjIkW1cZWom4oG2d',
    'Cookie': 'visid_incap_1229188=8IRMcS7nQpydPS3z5tz1+K0cx2IAAAAAQUIPAAAAAADaWEH7q9vA/dx2lwrcytyn'
}

class HelloAuthView(generics.GenericAPIView):
    def get(self,request):
        response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)
        return Response(data={response}, status=status.HTTP_200_OK)

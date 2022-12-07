
from venv import create
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Dataserializer
from rest_framework import status
from .models import Data
from rest_framework.parsers import MultiPartParser
import requests
from django.core.files.storage import FileSystemStorage

url = "https://app.bluevine.com/api/v3/partners/file-upload/?external_register_token=PLATFORMFUNDINGTEST-2a1e0af3691a4667a2b6658db3dfce62&pid_login=0182857"


headers = {
    'Authorization': 'Bearer 00D740000008fzN!AQ8AQHS7fDz.qmufo3XflnMxuBlnKiM3yLKttVo.5SnnWm8O3OBtFL5ACGo3CMiU90Fm6HHpUCNwQYHYfjIkW1cZWom4oG2d',
    'Cookie': 'visid_incap_1229188=8IRMcS7nQpydPS3z5tz1+K0cx2IAAAAAQUIPAAAAAADaWEH7q9vA/dx2lwrcytyn'
}



class DataView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        serializer = Dataserializer(data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            file_uploaded = request.FILES['file_uploaded']
            fs = FileSystemStorage()
            # filename = fs.save("Sample.pdf", file_uploaded)
            uploaded_file_url = fs.url(file_uploaded)

            files = [
                ('file', ('Partner Web Service documentation v15 08112021docx (2).pdf',
                        open('API/sample.pdf', 'rb'), 'application/all'))
            ]
            slug = serializer.data.get('user_slug')
            payload = {'category': 'bank_statement',
                       'user_slug': slug,
                       'original_filename': 'bank_statement.pdf',
                       'upload_for': 'user_registration'}
            response = requests.request(
            "POST", url, headers=headers, data=payload, files=files)
            return Response(data={response}, status=status.HTTP_200_OK)
            #return Response({"status": "success", "header": slug}, status=status.HTTP_200_OK)
        else:
            print(serializer.data.get('user_slug'))
            return Response({"status": "xxx", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
   
        
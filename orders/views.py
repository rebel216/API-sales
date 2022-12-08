
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Dataserializer
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from .form import UploadFileForm
from django.conf import settings
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from .form import UploadFileForm

url = "https://app.bluevine.com/api/v3/partners/file-upload/?external_register_token=PLATFORMFUNDINGTEST-2a1e0af3691a4667a2b6658db3dfce62&pid_login=0182857"


headers = {
    'Authorization': 'Bearer 00D740000008fzN!AQ8AQHS7fDz.qmufo3XflnMxuBlnKiM3yLKttVo.5SnnWm8O3OBtFL5ACGo3CMiU90Fm6HHpUCNwQYHYfjIkW1cZWom4oG2d',
    'Cookie': 'visid_incap_1229188=8IRMcS7nQpydPS3z5tz1+K0cx2IAAAAAQUIPAAAAAADaWEH7q9vA/dx2lwrcytyn'
}


class DataView(APIView):
    parser_classes = [FileUploadParser,TemplateHTMLRenderer,]
    template_name ='home.html'
    def post(self,request):
        print(request.FILES)        
        serializer = Dataserializer(data=request.data)
        print(request.FILES)       
        if serializer.is_valid():
            serializer.save()
            if request.method == 'POST':
                form = UploadFileForm(request.POST, request.FILES)
                # request.headers['Content_Length'] = len(request.headers)
                print(len(request.headers))
                user_slug = request.headers.get('slug')
                file_up = request.FILES.get('file')
                
                print(user_slug)
                fs = FileSystemStorage()
                filename = fs.save("sample.pdf", file_up)
                uploaded_file_url = fs.url(filename)

                files = [
                    ('file', ('Partner Web Service documentation v15 08112021docx (2).pdf',
                              open(settings.MEDIA_ROOT+uploaded_file_url, 'rb'), 'application/pdf'))
                ]
                print(uploaded_file_url)
                payload = {'category': 'bank_statement',
                           'user_slug': 'de07c9ff474741c08fe9bbc66b0a4f84',
                           'original_filename': 'bank_statement.pdf',
                           'upload_for': 'user_registration'}
                response = requests.request(
                "POST", url, headers=headers, data=payload,files=files)
                return Response(data={response}, status=status.HTTP_200_OK)
                #return render(request,'home.html') 
            
        else:
            print(serializer.errors)
            return Response({"status": "xxx", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# def handle_uploaded_file(f):
#     with open('/API/'+"xxx.pdf", 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

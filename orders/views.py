
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Dataserializer
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .form import UploadFileForm

url = "https://app.bluevine.com/api/v3/partners/file-upload/?external_register_token=PLATFORMFUNDINGTEST-2a1e0af3691a4667a2b6658db3dfce62&pid_login=0182857"


headers = {
    'Authorization': 'Bearer 00D740000008fzN!AQ8AQHS7fDz.qmufo3XflnMxuBlnKiM3yLKttVo.5SnnWm8O3OBtFL5ACGo3CMiU90Fm6HHpUCNwQYHYfjIkW1cZWom4oG2d',
    'Cookie': 'visid_incap_1229188=8IRMcS7nQpydPS3z5tz1+K0cx2IAAAAAQUIPAAAAAADaWEH7q9vA/dx2lwrcytyn'
}


class DataView(APIView):
    parser_classes = [FileUploadParser,]
    
    def post(self,request):
        
        form = UploadFileForm(request.POST, request.FILES)
        serializer = Dataserializer(data=request.data)
               
        if serializer.is_valid():
            serializer.save()
            myfile = request.FILES['myfile']
           
           
            
            
            # # handle_uploaded_file(request.FILES['file_uploaded'])
            # form = UploadFileForm(request.POST , request.FILES)
            # handle_uploaded_file(request.FILES['file'].read())
            
            # print(doc.size) 
            User_slug = serializer.data.get('slug')
            print(request.FILES)
            # file_up = request.FILES.get("file_uploaded")
            
            # print("read file")
            fs = FileSystemStorage()
            filename = fs.save("Sample.pdf", myfile)
            uploaded_file_url = fs.url(filename)

            # files = [
            #     ('file', ('Partner Web Service documentation v15 08112021docx (2).pdf',
            #               open(settings.MEDIA_ROOT+uploaded_file_url, 'rb'), 'application/pdf'))
            # ]
            
            payload = {'category': 'bank_statement',
                       'user_slug': User_slug,
                       'original_filename': 'bank_statement.pdf',
                       'upload_for': 'user_registration'}
            # response = requests.request(
            # "POST", url, headers=headers, data=payload,file=files)
            # return Response(data={response}, status=status.HTTP_200_OK)
            return Response({"status": "success", "header": "slug"}, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response({"status": "xxx", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
def handle_uploaded_file(f):
    with open('/API/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

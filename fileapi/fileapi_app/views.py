from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PyPDF2 import PdfReader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter

api_key = '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'
embeddings = OpenAIEmbeddings(openai_api_key=api_key)



# @api_view(['POST'])
# def process_file(request):
#     file = request.FILES.get('file')

#     if file:
#         content = file.read().decode('utf-8')
#         return Response({'result': content})
#     else:
#         return Response({'error': 'No file provided.'})
    
@api_view(['POST'])
def process_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        
        if file.name.endswith('.pdf'):
           pdf_file = PdfReader(file)
           extracted_text = ""
           for page_num in range(len(pdf_file.pages)):
                page = pdf_file.pages[page_num]
                text = page.extract_text()
                
                extracted_text += text
           contents = extracted_text
            
        elif file.name.endswith('.txt'):
            contents = file.read().decode('utf-8')
            
        elif file.name.endswith('.docx'):
            contents = "word format not supported"
            
        else:
            contents = "format not supported"


 # text_splitter = CharacterTextSplitter(separator = " ", chunk_size=200, chunk_overlap=0)
        splitter = CharacterTextSplitter(separator=" ", chunk_size=7, chunk_overlap=3)
        documents = splitter.create_documents([contents])
        embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        # docsearch = Chroma.from_documents(documents, embeddings)




        return Response({'result': contents})
    else:
        return Response({'error': 'error'})



@api_view(['POST'])
def chat(request):
    if request.method == 'POST':
        return Response({'answer': "responsegen"})
        input_string = request.data.get('input_string', '')
        

        return Response({'answer': "responsegen"})
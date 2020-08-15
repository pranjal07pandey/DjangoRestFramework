from django.shortcuts import render
from .models import Snippet
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import SnippetSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.

# @api_view(['GET','POST'])
# def snippet_list(request):
#     '''
#         list all the code snippets or create a new one

#     '''

#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':

#         serializer = SnippetSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def snippet_details(request, pk):

    
#     '''
#     Retrive, update or delete a code snippet

#     '''

#     try:
#         snippet = Snippet.objects.get(id = pk)

#     except Snippet.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(instance = snippet, data = request.data)

#         if serializer.is_valid:
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status = HTTP_204_NO_CONTENT) 

    


    
# using viewsets
from rest_framework import viewsets,permissions

class SnippetViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    pemission_classes = [permissions.IsAuthenticatedOrReadOnly]






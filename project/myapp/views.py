from django.shortcuts import render

# Create your views here.

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegiserClientSerializer,ClientSerializer,ProjectSerializer,CreateProjectSerializer
from .models import Client,Project


from django.http import Http404

class ClientList(APIView):
    def get(self,request,pk=None):
        all_clients =Client.objects.all()
        clients_list =ClientSerializer(all_clients,many=True)
        return Response( clients_list.data, status=status.HTTP_200_OK )

    def post(self,request=None):
        result={}
        if not request.data.get('client_name'):
            result['error']="client_name required."
            return Response( result, status=status.HTTP_201_CREATED )
        if not request.data.get('created_by'):
            result['error']="created_by required."
            return Response( result, status=status.HTTP_400_BAD_REQUEST )

        serializer =RegiserClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            client_name =request.data.get( 'client_name' )
            message =f"{client_name} Register Successfully"
            return Response( message, status=status.HTTP_200_OK )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )



#all  details put and delect funstion code start>
class ClientDetails(APIView):
    def get_object(self,pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        client =self.get_object(pk)
        client_list =ClientSerializer(client)
        return Response(client_list.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        print(request)
        client = self.get_object( pk )
        print(request.data)
        serilizer =RegiserClientSerializer(client, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response( serilizer.data, status=status.HTTP_202_ACCEPTED )
        else:
            return Response( serilizer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self,request,pk):
        client = self.get_object( pk )
        client.delete()
        return Response({'message':"Client Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
# all  details put and delect funstion code close>

# <project show and add list start code>
class ProjectList( APIView ):
    def get(self, request, pk=None):
        all_project = Project.objects.all()
        project_list = ProjectSerializer( all_project, many=True )
        return Response( project_list.data, status=status.HTTP_200_OK )

    def post(self, request=None):
        result = {}
        if not request.data.get( 'project_name' ):
            result['error'] = "project_name required."
            return Response( result, status=status.HTTP_201_CREATED )

        if not request.data.get( 'created_by' ):
            result['error'] = "created_by required."
            return Response( result, status=status.HTTP_400_BAD_REQUEST )

        serializer = CreateProjectSerializer( data=request.data )
        if serializer.is_valid():
            serializer.save()
            project_name = request.data.get( 'project_name' )
            message = f"{project_name} Register Successfully"
            return Response( message, status=status.HTTP_200_OK )
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )


# <project show and add list cloes code>



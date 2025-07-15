from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class EstadoView(APIView):
    @swagger_auto_schema(
        operation_description="Verifica el estado de respuesta de la API.",
        responses={200: openapi.Response('Estado OK')}
    )
    def get(self, request):
        """
        Devuelve el estado actual de la API.
        """
        return Response({'estado': 'La API responde correctamente'}, status=status.HTTP_200_OK)

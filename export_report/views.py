from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def export_report(request):
    return Response(request.data, status.HTTP_200_OK)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import bzRomanizer

class RomanizerView(APIView):
    def get(self, request):
        try:
            name = bzRomanizer.romanize(request.query_params.get('name'))
            return Response(name)
        except Exception as e:
            return Response(str(e),  status=status.HTTP_400_BAD_REQUEST)
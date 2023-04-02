from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ProviderSerializer


class ProvidersView(APIView):
    def get(self, request):
        return Response({"message": "Get all!"})


class ProviderView(APIView):
    def get(self, request, key):
        return Response({"message": f"Get one {key}"})

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"message": "OK"})

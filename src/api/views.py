from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view()
@permission_classes([IsAuthenticated])
def index(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

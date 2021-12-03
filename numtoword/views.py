from .utils import requestHandler
from rest_framework import views


class NumbersToWord(views.APIView):

    def get(self, request):
        return requestHandler(request.GET)

    def post(self, request):
        return requestHandler(request.data)

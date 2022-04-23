from django.shortcuts import render
from django.http import JsonResponse
from .models import Quote, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuoteSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class Tsitata(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_news = Quote.objects.all()

        serialized_news = QuoteSerializer(data=all_news, many=True)
        serialized_news.is_valid()

        return Response(serialized_news.data)


    def post(self, request):

        print(dir(request), request.GET['keyin'])
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
                
            # user_obj = User.objects.get(id=int(request.data['author']))
            # print(user_obj.first_name, user_obj.last_name, user_obj.email, user_obj.password)

            serialized_news = QuoteSerializer(data=request.data)

            if serialized_news.is_valid():
                # serialized_news.save()
                return Response({"detail": "Yanglik muvaffaqiyatli qo'shildi"})

            return Response({"detail": serialized_news.errors})
        else:
            return Response({"detail": "Avtorizatsiya ma'lumotlarini kiriting"})
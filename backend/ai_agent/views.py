from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import AIAgentService


class HelloView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "Hello from Django!"})


class AgentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get("message", "")
        if not message:
            return Response({"error": "Message is required"}, status=400)
        
        # Use the AI service
        ai_service = AIAgentService()
        response = ai_service.process_message(message)
        
        return Response({"reply": response})

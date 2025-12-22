from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def handle_echo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response_msg = data.get('message', '')
            response_msg += ' frontend'
            return JsonResponse({'message': response_msg})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def handle_register(request):
    return HttpResponse("Hello, yan yan")
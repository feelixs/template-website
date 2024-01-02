from django.shortcuts import render

async def home(request):
    return render(request, 'index.html')
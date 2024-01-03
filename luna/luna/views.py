from django.shortcuts import render, redirect

async def home(request):
    return render(request, 'index.html')

async def home_redir(request):
    return redirect("/home")

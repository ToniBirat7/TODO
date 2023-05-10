from django.shortcuts import render, redirect
from main_app.models import TODO
# Create your views here.
def Home(request):
    data = TODO.objects.all()
    print(data)
    return render(request, 'main_app/home.html', {'data' : data})

def Delete(request,id):
    data = TODO.objects.get(id=id)
    print(request.method)
    print(data)
    data.delete()
    return redirect('home')

def Edit(request,id):
    data = TODO.objects.get(id=id)
    if request.method == 'GET':
        return render(request,'main_app/edit.html',{'data':data})
    else: 
         data.title = request.POST['title']
         data.description = request.POST['description']
         data.save()
         return redirect('home')

def Add(request):
    if request.method == 'GET':
        print(request.method)
        return render(request,'main_app/form.html')
    else:
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        is_completed = True if request.POST.get('is_completed') else False
        TODO.objects.create(title=title,description=description,is_completed=False, user_id=1)
    return redirect('home')
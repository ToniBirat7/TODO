from django.shortcuts import render, redirect
from main_app.models import TODO
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Home(request):
    search = request.GET.get('search')
    if search is None:
        data = TODO.objects.all()
    else: 
        data = TODO.objects.filter(title__icontains=search)
        request.session['search'] = search
    print(data)
    return render(request, 'main_app/home.html', {'data' : data})
@login_required
def Delete(request,id):
    try:
        data = TODO.objects.get(id=id)
        data.delete()
        return redirect('home')
    # print(request.method)
    # print(data)
    except TODO.DoesNotExist:
        return redirect('404notfound')
@login_required
def Edit(request,id):
    try:
        data = TODO.objects.get(id=id) 
    except TODO.DoesNotExist:
        return redirect('404notfound') 
    if request.method == 'GET':
        return render(request,'main_app/edit.html',{'data':data})
    else: 
         data.title = request.POST['title']
         data.description = request.POST['description']
         data.save()
         return redirect('home')
@login_required
def Add(request):
    if request.method == 'GET':
        print(request.method)
        return render(request,'main_app/form.html')
    else:
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        # is_completed = True if request.POST.get('is_completed') else False #This button is removed
        TODO.objects.create(title=title,description=description,is_completed=False, user_id=request.user.id) #is_comp is kept False by default
    return redirect('home')

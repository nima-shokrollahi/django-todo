from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Do
from .forms import AddDoForm, AddDoFormOrj


def home(request):
    return render(request, 'do/home.html')


@login_required(login_url='accounts:login')
def list_do(request):
    does = Do.objects.filter(owner=request.user)
    todo_list_len = len(does)
    context = {'data': does,'todo_list_len':todo_list_len}
    if request.method == "POST":
        checks_list = request.POST.getlist('checked')
        checks_list = [int(x) for x in checks_list]
        for item in does:
            if item.id in checks_list:
                item.checked = True
                item.save()
                # Do.objects.filter(id=item.id).update(checked=True)
            else:
                item.checked = False
                item.save()
                # Do.objects.filter(id=item.id).update(checked=False)
        return render(request, 'do/list_do.html', context)
    return render(request, 'do/list_do.html', context)


@login_required(login_url='accounts:login')
def detail_do(request, id):
    data = Do.objects.get(id=id)
    context = {'data': data}
    return render(request, 'do/detail_do.html', context)


@login_required(login_url='accounts:login')
def add_do(request):
    if request.method == "POST":
        form = AddDoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('list_do')
    form = AddDoForm()
    context = {'form': form}
    return render(request, 'do/add_do.html', context=context)


@login_required(login_url='accounts:login')
def dell_do(request, id):
    try:
        do = Do.objects.get(id=id, owner=request.user)
        do.delete()
        return redirect('list_do')
    except:
        return redirect('list_do')

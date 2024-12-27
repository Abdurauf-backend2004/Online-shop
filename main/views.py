from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
from main.forms import *
from main.models import *

def home_view(request):
    return render(request,'home.html')
def mahsulot_view(request):
    if request.method=='POST':
        form=MahsulotForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mahsulotlar')
    mahsulotlar=Mahsulot.objects.all()
    q_soz=request.GET.get('q_soz')
    if q_soz is not None:
        mahsulotlar=mahsulotlar.filter(mahsulot_nomi__contains=q_soz)
    context={
        'mahsulotlar':mahsulotlar,
        'q_soz':q_soz,
        'form':MahsulotForm()
    }
    return render(request,'mahsulot.html',context)
def mahsulot_index_view(request,mahsulot_id):
    mahsulotlar=Mahsulot.objects.get(id=mahsulot_id)
    context={
        'mahsulotlar':mahsulotlar
    }
    return render(request,'mahsulot_index.html',context)
def mijoz_view(request):
    if request.method=='POST':
        form=MijozForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mijozlar')
    mijozlar=Mijoz.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        mijozlar = mijozlar.filter(ism__contains=q_soz)
    context={
         'mijozlar':mijozlar,
         'q_soz':q_soz,
        'form':MijozForm()
    }
    return render(request,'mijoz.html',context)
def mijoz_index_view(request,mijoz_id):
    mijoz=Mijoz.objects.get(id=mijoz_id)
    context={
        'mijoz':mijoz
    }
    return render(request,'mijoz_index.html',context)

def buyurtma_view(request):
    if request.method=='POST':
        form=BuyurtmaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('buyurtmalar')
    buyurtmalar=Buyurtma.objects.all()
    q_soz = request.GET.get('q_soz')
    if q_soz is not None:
        buyurtmalar = buyurtmalar.filter(mijoz_id__ism__contains=q_soz)
    context={
        'buyurtmalar':buyurtmalar,
        'q_soz':q_soz,
        'form':BuyurtmaForm()
    }
    return render(request,'buyurtma.html',context)
def buyurtma_index_view(request,buyurtma_id):
    buyurtma=Buyurtma.objects.get(id=buyurtma_id)
    context={
        'buyurtma':buyurtma
    }
    return render(request,'buyurtma_index.html',context)

def mahsulot_delete(request,mahsulot_id):
    mahsulotlar=get_object_or_404(Mahsulot,id=mahsulot_id)
    mahsulotlar.delete()
    return redirect('mahsulotlar')
def mijoz_delete(request,mijoz_id):
    mijozlar=get_object_or_404(Mijoz,id=mijoz_id)
    mijozlar.delete()
    return redirect('mijozlar')
def buyurtma_delete(request,buyurtma_id):
    buyurtmalar=get_object_or_404(Buyurtma,id=buyurtma_id)
    buyurtmalar.delete()
    return redirect('buyurtmalar')
def mahsulot_update(request,mahsulot_id):
    mahsulot = get_object_or_404(Mahsulot, id=mahsulot_id)
    if request.method == 'POST':
        form = MahsulotForm(request.POST,instance=mahsulot)
        if form.is_valid():
            form.save()
            return redirect('mahsulotlar')
    else:
        form =MahsulotForm(instance=mahsulot)
    context={
        'form':form
    }
    return render(request,'mahsulot_update.html',context)


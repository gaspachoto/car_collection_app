from django.shortcuts import render, redirect

from car_collection.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection.web.models import Profile, Car


def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'core/index.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form
    }
    return render(request, 'profile/profile-create.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_price = 0
    for car in cars:
        total_price += car.price
    context = {
        'profile': profile,
        'total_price': total_price
    }
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-delete.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    cars_count = Car.objects.count()
    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'core/catalogue.html', context)


def create_car(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    profile = Profile.objects.first()
    context = {
        'car': car,
        'profile': profile,
    }
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'car': car,
        'profile': profile,
        'form': form,
    }
    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    context = {
        'car': car,
        'profile': profile,
        'form': form,
    }
    return render(request, 'car/car-delete.html', context)

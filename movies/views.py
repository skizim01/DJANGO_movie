from django.db.models import Q
from django.shortcuts import render, redirect
from django.apps import apps
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from .models import Country, OBT, Plane, Ship, Rocket, Weapon, Ammunition, Artillery, Request

for app_conf in apps.get_app_configs():
    try:
        lists = app_conf.get_model("request")
    except LookupError:
        pass

class RequestView(ListView):
    model = lists
    queryset = lists.objects.all()

class OBTView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=2).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'request'
        return render(request, f'movies/{varr}_datail.html', {'data': data, 'pk': 2, 'fullData': data})

class CountryView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=1).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'country'
        return render(request, f'movies/{varr}_datail.html', {'data': data, 'pk': 1, 'fullData': data})

class PlaneView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=3).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'plane'
        return render(request, f'movies/{varr}_datail.html', {'data': data, 'pk': 3, 'fullData': data})

class ShipView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=4).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'ship'
        return render(request, f'movies/{varr}_datail.html', {'data': data, 'pk': 4, 'fullData': data})

class RocketView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=5).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'rocet'
        return render(request, f'movies/{varr}_detail.html', {'data': data, 'pk': 5, 'fullData': data})

class WeaponView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=6).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'weapon'
        return render(request, f'movies/{varr}_detail.html', {'data': data, 'pk': 6, 'fullData': data})

class ArtView(View):
    def get(self, request):
        for app_conf in apps.get_app_configs():
            try:
                model = app_conf.get_model(lists.objects.get(id=8).model)
            except LookupError:
                pass
        data = model.objects.all()
        varr = 'art'
        return render(request, f'movies/{varr}_detail.html', {'data': data, 'pk': 8, 'fullData': data})


class Filtet(View):
    def get(self, request):
        data = Ship.objects.all().only("name", "displacement")
        fullData = Ship.objects.all().only("country", "name")

        return render(request, f'movies/filter.html', {'data': data, 'pk': 9, 'fullData': fullData})


def firlterCountry(request, pk):
        m_vvp = request.GET["1Element"].split(',')
        s_1000 = request.GET["2Element"].split(',')
        data = Country.objects.filter(Q(m_vvp__gte=float(f"{m_vvp[0]}.{m_vvp[1]}")) &
                                      Q(s_1000__gte=float(f"{s_1000[0]}.{s_1000[1]}")))
        varr = 'country'
        fullData = Country.objects.all()
        return render(request, f'movies/{varr}_datail.html', {'data': data, "pk": 1, 'fullData': fullData})

def firlterOBT(request, pk):
        print(request.GET)
        data = OBT.objects.filter(weapon=request.GET["1Element"],
                                  range=request.GET["2Element"])
        varr = 'request'
        fullData = OBT.objects.all()
        return render(request, f'movies/{varr}_datail.html', {'data': data, "pk": 2, 'fullData': fullData})

def firlterPlane(request, pk):
        print(request)
        el2 = Country.objects.get(name=request.GET['2Element'])
        el1 = request.GET["1Element"]
        data = Plane.objects.filter(appointment=el1,
                                      country=el2)
        varr = 'plane'
        fullData = Plane.objects.all()
        return render(request, f'movies/{varr}_datail.html', {'data': data, "pk": 1, 'fullData': fullData})

def firlterShip(request, pk):
        el2 = request.GET["2Element"]
        el1 = request.GET["1Element"]
        data = Ship.objects.filter(autonomy=el1,
                                      year=el2)
        varr = 'ship'
        fullData = Plane.objects.all()
        return render(request, f'movies/{varr}_datail.html', {'data': data, "pk": 4, 'fullData': fullData})

def firlterRocket(request, pk):
        el2 = request.GET["2Element"]
        el1 = request.GET["1Element"]
        data = Rocket.objects.filter(height=el1,
                                      year=el2)
        varr = 'rocet'
        fullData = Rocket.objects.all()
        return render(request, f'movies/{varr}_detail.html', {'data': data, "pk": 5, 'fullData': fullData})

def firlterWeapon(request, pk):
        el2 = request.GET["2Element"]
        el1 = request.GET["1Element"]
        data = Weapon.objects.filter(range=el1,
                                      spm=el2)
        varr = 'weapon'
        fullData = Weapon.objects.all()
        return render(request, f'movies/{varr}_detail.html', {'data': data, "pk": 6, 'fullData': fullData})

def firlterAmmunition(request, pk):
        el2 = request.GET["2Element"]
        el1 = request.GET["1Element"]
        data = Weapon.objects.filter(appointment=el1,
                                      range=el2)
        varr = 'amm'
        fullData = Weapon.objects.all()
        return render(request, f'movies/{varr}_detail.html', {'data': data, "pk": 7, 'fullData': fullData})

def firlterArt(request, pk):
    for i in Artillery.objects.get(id=request.GET["id"]).ammunition.all():
        print(i.name, request.GET["id"], )
        el1 = Artillery.objects.get(id=request.GET["id"]).ammunition.all()

        el2 = request.GET["2Element"]
        data = Artillery.objects.filter(ammunition__artillery__in=el1,
                                      range_move=el2)
        varr = 'art'
        fullData = Artillery.objects.all()
        return render(request, f'movies/{varr}_detail.html', {'data': fullData, "pk": 8, 'fullData': fullData})

def addOBT(request):
    print(request.POST)
    name = request.POST['element1']
    country = Country.objects.get(name=request.POST['element2'])
    weapon = request.POST['element4']
    apppo = request.POST['element5']
    range = request.POST['element6']
    OBT.objects.get_or_create(name=name, country=country, weapon=weapon, speed=apppo, range=range)
    return redirect("/2/")

def addPlane(request):
    print(request.POST)
    name = request.POST['element1']
    country = Country.objects.get(name=request.POST['element2'])
    weapon = request.POST['element3']
    appointment = request.POST["element4"]
    range = request.POST["element5"]
    Plane.objects.get_or_create(name=name, country=country,
                                  weapon=weapon, appointment=appointment,
                                  range=range)
    return redirect("/3/")

def addCountry(request):
    print(request.POST)
    name = request.POST['element1']
    soldat = int(request.POST['element2'])
    money = int(request.POST['element4'])
    m_vvp = request.POST["element5"].split(',')
    s_1000 = request.POST["element3"].split(',')
    Country.objects.get_or_create(name=name, soldat=soldat,
                                  money=money, m_vvp=float(f"{m_vvp[0]}.{m_vvp[1]}"),
                                  s_1000=float(f"{s_1000[0]}.{s_1000[1]}"))
    return redirect("/1/")

def addShip(request):

    print(request.POST)
    name = request.POST['element1']
    country = Country.objects.get(name=request.POST['element2'])
    appointment = request.POST['element3']
    autonomy = request.POST["element4"]
    displacement = request.POST["element5"]
    year = int(request.POST["element6"])
    Ship.objects.get_or_create(name=name, country=country,
                                  autonomy=autonomy, appointment=appointment,
                                  displacement=displacement, year=year)
    return redirect("/4/")

def addRocket(request):

    print(request.POST)
    name = request.POST['element1']
    country = Country.objects.get(name=request.POST['element2'])
    height = request.POST['element3']
    speed = request.POST["element6"]
    range = request.POST["element5"]
    year = int(request.POST["element4"])
    Rocket.objects.get_or_create(name=name, country=country,
                                  height=height, range=range,
                                  speed=speed, year=year)
    return redirect("/5/")

def addWeapon(request):
    print(request.POST)
    name = request.POST['element1']
    country = Country.objects.get(name=request.POST['element2'])
    caliber = request.POST['element3']
    range = request.POST["element4"]
    spm = request.POST["element5"]
    Weapon.objects.get_or_create(name=name, country=country,
                                  range=range, caliber=caliber,
                                  spm=spm)
    return redirect("/6/")

def delCountry(request):
    req = request.POST['1Element'].split('@')
    print(req, request.POST['1Element'])
    name = req[1]
    weapon = req[0]
    Country.objects.get(name=name, soldat=weapon).delete()
    return redirect("/1/")

def delOBT(request):
    req = request.POST['1Element'].split('@')
    print(req, request.POST['1Element'])
    name = req[1]
    weapon = req[0]
    OBT.objects.get(name=name, weapon=weapon).delete()
    return redirect("/2/")

def delPlane(request):
    req = request.POST['1Element'].split('@')
    print(req, request.POST['1Element'])
    appointment = req[1]
    name = req[0]
    Plane.objects.get(name=name, appointment=appointment).delete()
    return redirect("/3/")

def delShip(request):
    req = request.POST['1Element'].split('@')
    print(req, request.POST['1Element'])
    displacement = req[1]
    name = req[0]
    Ship.objects.get(name=name, displacement=displacement).delete()
    return redirect("/4/")

def delRocket(request):
    req = request.POST['1Element'].split('@')
    print(req, request.POST['1Element'])
    range = req[1]
    name = req[0]
    Rocket.objects.get(name=name, range=range).delete()
    return redirect("/5/")

def delWeapon(request):
    req = request.POST['1Element'].split('@')
    print(req, request.POST['1Element'])
    caliber = req[1]
    name = req[0]
    Weapon.objects.get(name=name, caliber=caliber).delete()
    return redirect("/6/")

def changeC(request):
    print(request.GET)
    return redirect(f"/admin/movies/country/{request.GET['1']}/change/")


def filter(request, pk):
    print(request.GET)
    el1 = Country.objects.get(name=request.GET["name"].split('@')[0],
                              soldat=int(request.GET["name"].split('@')[1])
                            )
    el2 = int(request.GET["2"])
    data = Ship.objects.filter(country=el1, year=el2).only("name", "displacement")
    print(data.query)
    fullData = Ship.objects.all().only("country", "year")
    return render(request, f'movies/filter.html', {'data': data, 'pk': 9, 'fullData': fullData})

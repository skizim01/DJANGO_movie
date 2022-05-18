from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestView .as_view()),
    path('1/change', views.changeC , name="change_c"),
    path("1/<int:pk>", views.firlterCountry, name='filter_Country'),
    path('1/', views.CountryView.as_view(), name='Country_info'),
    path("1/add/", views.addCountry, name='add_Country'),
    path("1/delete/", views.delCountry, name='delete_Country'),
    path("2/<int:pk>", views.firlterOBT, name='filter_OBT'),
    path('2/', views.OBTView.as_view(), name='OBT_info'),
    path("2/add/", views.addOBT, name='add_OBT'),
    path("2/delete/", views.delOBT, name='delete_OBT'),
    path("3/<int:pk>", views.firlterPlane, name='filter_plane'),
    path('3/', views.PlaneView.as_view(), name='plane_info'),
    path("3/add/", views.addPlane, name='add_plane'),
    path("3/delete/", views.delPlane, name='delete_plane'),
    path("4/<int:pk>", views.firlterShip, name='filter_ship'),
    path('4/', views.ShipView.as_view(), name='ship_info'),
    path("4/add/", views.addShip, name='add_ship'),
    path("4/delete/", views.delShip, name='delete_ship'),
    path("5/<int:pk>", views.firlterRocket, name='filter_rocket'),
    path('5/', views.RocketView.as_view(), name='rocket_info'),
    path("5/add/", views.addRocket, name='add_rocket'),
    path("5/delete/", views.delRocket, name='delete_rocket'),
    path("6/<int:pk>", views.firlterWeapon, name='filter_weapon'),
    path('6/', views.WeaponView.as_view(), name='weapon_info'),
    path("6/add/", views.addWeapon, name='add_weapon'),
    path("6/delete/", views.delWeapon, name='delete_weapon'),
    path('8/', views.ArtView.as_view(), name='weapon_info'),
    # path("8/add/", views.addArt, name='add_weapon'),
    # path("8/delete/", views.delArt, name='delete_weapon'),
    path("8/<int:pk>", views.firlterArt, name='filter_art'),
    path("9/", views.Filtet.as_view(), name='filter'),

    path("9/<int:pk>", views.filter, name='filter'),

]
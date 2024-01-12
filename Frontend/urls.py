from django.urls import path
from Frontend import views

urlpatterns = [path('',views.homePage,name="homePage"),
               path('ItemPage/',views.ItemPage,name="ItemPage"),
               path('itemFiltered/<iname>/',views.itemFiltered,name="itemFiltered"),
               path('single_iem/',views.single_iem,name="single_iem"),
               path('reservation/',views.reservation,name="reservation"),
               path('loginPage/',views.loginPage,name="loginPage"),
               path('saveSignup/',views.saveSignup,name="saveSignup"),
               path('UserLogin/',views.UserLogin,name="UserLogin"),
               path('Userlogout/',views.Userlogout,name="Userlogout"),
               path('saveReservation/',views.saveReservation,name="saveReservation"),
               path('aboutPage/',views.aboutPage,name="aboutPage"),
               path('contactPage/',views.contactPage,name="contactPage"),
               path('saveContact/',views.saveContact,name="saveContact"),
               path('gallery/',views.gallery,name="gallery"),
               ]
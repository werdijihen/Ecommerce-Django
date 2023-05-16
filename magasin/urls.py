from django.urls import path
from django.contrib import admin
from django.urls import path,include
from .import views
from .views import liste_commandes
from .views import liste_categories
from .views import liste_Commission
from .views import send_feedback_view
from .views import view_feedback_view
from .views import product_detail
from magasin.views import search

from magasin.views import CategoryAPIView
from magasin.views import ProduitAPIView

from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
 
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')



urlpatterns = [
    path('products/', views.index, name='index'),
    path('', views.indexA, name='indexA'),
   
    path('Fournisseur/', views.nouveauFournisseur, name='Fournisseur'),
    path('fournisseurs/', views.indexF, name='fournisseurs'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('send_feedback_view/', views.send_feedback_view, name='send_feedback_view'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),
    path('commandes/', views.liste_commandes, name='commandes'),
    path('categories/', views.liste_categories, name='categories'),
     path('Commission/', views.liste_Commission, name='liste_Commission'),

     path('magasin/search/', views.search, name='search'),
     path('magasin/<int:pk>/', views.product_detail, name='product_detail'),

path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('', include(router.urls)),
                
              
  path('api/category/', CategoryAPIView.as_view()),
 path('api/produits/', ProduitAPIView.as_view()),


path('contact/',views.contact,name='contact'),

    path('supprimer_produit/<int:id>/',views. supprimer_produit, name='supprimer_produit'),  
    path('modifier_produit/<int:id>/',views. modifier_produit, name='modifier_produit'),
     path('supprimer_fournisseur/<int:id>/',views. supprimer_fournisseur, name='supprimer_fournisseur'),  
    path('modifier_fournisseur/<int:id>/',views. modifier_fournisseur, name='modifier_fournisseur'),

    path('ListCommande/', views.ListCommande, name='ListCommande'),
    path('create_commande/',views.create_commande,name='create_commande'),
     path('editCommande/<int:pk>/', views.edit_commande, name='edit_commande'),
    path('deleteCommande/<int:pk>/', views.delete_commande, name='delete_commande'),
    path('Commande/<int:commande_id>/', views.detail_commande, name='detail_commande'),

   path('ListCategorie/', views.ListCategorie, name='ListCategorie'),
    path('create_categorie/',views.create_categorie,name='create_categorie'),
    path('editCategorie/<int:pk>/', views.edit_categorie, name='edit_categorie'),
    path('deleteCategorie/<int:pk>/', views.delete_categorie, name='delete_categorie'),
    path('Categorie/<int:categorie_id>/', views.detail_categorie, name='detail_categorie'),
    
     path('liste/', views.liste_produits, name='liste_produits'),
     path('ajouter/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('contenu/', views.contenu_panier, name='contenu_panier'),
    path('passer_commande/', views.passer_commande, name='passer_commande'),
    path('vider_panier/', views.vider_panier, name='vider_panier'),
    path('panier_detail/', views.panier_detail, name='panier_detail'),
    path('paniers/', views.liste_paniers, name='liste_paniers'),
    path('panier/<int:pk>/', views.edit_panier, name='edit_panier'),
    path('register/',views.register, name = 'register'),
    path('home/',views.home, name = 'home'),
   path('', include(router.urls)),
    path('message/', views.message, name='message'),
    path('TtMessage/', views.TtMessage, name='TtMessage'),
    path('deleteMessage/<int:pk>/', views.delete_message, name='delete_message'),
    path('Message/<int:msg_id>/', views.detail_message, name='detail_message'),
                
 
   
]

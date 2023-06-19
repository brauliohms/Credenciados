from credenciados import views
from django.contrib import admin
from django.urls import include, path
from usuarios.views import edit_usuario, sair

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/profile/", edit_usuario, name="edit_usuario"),
    path("accounts/sair/", sair, name="sair"),
    path("", views.index, name="index"),
    path("credenciado/add/", views.add_credenciado, name="add_credenciado"),
    path("credenciado/<int:pk>/", views.edit_credenciado, name="edit_credenciado"),
    path("credenciado/<int:pk>/excluir/", views.del_credenciado, name="del_credenciado"),
    path("credenciado/<int:pk>/informacoes/", views.pdf_credenciado, name="pdf_credenciado"),
    path("credenciado/buscar_por_nomes", views.buscar_nomes, name="buscar_nomes"),
    path("credenciado/buscar_por_servicos", views.buscar_servicos, name="buscar_servicos"),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]

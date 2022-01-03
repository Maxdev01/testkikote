from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="firststep"),
    # sa pou le li jwenn kategori an an
    path('lis-konpayi-ki-gen-anndanl/<catego>/' ,views.index , name="allcatego"),
    path('detay/<int:id>/' , views.detailArchive, name='detay'),

    # pou detail ki andan potfolio an
    path('les-details-du-portefolio/<int:id>/', views.detailPotfo , name='detpotfos'),

    path('kikote-all-users', views.listUser , name="viewsuser"),
    path("kikote-user-profil/<int:id>/", views.profilDetail, name="profiluser"),
    path('chwazibaytravay', views.jobList, name="job"),
    path("bay-yon-moun-travay", views.jobUser, name="jobuser"),
    path('antreprize-kap-bay-travay', views.antreprizJob, name="jobuser-2"),
    path('modidifye-itilizate', views.modifProfil, name="changeprofil"),

    path('detay-sou-travay-la/<int:id>/', views.detailJob, name="details-work"),

    path('ajoute-yon-projet', views.projectUser, name="projects"),
    path('tout-potfolio-itilizate-sa', views.viewpotfolio, name='mypotfolios'),

    path('efase-yon-potfolio/<int:id>/', views.delpotfolio, name='del'),
]
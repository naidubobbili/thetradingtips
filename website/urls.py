from django.urls import path
from website import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('hello/',views.hello),
    path('',views.shortview,name=''),
    path('<int:id>',views.detailview,name='detail'),
    path('documents',views.documentview,name='document')

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

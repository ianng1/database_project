
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf.urls.static import static
import students.views


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students.views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('students/', include('students.urls')),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('create/', students.views.create, name='create'),
    path('home/', students.views.home, name='home'),
    path('data/<int:student_id>', students.views.data, name='data'),
    path('detail', students.views.data, name = 'detail'),
    path('students/delitem', students.views.delitem, name='delitem'),
    path('students/additem', students.views.additem, name='additem'),
]

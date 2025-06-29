
from django.contrib import admin
from django.urls import path,include
from application import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('reg_home/', views.reg_user, name='reg_home'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('workoutlib/', views.worklib, name='worklib'),
    path('login/', views.login_user, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_login__page/', views.user_login_page, name='user_login_page'),
    path('user_logins/', views.user_logins, name='user_logins'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('adduser/', views.add_user, name='adduser'),
    path('alluser/', views.alluser, name='alluser'),
    path('after_alluser/', views.after_alluser, name='after_alluser'),

    path('logout_user/', views.logout_user, name='logout_user'),
    path('login/', views.logout, name='logout'),


    path('precustomplan/', views.precustomplan, name='precustomplan'),
    path('customizeplan/<int:id>/', views.customizeplan, name='customizeplan'),
    path('customplan/', views.customplans, name='customplan'),

    path('getyourplan/', views.getyourplan, name='getyourplan'),
    path('searchplan/', views.searchplan, name='searchplans'),

    path('feedbacks/', views.feedbacks, name='feedbacks'),



    path('displayplan/', views.displayplan, name='displayplan'),
    path('modifyuser/', views.modifyuser, name='modifyuser'),
    path('delete/<int:id>/', views.delete_record, name ='delete_record'),
    path('edit/<int:id>/', views.edit_record, name ='edit_record'),
    path('update/<int:id>/', views.update_record, name ='update_record'),

    path('reject_reg/<int:id>/', views.reject_reg, name ='reject_reg'),
    path('check_approve/<int:id>/', views.approve_reg, name ='approve_reg'),
    path('verified_reg/<int:id>/', views.verified_reg, name ='verified_reg'),






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
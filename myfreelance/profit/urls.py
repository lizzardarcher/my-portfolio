from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.IndexPage.as_view(), name='home'),
    path('portfolio', views.PortfolioTemplateView.as_view(), name='portfolio'),
    path('projects', views.ProjectListView.as_view(), name='project'),
    path('project_details/<int:pk>', views.ProjectDetailsView.as_view(), name='project'),
    path('create_project', views.ProjectCreateView.as_view(), name='create project'),
    path('create_portfolio_project', views.PortfolioProjectCreateView.as_view(), name='create portfolio project'),
    path('update_project/<int:pk>', views.ProjectUpdateView.as_view(), name='update project'),
    path('delete_project/<int:pk>', views.ProjectDeleteView.as_view(), name='delete project'),

    path('support_payment_details/<int:pk>', views.SupportPaymentsDetailsView.as_view(), name='spd'),
    path('create_support_payment', views.SupportPaymentsCreateView.as_view(), name='create sp'),
    path('update_support_payment/<int:pk>', views.SupportPaymentsUpdateView.as_view(), name='update sp'),
    path('delete_support_payment/<int:pk>', views.SupportPaymentsDeleteView.as_view(), name='delete sp'),

    path('create_additional_payment', views.AdditionalPaymentsCreateView.as_view(), name='create sp'),
    path('update_additional_payment/<int:pk>', views.AdditionalPaymentsUpdateView.as_view(), name='update sp'),
    path('delete_additional_payment/<int:pk>', views.AdditionalPaymentsDeleteView.as_view(), name='delete sp'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
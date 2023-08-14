from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('add/',views.StoreView.as_view(),name='add'),
    path('show/',views.ShowView.as_view(),name="show"),
    path('delete/<int:pk>',views.DeleteTaskView.as_view(),name="delete"),
    path('edit/<int:pk>',views.EditView.as_view(),name="edit"),
    path('completed/<int:pk>',views.CompletedTaskView.as_view(),name="completed"),
    path('complete/',views.CompleteView.as_view(),name="complete"),
]

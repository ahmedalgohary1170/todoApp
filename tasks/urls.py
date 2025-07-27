from django.urls import path
from . import views

# urlpatterns =[
#     path('',views.list_todo),
#     path('add',views.add_todo),
#     path('edit/<int:pk>',views.edit_status),
#     path('delete/<int:pk>',views.delete_todo)

# ]

urlpatterns =[
    path('',views.TaskCreateView.as_view(), name='todo'),
    path('add',views.TaskCreateView.as_view()),
    path('edit/<int:pk>',views.edit_status),
    path('delete/<int:pk>',views.TaskDeleteView.as_view())

]


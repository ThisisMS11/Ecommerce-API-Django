from django.urls import path
from notes.views import NotesViews

app_name = "notes"

urlpatterns=[
    # CRUD
    path('create/',NotesViews.as_view(),name='notes'),
    # path('/:id',UserViews.as_view(),name='register'),
    # path('update/:id',UserViews.as_view(),name='register'),
    # path('delete/:id',UserViews.as_view(),name='register'),
]
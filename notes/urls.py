from django.urls import path
from . import views

app_name = "notes"

urlpatterns=[
    path("",views.ListNotesView.as_view()),
    path("create/",views.NotesViews.as_view()),
    path("delete/<int:id>", views.DeleteNoteViews.as_view()),
    path("update/<int:id>", views.UpdateNoteViews.as_view()),
]
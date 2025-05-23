from django.contrib import admin

from django.urls import path


from start import views


urlpatterns = [ 
    #path("", views.index, name="index"),
    path("imain/", views.imain, name="imain"),
    path("", views.register, name="register"),
    path("signin/", views.signin, name="signin"),
    path("details/", views.details, name="details"),
    path("reset/", views.reset, name="reset"),
    path('ChangePassword/<token>/', views.ChangePassword, name='ChangePassword'),
    
    path("gmail/", views.Cmail, name="Cmail"),

    path("net/", views.net, name="net"),
    path("sent/", views.emailsent, name="emailsent"),
    path("draft/", views.draft, name="draft"),
    # path("trash/", views.trash, name="trash"),
    path("pk/", views.pk, name="pk"),
    path("gk/", views.gk, name="gk"),
    path("inbox/", views.inbox, name="inbox"),
    #path("ttm/", views.propic, name="propic"),
    path("pk/", views.propic, name="propic"),
    path("delete_emailsent/<int:myid>/", views.emailsent, name="emailsent"),
    path("gmail/", views.gmail, name="gmail"),
    path("next/", views.next, name="next"),

    path("student_registration/", views.student_registration, name="student_registration"),

    path("view_students/", views.view_students, name="view_students"),

    path("student_login/", views.student_login, name="student_login"),
    path("profile/", views.profile, name="profile"),
    path("gmail2/", views.gmail2, name="gmail2"),

    # path("delete_next/<int:myid>/", views.delete_next, name="delete_next"),

    # path('trash/', views.trash, name='trash'),
    # path('trash/restore/<int:pk>/', views.restore_item, name='restore_item'),
    # path('trash/delete/<int:pk>/', views.hard_delete_item, name='hard_delete_item'),


    path('delete/<int:myid>/', views.delete_next, name='delete_next'),
    path('restore/<int:myid>/', views.restore_item, name='restore_item'),
    path('hard_delete/<int:myid>/', views.hard_delete_item, name='hard_delete_item'),
    path('trash/', views.trash_view, name='trash_view'),

    path('Profile_register/', views.Profile_register, name='Profile_register'),
    # path('edit/<int:pk>/', edit_register, name='edit_register'),


    path("edit/<int:pk>", views.edit, name="edit"),
    # path('Todo/', views.Todo, name='Todo'),
   

    # path('gmail2/', views.inbox_view, name='inbox_view'),

]

 
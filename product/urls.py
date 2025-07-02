from django.contrib import admin
from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('item/<int:prod_id>', view=views.detail, name="prod-detail"),
    # path('detail/<string: prod_id>', view=)
    path('checkout/', view=views.checkout, name='checkout'),
]   
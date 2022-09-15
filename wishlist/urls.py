from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import menerima_fungsi
from wishlist.views import menerima_fungsi_json
from wishlist.views import menerima_request_id_json
from wishlist.views import menerima_request_id_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', menerima_fungsi, name='menerima_fungsi'),
    path('json/', menerima_fungsi_json, name='menerima_fungsi_json'),
    path('json/<int:id>', menerima_request_id_json, name='menerima_request_id_json'),
    path('json/<int:id>', menerima_request_id_xml, name='menerima_request_id_xml'),
]
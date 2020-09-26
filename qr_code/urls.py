from django.urls import path

from qr_code import views


app_name = 'qr_code'
urlpatterns = [
    path('images/serve-qr-code-image/', views.serve_qr_code_image, name='serve_qr_code_image')
]

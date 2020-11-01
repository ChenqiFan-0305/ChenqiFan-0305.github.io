from django.urls import path
from sim_rating import views

urlpatterns = [
    path('', views.main, name='main'),
    path('sim_rates/a', views.SimRateView1, name='similarity-rates'),
    path('sim_rates/b', views.SimRateView1, name='similarity-rates2'),
    path('sim_rates/c', views.SimRateView1, name='similarity-rates3'),
    path('sim_rates/d', views.SimRateView1, name='similarity-rates4'),
    path('sim_rates/e', views.SimRateView1, name='similarity-rates5'),
    path('sim_rates/f', views.SimRateView1, name='similarity-rates6'),
    path('sim_rates/end', views.end, name='end'),
    
    ]


# 1. main_page add id input
# 2. click submit to submit the data and redirect to the next page
# 3. change the similarity of two articles to 7 fixed values
# 4. every article will have one visible rolling
# 5. add a process line in the beside part

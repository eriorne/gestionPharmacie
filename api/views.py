from rest_framework import viewsets

from .models import *

class medicamentViewSet(viewsets.ModelViewSet):
	queryset = medicament.objects.all()
	

class AchatViewSet(viewsets.ModelViewSet):
	queryset = Achat.objects.all()   


class VenteViewSet(viewsets.ModelViewSet):
	queryset = Vente.objects.all()
	    



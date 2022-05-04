from django.shortcuts import render, redirect
from .models import Mijoz
from django.db.models import Count
from .forms import MijozForm

def index(request):

	form = MijozForm()
	if request.method == 'POST':
		form = MijozForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	nomers = Mijoz.objects.latest('id')
	raqam  = nomers.nomer.upper()

	q = Mijoz.objects.all()
	soni = 0
	for x in q:
		if raqam==x.nomer.upper():
			soni += 1
	text = None
	if soni % 5 == 0:
		text = f'Bu sizning {soni} xaridingiz. Bonusga egasiz'

	context = {'form':form,'soni':soni, 'text':text, 'raqam':raqam}

	return render(request, 'index.html', context)

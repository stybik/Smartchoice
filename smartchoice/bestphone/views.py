from django.shortcuts import render
from .models import table_11
# Create your views here.
def home(request):
	return render(request,"index.html")

def index(request):
	input1 = request.POST['input1']
	input2 = request.POST['input2']
	try:
		q1 = table_11.objects.order_by('-result').filter(price__range = (input1,input2))
				#q2 = table_11.objects.get(price <= input2)
	except table_11.DoesNotExist:
		q1 = "Not found"
	context = {
	"q1":q1,
	}	
	return render(request,"result.html",context)


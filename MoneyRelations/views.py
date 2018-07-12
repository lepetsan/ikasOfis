from django.shortcuts import render
from django.http import HttpResponse
from .forms import CountryForm
from django.shortcuts import render_to_response
from django.template import RequestContext


from django.shortcuts import render
from django.shortcuts import redirect
from .models import Expense

def index_redirect(request):
    return redirect('/table/')





# Create your views here.

def index(request):
    all_members = Expense.objects.all()
    return render(request, 'expense/index.html', {'all_members': all_members})


def countries_view(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('countries')
            # do something with your results
    else:
        form = CountryForm

    return render_to_response('render_country.html', {'form':form },
        context_instance=RequestContext(request))


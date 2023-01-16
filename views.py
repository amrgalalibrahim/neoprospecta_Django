from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OTU

@login_required
def otu_table_view(request):
    otu_table = OTU.objects.all().order_by('taxon_name', 'frequency')
    context = {'otu_table':otu_table}
    return render(request, 'otu_table/otu_table.html', context)


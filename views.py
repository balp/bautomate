# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from bautomate.models import TelldusDevice
try:
    from telldus import telldus 
except ImportError:
    from bautomate.telldus_dummy import telldus
td_core = telldus.TelldusCore()

def index(request):
    device_list = TelldusDevice.objects.all()
    return render_to_response('bautomate/index.html',
                               {'device_list': device_list},
                               context_instance=RequestContext(request))

def switch(request, device_id):
    tdDev = get_object_or_404(TelldusDevice, pk=device_id)
    to = request.POST.get('to', False)
    print "Debug:", to
    if to == 'on':
        status = td_core.lib.tdTurnOn(tdDev.td_id)
        tdDev.on = True
    else:
        status = td_core.lib.tdTurnOff(tdDev.td_id)
        tdDev.on = False
    tdDev.save()
    return HttpResponseRedirect(reverse('bautomate.views.index'))
    
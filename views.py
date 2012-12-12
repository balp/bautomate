# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from bautomate.models import TelldusDevice
import telldus.telldus 

td_core = telldus.telldus.TelldusCore()

def index(request):
    device_list = TelldusDevice.objects.all()
    return render_to_response('bautomate/index.html', {'device_list': device_list})

def on(request, device_id):
    tdDev = get_object_or_404(TelldusDevice, pk=device_id)
    status = td_core.lib.tdTurnOn(tdDev.td_id)
    tdDev.on = True
    tdDev.save()
    return HttpResponseRedirect(reverse('bautomate.views.index'))

def off(request, device_id):
    tdDev = get_object_or_404(TelldusDevice, pk=device_id)
    status = td_core.lib.tdTurnOff(tdDev.td_id)
    tdDev.on = False
    tdDev.save()
    return HttpResponseRedirect(reverse('bautomate.views.index'))

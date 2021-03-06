# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import simplejson

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
    def get_json_response(content, **httpresponse_kwargs):
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)
    tdDev = get_object_or_404(TelldusDevice, pk=device_id)
    to = request.POST.get('to', False)
    if to == 'on':
        td_core.lib.tdTurnOn(tdDev.td_id)
        tdDev.on = True
    else:
        td_core.lib.tdTurnOff(tdDev.td_id)
        tdDev.on = False
    tdDev.save()
    if request.is_ajax():
        tmp = simplejson.dumps(tdDev.as_dict())
        return get_json_response(tmp)
    else:
        return HttpResponseRedirect(reverse('bautomate.views.index'))
    
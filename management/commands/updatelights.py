from django.core.management.base import BaseCommand, CommandError
from bautomate.models import TelldusDevice
import telldus.telldus 
import telldus.constants

class Command(BaseCommand):
    args = ''
    help = 'Updates the polls in the database to match telldusd.'

    def isDeviceOn(self, device):
        state = device.last_sent_command(telldus.constants.TELLSTICK_TURNON|telldus.constants.TELLSTICK_TURNOFF)
        if state == telldus.constants.TELLSTICK_TURNON:
            return True
        return False
    def handle(self, *args, **options):
        #dbobjects = TelldusDevice.objects.all()
        core = telldus.telldus.TelldusCore()
        devices = core.devices()
        for device in devices:
            try:
                td = TelldusDevice.objects.get(td_id=device.id)
            except TelldusDevice.DoesNotExist:
                td = TelldusDevice(td_id=device.id, name=device.name, on=self.isDeviceOn(device))
            td.on = self.isDeviceOn(device)
            td.save()



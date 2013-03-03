"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import TimerPeriod
import datetime

class TestTime(TestCase):
    def test_on_piriod(self):
        tp = TimerPeriod(start_time=datetime.time(8,00),
                end_time=datetime.time(9,00))
        self.assertEqual(True, tp.status(time=datetime.time(8,01)))

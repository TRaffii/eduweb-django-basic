from django.test import TestCase

# Create your tests here.
from .models import Icecream


class IcecreamModelTests(TestCase):

    def test_icecream_is_not_featured_when_price_is_default(self):
        icecream = Icecream(name='Test', is_featured=True)
        icecream.save()
        self.assertEqual(icecream.is_really_featured(), False)

    def test_icecream_is_featured_when_price_is_not_default_and_is_featured_is_true(self):
        icecream = Icecream(name='Test', is_featured=True, price=2)
        icecream.save()
        self.assertEqual(icecream.is_really_featured(), True)

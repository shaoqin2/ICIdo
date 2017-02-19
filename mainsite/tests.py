from django.test import TestCase
from mainsite.models import Portfolio
from mainsite.models import Category
from mainsite.models import User
from mainsite.models import Donor
from mainsite.models import Donation


# Create your tests here.
class PortfolioTest(TestCase):
    def setUp(self):
        Portfolio.name.create(name="profolio")
        Portfolio.name.create(name="Women's Fund")

    def test_portfolio_to_str(self):
        pro = Portfolio.__getattribute__(self, )

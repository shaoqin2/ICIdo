from models import Donor
from models import Donation


donation = Donation()
donor = Donor()

donor.first_name = "FirstName"
donor.last_name = "LastName"

print Donor.__str__(donor)



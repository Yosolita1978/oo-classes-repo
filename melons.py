"""This file should have our order classes in it."""
import random
from datetime import datetime, time
# import time


class AbstractMelonOrder(object):
    """ This is the super parenth class for melons """

    def __init__(self, species, qty, country_code="US"):
        """This initialize the melon order """

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08
        self.country_code = country_code

    def get_base_price(self):
        self.base_price = random.randint(5, 10)
        weekday = datetime.today().weekday()
        now = datetime.now()
        now_time = now.time()
        if weekday >= 0 and weekday <= 4 and now_time >= time(8, 0) and now_time <= time(11, 0):
            self.base_price += 4
        return self.base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total = total + 3
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """ This is only for the Government orders"""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Set inspection to true."""

        self.passed_inspection = passed

    def get_passed_inspection(self):
        """Return the inspection."""

        return self.passed_inspection


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize domestic order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize international order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

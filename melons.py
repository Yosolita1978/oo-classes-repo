"""This file should have our order classes in it."""


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

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


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

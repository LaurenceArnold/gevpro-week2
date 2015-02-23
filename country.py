#!/usr/bin/env python

"""This class generates a Country which when called can greet you from that country"""

class Country:
    def __init__(self,country):
        self.country=country

    def getCountry(self):
        """Returns the country"""
        return self.country

    def __str__(self):
        return ("Hello from {} ".format(self.country))

if __name__== "__main__":
    main()

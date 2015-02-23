#!/usr/bin/env python

import sys

from country import *

def main():
    countryList=[]
    with open('countries_list.txt') as in_f:
         for line in in_f:
             x = line.split('\n')
             countryList.append(x[0])    

    for land in countryList:
        land=Country(land)
        print(land)

if __name__== "__main__":
    main()

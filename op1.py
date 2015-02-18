#!/usr/bin/env python

import sys

from country import *

def main():
    #for land in open("countries_list.txt","r"):
     #   country=Country(land)
      #  print(country)

    lijst=[]
    with open('countries_list.txt') as in_f:
        for line in in_f:
            x = line.split('\n')
            lijst.append(x)

    lijst2=[]
    for i in lijst:
        lijst2.append(i[0])

    for land in lijst2:
        land=Country(land)
        print(land)

if __name__== "__main__":
    main()

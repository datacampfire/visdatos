#!/usr/bin/python3
import pandas

df = pandas.read_json("treemap/generacion-solar.json")
df.to_csv("treemap/generacion-solar.csv", sep=',')

'''
Really simple converter from json to csv using Python
'''

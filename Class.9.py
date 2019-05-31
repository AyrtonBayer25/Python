import os
import csv
os.chdir(os.path.dirname(__file__)

abc = os.path.join("..","Resources","netflix_ratings.csv")
with open(abc, newline ="") as abcd:
    xyz=csv.reader(abcd,delimiter=',')
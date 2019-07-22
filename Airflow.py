#python core
import datetime
import logging


#external module
import pandas as pd
import  requests

#import luigis
import luigi
from luigi.contrib  import redshift, s3

logger =  logging.getLogger('luigi-interface')

#meta data
_author_ = 'Dillion'
_date_ = '2018-01-30'

DATE_FORMAT = '%Y-%m-%d'
DATEHOUR_FORMAT ='%Y-%m-%dT%H'
DATEMINUTE_FORMAT = '%Y-%m-%dT%H%M'

class path (luigi.Config):
    tos3 = luigi.Parameter()
    s3_load_bucket = luigi.Parameter()

class redshift(luigi.Config):
    host =  luigi.Parameter(default='')
    database = luigi.Parameter(default= '')
    user = luigi.Parameter(default= '')
    password = luigi.Parameter(default= '')

class s3 (luigi.Config):
    aws_access_key_id = luigi.Parameter(default= '')
    aws_secret_access_key = luigi.Parameter(default= '')

class Exampletask(luigi.WrapperTask):
    date = luigi.DateHourParameter(default=datetime.datetime.utcnow())
    def requires(self):
        jobs = [
            {'table': 'your_table',
             'fn': 'my_file'
            },

            {'table':'your_table',
             'fn':'your_file'

            }

    ]
    for job in jobs:
        yield  RedshiftCopy(
    
        )


### stop here and create classes

class shark:
    def __init__(self):
        print("This is the constructor method")

    def swim(self):
        print("The shark can swim")
    def dangerous(self):
        print("the sjhark will eat you")


def main():
    sammy = shark()
    sammy.swim()
    sammy.dangerous()

if __name__ == "__main__":
    main()


sammy = shark()
print(sammy)

##version 2
class dolphin:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + "is swimming")

    def dangerous(self):
        print(self.name + " will eat you")

def main():
    sammy = dolphin("Sammy")
    sammy.swim()
    sammy.dangerous()


#self in def
class car():
    #init or constructor method

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print ("Model is ", self.model)
        print("color is", self.color)

audi = car("audi a4", "blue")
ferrari = car

#func in func
def shout(text):
    return text.upper()
def whisper (text):
    return text.lower()

def  greet(func):
    greetings = func("This is a FUNCTION passed in another")
    print(greetings)

greet(shout)
greet(whisper)

# return anther function
 def create_adder(x):
     def adder(y):
        return  x+y

        return adder






# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print add_15(10)

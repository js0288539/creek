# -*- coding: utf-8 -*-

"""
Created on Sun Mar 29 14:24:39 2020

@author: RADeighan
"""

#%% IMPORT
import datetime as dt
import dateutil as dtutil
import re

#%% CLASS

# ------------------------------
class Dog:
        """ A simple attempt to model a dog. """
        def __init__(self,name,age):
            self.name = name
            self.age = age
            self.state = "awake"
            self.action = "standing"
            self.location = "at the door"
            self.sex = 'male'
            self.breed = 'German Shepard'
            self.birthday = dt.datetime.now() - dtutil.relativedelta.relativedelta(years=age)
        
        def action_sit(self):
            print(f"{self.name}, SIT!")
            print(f">>> {self.name} is now sitting!")
            self.action = "sitting"
            
        def action_roll_over(self):
            print(f"{self.name}, ROLL OVER!")
            print(f">>> {self.name} rolled over!")
            self.action = "prone"

# ------------------------------
class Restaurant:
    def __init__(self,name,cuisine,state="closed"):
        self.name = name
        self.cuisine = cuisine
        self.state = state
        
    def describe(self):
        print(f"{self.name} servers {self.cuisine} food and is now {self.state}.")
        
    def mopen(self):
        self.state = "open"
        
    def mopen(self):
        self.state = "closed"

class Flavor:
    default_flavors = ['Chocolate','Vanilla','Strawberry']
    
    def __init__(self,flavors=default_flavors):
        self.flavors = flavors
    
    def display_flavors(self):
        return self.flavors
    
    def update_flavors(self,flavors):
        self.flavors = flavors
        return True

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine,state):
        super().__init__(name, cuisine,state)
        self.flavors = Flavor()

# ------------------------------
class User:
    def __init__(self,fname,lname,age,sex,ethnicity,empID):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.empID = empID
        self.privileges_dict = {   # No privilege by default
               'post' : '', # CRUD
               'user' : '', # CEDT
               'channel' : '', # CRUD
               'backup' : '', #FI
               'restore' : '' # LFIU
            }
        
    def describe(self):
        print(f' name:\t{self.fname} {self.lname}\n age:\t{self.age}\n sex:\t{self.sex}\n ethnicity:\t{self.ethnicity}\n empID:\t{self.empID}')



class Admin(User):
    def __init__(self,fname,lname,age,sex,ethnicity,empID):
        super().__init__(fname, lname, age, sex, ethnicity, empID)
        # post'CRUD'         # create, read, update, delete
        # user'CDAI'          # create, update, read, delete, active, inactive
        # channel'CRUDO'      # create, read, update, delete
        # backup'FI'         # full, incremental
        # restore'LFU'       # list,full, incremental, user
        self.allowed_modules = ['post','user','channel','backup','restore']
        self.active_roles = ['Admin','Operator','Moderator','User']
        self.role = 'Admin'
        self.privileges = ['create post','delete post','update post','disable user','enable user','timeout user']
        self.privileges_dict['post'] = 'CRUD'
        self.privileges_dict['user'] = 'CRUD' # U=>active and inactive
        self.privileges_dict['channel'] = 'CRUD' # U=>Archived or Active
        self.privileges_dict['backup'] = 'FI'
        self.privileges_dict['restore'] = 'LFU'
        
    def has_priv(self,key,priv):
        bstate = False
        allowed = self.privileges_dict[key]
        for p in allowed:
            bstate = bstate or (p == priv)
        return bstate
    
    def set_Admin(self):
        self.role = 'Admin'
        self.privileges_dict = {
               'post'    : 'CRUD',
               'user'    : 'CRUD',
               'channel' : 'CRUD',
               'backup'  : 'FI',
               'restore' : 'LFU'
            }
        return True
    
    def set_Operator(self):
        self.role = 'Operator'
        

        
#%% MAIN

# now = dt.datetime.now()
# birthday = dt.datetime.now() - dtutil.relativedelta.relativedelta(years=3)

d1 = Dog('Willie',6)
print(f"My dog's name is {d1.name}")
print(f"My dog is {d1.age} years old")
print(f"Myd dog is {d1.action} {d1.location}")

d1.action_sit()
d1.action_roll_over()
print(f"My dog is now {d1.action} {d1.location}")

#%%

r1 = Restaurant(name="Donught World",cuisine="American",state="open")
r2 = Restaurant(name="Bobbie's", cuisine="Italian",state="closed")
r3 = Restaurant(name="The Tea House",cuisine="Japanise", state="open")
r1.describe()
r2.describe()
r3.describe()

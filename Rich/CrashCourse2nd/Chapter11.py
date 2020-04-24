# -*- coding: utf-8 -*-

#%%
## INITIALIZATION
# add in local paths
sys.path.append('F:/Public/Creek/Rich/LocLib/chapter_11')

#%%
## IMPORT
import sys 
import unittest

# we eventuall need to put these things in a central location
from name_function import get_formatted_name


#%%
## FUNCTIONS

#%%
## DEFINES

#%%
## CLASSES
class NamesTestCase(unittest.TestCase):
    """Tests for the name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

#%%
## MAIN 01

if __name__ == '__main__':
    unittest.main()
    

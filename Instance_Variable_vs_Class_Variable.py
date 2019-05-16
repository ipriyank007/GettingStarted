'''
Created on Feb 18, 2019

@author: Priyank007
'''

class Girls:
    '''
    classdocs
    '''
    gender = "Female"

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        print(self.name)
       
Sandy = Girls('snady')
print(Sandy.gender)

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

Sandy = Girls('Sandy')
print(Sandy.gender)
print(Sandy.name)
Barbara = Girls('Barbara')
print(Barbara.gender)
print(Barbara.name)
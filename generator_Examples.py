# num_list = [1,2,3,4,5]
#
# def square_Nums(nums):
#     for i in nums:
#         yield i*i
#
# my_num = square_Nums(num_list)
# print(next(my_num))

import memory_profiler as mem_profile
# help(mem_profile)
import random
import time

names = ['Rahul', 'Sumit', 'Saqueeb', 'Priyanka']
majors = ['Maths', 'Civics', 'Mechanics', 'Economics']

print('Memory before: {}mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name':random.choice(names),
            'course':random.choice(majors),
        }
        result.append(person)
    return(person)

def people_generator(sum_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'course': random.choice(majors),
        }
        yield person
t1 = time.clock()
people = people_generator(1000)
t2= time.clock()
print('Memory after: {}mb'.format(mem_profile.memory_usage()))
print('Took {} time'.format(t2-t1))
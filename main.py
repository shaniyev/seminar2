from mybox import MyBox
from myclass import my_point

a = my_point(5,6)
b = my_point(1,2)
box = MyBox([a,b])

box.add('One')
box.add(2)
box.add(True)
box.add('Hello')
box.add(5)
box.add('Done')


box.remove('Hello')
if ('One' in box) and (len(box) > 0):
    box.remove('One')

for i in box:
    print(i)
 

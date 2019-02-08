from mybox import MyBox

box = MyBox()

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
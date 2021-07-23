s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)

dic={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
list={}
count=0
for value in dic.values():
    if count<=1:
        count=count+1
    list.update({value:count})
print(list)



dic={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
total_length=0
for value in dic.values():
    length=len(value)
    total_length=total_length+length
print(total_length)



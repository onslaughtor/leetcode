from operator import itemgetter

l1 = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]  
print sorted(l1,key = lambda x:x['age'],reverse=True)
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]  
print sorted(students, cmp=lambda x,y : cmp(x[2], y[2]))
print sorted(students, key=itemgetter(2)) 
print sorted(students, key=itemgetter(1,2)) 
#Rotate an array

print "Rotate an Array\n"

def rotate(l, n):
   print l
   print n
   t =  l[-n:] + l[:-n]
   print t
   

example_array = [1, 2, 3, 4, 5]

rotate(example_array, 2)
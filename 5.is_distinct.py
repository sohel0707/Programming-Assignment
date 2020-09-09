arr1=[3,2,5,4,6]
arr2=[7,8,9,0,10]

if len(set(arr1).intersection(set(arr2)))==0:
    print("distinct")
else:
    print("not distinct")


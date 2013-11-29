import cloud

def mult(x,y):
    return x*y
jids = cloud.map(mult, [1,3,5], [2,4,6]) 

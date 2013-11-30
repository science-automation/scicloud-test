import cloud.mp

def mult(x,y):
    return x*y
jid = cloud.mp.map(mult, [1,3,5], [2,4,6]) 
result = cloud.mp.result(jid)
print result

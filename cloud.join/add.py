import cloud

def add(x, y):
    return x + y
jid = cloud.call(add, 1, 2) 
cloud.join(jid)
answer = cloud.result(jid)
print answer

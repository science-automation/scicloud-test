import cloud

def add(x, y):
    return x + y
jid = cloud.call(add, 1, 2) 
cloud.join(jid,timeout=20,ignore_errors=True,deadlock_check=False)
answer = cloud.result(jid)
print answer

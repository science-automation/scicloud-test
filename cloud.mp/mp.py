import cloud.mp

jid = cloud.mp.call(lambda: 3*3)
answer = cloud.mp.result(jid)
print answer

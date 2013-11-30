import cloud
jid = cloud.call(lambda: 3*3)
cloud.join(jid)
answer = cloud.result(jid)
print answer

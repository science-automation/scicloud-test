import cloud
jid = cloud.call(lambda: 3*3)
answer = cloud.result(jid)
print answer

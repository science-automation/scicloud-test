import cloud

def infinite_loop():
        while True:
                pass

jid = cloud.call(infinite_loop) #start a job which will never end
cloud.kill(jid)                 #at least until you kill it

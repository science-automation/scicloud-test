import cloud
import sys

def foo():
        print "Output"
        print >> sys.stderr, "An Error"
        sys.stdout.flush()
        sys.stderr.flush()

jid = cloud.call(foo)
cloud.join(jid)
cloud.info(jid, ['stderr', 'stdout'] )
#returns {jid: {'stderr': 'An Error\n', 'stdout': 'Output\n'}}
result = cloud.info(jid, ['stdout', 'memory.failcnt', 'cputime.user'])
print result

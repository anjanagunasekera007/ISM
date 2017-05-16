import threading

def f():
    # do something here ...
    # call f() again in 60 seconds
    print "Executing"
    threading.Timer(2, f).start()

# start calling f now and every 60 sec thereafter
f()
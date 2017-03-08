# -*- coding: utf-8 -*-

import sys, traceback, Ice
import Arithmetic

status = 0
ic = None
IPdirection = "localhost"
portDest = "12545"
try:
    ic = Ice.initialize(sys.argv)
    base = ic.stringToProxy("Arithmetic:default -h " + directionIP + " -p " + portDest)
    natural = Arithmetic.NaturalPrx.checkedCast(base)
    if not natural:
        raise RuntimeError("Invalid proxy")

    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print "Calling server to substract", a, "-", b, "= ",natural.substract(a, b)

except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)

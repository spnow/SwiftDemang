import idaapi
import idautils
import os

# SwiftDemang
__author__ = "Tyler Halfpop"
__version__ = "0.1"
__license__ = "MIT"

# Location of the demangled file
demangled_file = "{}{}{}_demangled.txt".format(
    os.getcwd(), os.sep, GetInputFile())

print "Attempting to rename functions to demangled Swift names\n"

# Loop over the demangled file and rename the functions in IDA
with open(demangled_file, "rb") as df:
    for l in df:
        try:
            addr, name = l.split(",")
            addr = int(addr, 16)
            name = name.split(" :")[0].split(" (")[0].strip("\n")
            MakeNameEx(addr, name, SN_NOCHECK | SN_NOWARN)
            print "{} {}".format(hex(addr).strip("L"), name)
        except:
            pass

print "SwiftDemang renaming done."

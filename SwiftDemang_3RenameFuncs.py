import idaapi
import idautils
import os

# SwiftDemang
__author__ = "Tyler Halfpop"
__version__ = "0.2"
__license__ = "MIT"

# Location of the demangled file
#demangled_file = "{}{}{}_demangled.txt".format(
#    os.getcwd(), os.sep, GetInputFile())
demangled_file = AskFile(0, "*", "Demangled File")

print "Attempting to rename functions to demangled Swift names\n"

# Loop over the demangled file and rename the functions in IDA
with open(demangled_file, "rb") as df:
    for l in df:
        try:
            addr, full_name = l.split(",")
            addr = int(addr, 16)
            new_name = full_name.split(" :")[0].split(" (")[0].strip("\n")
            old_name = idc.GetFunctionName(addr)
            if new_name != old_name:
                MakeNameEx(addr, new_name, SN_NOCHECK | SN_NOWARN)
                SetFunctionCmt(addr, "{} \n{}".format(old_name, full_name), 1)
                print "{} {}".format(hex(addr).strip("L"), name)
        except:
            pass

print "SwiftDemang renaming done."

import idaapi
import idautils
import os

# SwiftDemang
__author__ = "Tyler Halfpop"
__version__ = "0.2"
__license__ = "MIT"

# Mangled Function Saved File
#mangled_file = "{}{}{}_mangled.txt".format(os.getcwd(), os.sep, GetInputFile())
mangled_file = AskFile(1, "*", "Output File")

print "Generating list of mangled Swift function names and addresses:\n{}".format(mangled_file)

# Loop through the functions in IDA and write the address and name to a file
count = 0
with open(mangled_file, "wb") as f:
    for func in idautils.Functions():
        f.write("{},{}\n".format(hex(func).strip("L"), idc.GetFunctionName(func)))
        count += 1

print "{} Mangled functions found".format(count)
print "Next run: python SwiftDemang_2GenDemang.py {}".format(mangled_file)

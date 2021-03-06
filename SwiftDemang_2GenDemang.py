import subprocess
import sys

# SwiftDemang
__author__ = "Tyler Halfpop"
__version__ = "0.2"
__license__ = "MIT"

# Location of swift-demangle binary
swift_demangle = '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swift-demangle'


def usage():
    """
    Prints usage if mangled file isn't specified
    """
    print "Specify generated mangled functions file as arg"


def demangle(name):
    """
    Run the swift-demangle binary to obtain just the demangled name with compact
    """
    try:
        return subprocess.check_output([swift_demangle, '-compact', name], stderr=subprocess.PIPE)
    except:
        return name


def main(mangled_file):
    """
    Loop over the mangled file and get the demangled name from swift-demangle
    then write the result and address to the new demangled file
    """

    # New filename
    demangled_file = "{}_demangled.txt".format(
        mangled_file.strip("_mangled.txt"))

    # Open mangled file to read, demangled file to write, and write results
    with open(mangled_file, "rb+") as mf:
        with open(demangled_file, "wb") as df:
            print "Generating demangled file {}".format(demangled_file)
            for l in mf:
                addr, func = l.split(",")[0], l.split(",")[1].rstrip()
                print "Attempting Demangling: {}".format(func)
                df.write("{},{}".format(addr, demangle(func)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        main(sys.argv[1])

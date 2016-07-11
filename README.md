# SwiftDemang

IDA Pro IDAPython Script to Demangle Swift

## HowTo

1. Run SwiftDemang_1GetFuncs.py in IDA to generate the mangled functions list
2. Run python SwiftDemang_2GenDemang.py file_mangled.txt to generate the demangled functions list.  
  * This step requires the swift-demangle binary that is included in [XCode](https://swift.org/download/)
3. Run SwiftDemang_3RenameFuncs.py in IDA to rename the functions

### Example
![example](https://raw.githubusercontent.com/tylerhalfpop/SwiftDemang/master/example.png)

## Credits
Idea from [gsingh93](https://github.com/gsingh93/ida-swift-demangle), but I have Windows IDA and I wanted to rename the functions and work with Mac Swift.



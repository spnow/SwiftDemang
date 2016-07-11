# SwiftDemang

IDA Pro IDAPython Script to Demangle Swift

## HowTo

1. From IDA run: 
  ```
  SwiftDemang_1GetFuncs.py 
  ```
  to generate the mangled functions list
2. From the terminal run: 
  ```
  python SwiftDemang_2GenDemang.py file_mangled.txt 
  ```
  to generate the demangled functions list.  
  * This step requires the swift-demangle binary that is included in [XCode](https://swift.org/download/).
  In XCode 7.3.1 it's located in this location, which is where the script points to by default:
  ```
  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swift-demangle
  ```
3. From IDA run:
  ```
  SwiftDemang_3RenameFuncs.py 
  ```
  to rename the functions

### Example
![example](https://raw.githubusercontent.com/tylerhalfpop/SwiftDemang/master/example.png)

## Credits
Idea from [gsingh93](https://github.com/gsingh93/ida-swift-demangle), but I have Windows IDA and I wanted to rename the functions and work with Mac Swift.



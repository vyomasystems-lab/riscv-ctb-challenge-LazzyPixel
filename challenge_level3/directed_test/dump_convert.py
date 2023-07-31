'''
Doc:
Below are the execution ways of this script

    1.  Without providing output file
        > python3 script.py spike.dump 

    2.   With  output file
        > python3 script.py spike.dump output.dump 

'''
import sys
import os
import re

n = len(sys.argv)
print("Total arguments passed in script:", n)

# Different Files used in the script
input_file=sys.argv[1]
dasm_file = 'dasm_' + input_file
if n==3 :
    output_file=sys.argv[2]
else :
    output_file="readable_" + input_file

print("Input Dump File:", input_file)
print("Output Dump File:", output_file)

# If input file is not available just to test, write a file
#f = open(input_file, "a")
#f.write("3 0x800022c0 (0x0cc15a03) x20 0x00003002 \n 3 0x800022c4 (0x1390e813) x16 0xfffff7fd \n 3 0x800022c8 (0x21c11903) x18 0xfffff581 \n 3 0x800022cc (0x9fc12803) x16 0xffffffeb \n 3 0x800022d0 (0xe0e15a83) x21 0x00003a03 \n 3 0x800022d4 (0x00000033) x 0 0x00000000 \n 3 0x800022d8 (0xebf99ee3) x 0 0x00000000 \n 3 0x800022dc (0x00000033) x 0 0x00000000 \n 3 0x800022e0 (0xdc1103a3) x 0 0x00000000 \n 3 0x800022e4 (0x9b211803) x16 0xffffc7d2")
#f.close()

#Open and read the file:
f = open(input_file, "r")
temp = f.read()
f.close()

temp = re.sub("\(", '"DASM(', temp)
modified_contents = re.sub("\)", ')"', temp)

#Print modified DASM dump on terminal
'''
print("modified DASM : ==========>\n")
#print(modified_contents)
'''

f = open(dasm_file, "a")
f.write(modified_contents)
f.close()

cmd = 'cat '+ dasm_file +' | spike-dasm > ' + output_file
print(cmd)
os.system(cmd)




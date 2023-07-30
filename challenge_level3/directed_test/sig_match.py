'''
Doc:
matching the memory signatures script

    >>> python3 sig_match.py signature test_spike_signature.log         

'''
import sys
import os
import re

n = len(sys.argv)
print("Total Arguments Passed in The Script:", n)

if n==3 :
    rtl_signature_file=sys.argv[1]
    spike_signature_file=sys.argv[2]
elif n==2 :
    rtl_signature_file=sys.argv[1]
    spike_signature_file='test_spike_signature.log' 
else:
    rtl_signature_file = 'signature' 
    spike_signature_file = 'test_spike_signature.log' 
    


print("Input Signature Dump File:", rtl_signature_file)
print("Input Signature Dump File:", spike_signature_file)

f = open(rtl_signature_file, "r")
rtl_signature = f.read()
f.close()
f = open(spike_signature_file, "r")
spike_signature = f.read()
f.close()

spike_list = spike_signature.split("\n")
rtl_list=[]

x = rtl_signature.split("\n")
loop_size= len(x)//4
for i in range(0,loop_size):
	b=x[(i*4)+3]+x[(i*4)+2]+x[(i*4)+1]+x[i*4]
	rtl_list.append(b)
#print(rtl_list)
status=0
for i in range(len(rtl_list)):
    if rtl_list[i]==spike_list[i] :
        status|=0
        pass
    else :
        status|=1
        print("--------FAIL--------")
        print(' RTL Value = '+ rtl_list[i] + ' SPIKE Value = ' + spike_list[i])

if status==0:
    print("--------PASS--------")
else:
    print("--------FAIL--------")



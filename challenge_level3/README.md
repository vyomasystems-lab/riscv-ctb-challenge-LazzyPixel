# riscv_ctb_challenges
# Challenge_level3

For Challenge 3 Capture The Bug i have found 2 bugs in the buggy design.
To find out bugs i have followed few things
- To find the bugs I have used both Directed as well as Random tests.
- To make things easier i have created two scripts
    - dump_conv.py
        - converts RTL SPIKE or difference dump files into readable format
        - It take one input_file arguement and produce an output of readable_input_file
        - Name of output file is optional
    -  sig_match.py
         - It compares signature files of RTL and SPIKE dump.
         - It can take zero, one, two input_file arguement and produces result as PASS or FAIL.
         - for simplification, In case of zero argument it takes default signature files produced in this project.
## Captured Bugs
- ### Bug 1: 
    - OR instruction 
        - To reproduce the BUG or.S is present inside directed test directory.
        - Before running make, Open Makefile and replace test.S with or.S in the compile target section.
        - in the result of make is clearly visible that results of RTL and SPIKE are different.
        - for more analysis we can use spike.dump and rtl.dump with dump_conv.py
- ### Bug 2: 
    - ORI instruction
        - To reproduce the BUG ori.S is present inside directed test directory.
        - Before running make, Open Makefile and replace test.S with ori.S in the compile target section.
        - in the result of make is clearly visible that results of RTL and SPIKE are different.
        - for more analysis we can use spike.dump and rtl.dump with dump_conv.py
     
# Challenge_level3 Coverage





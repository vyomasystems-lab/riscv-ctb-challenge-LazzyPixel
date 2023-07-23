# challenge1_instructions

## Error:
After executing the "make" command, the compilation process failed.

    [UpTickPro] Test Compilation ------
    riscv32-unknown-elf-gcc -march=rv32i -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -    I/workspaces/riscv-ctb-challenge-LazzyPixel/challenge_level2/challenge1_instructions/work/common -T/workspaces/riscv-ctb-challenge-LazzyPixel/challenge_level2/challenge1_instructions/test.ld test.S /workspaces/riscv-ctb-challenge-LazzyPixel/challenge_level2/challenge1_instructions/work/common/crt.S -o test.elf
    test.S: Assembler messages:
    test.S:163: Error: unrecognized opcode `divuw s10,t6,t3'
    test.S:164: Error: unrecognized opcode `mulw t1,s10,s1'
    test.S:169: Error: unrecognized opcode `remuw t1,s3,s8'
    test.S:171: Error: unrecognized opcode `remuw t0,s7,s7'
    test.S:179: Error: unrecognized opcode `remuw t5,s4,s9'
    ..
    make: *** [Makefile:11: compile] Error 1


## Solution:
In the rv32i.yaml file there is a parameter named  `rel_rv64m`, which produces RV64 M-extension instruction( MUV & DIV instrucion).
The predefine value of `rel_rv64m` is  `10` by reducing it to zero we can fix the issue.

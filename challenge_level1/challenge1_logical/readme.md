
# Challenge1_logical 

The test.S had two syntex issue following at line 15855, 25584.

    riscv32-unknown-elf-gcc -march=rv32i -mabi=ilp32 -static -mcmodel=medany -fvisibility=hidden -nostdlib -nostartfiles -I/workspaces/riscv-ctb-challenge-LazzyPixel/challenge_level1/challenge1_logical/common -T/workspaces/riscv-ctb-challenge-LazzyPixel/challenge_level1/challenge1_logical/common/link.ld test.S -o test.elf
    test.S: Assembler messages:
    test.S:15855: Error: illegal operands `and s7,ra,z4'
    test.S:25584: Error: illegal operands `andi s5,t1,s0'
    make: *** [Makefile:4: compile] Error 1
## Syntex issue 1: 
Line 15855 contains the "add" instruction: `and s7, ra, z4`. Upon careful examination, it becomes evident that the third operand, `z4` is invalid. 
### Solution: 
- To address this problem, I replaced `z4` with `a4`.

## Syntex issue 2: 
Line 25584 contains the instruction: `andi s5, t1, s0`. Upon careful observation, it becomes apparent that the second operand is a register, which is not allowed for an I-type (immediate) instruction.
### Solution: 
To address this problem, We have two potential solutions :
- Replace `andi` with an appropriate R-type instruction.
- Replace the second argument with an immediate value (a 12-bit value).
To resolve this issue, I opted for the first approach, where I replaced the andi with and instruction.
# Challenge2_Exceptions

## AIM : 
Create a AAPG config file to generate a test with 10 illegal exceptions with the correct handler code.

## Solution:
  Below are the steps to produce the 10 illegal exception with the AAPG config file.
  - First copied `rv32i.yaml` from `challenge_level2/challenge1_instructions`
  - To produce excption in the test we have `exception-generation` in the YAML file.
  - exception code for illegal exception is 2 (from Privledge Spec. MCAUSE Table)
  - Now to target 10 illegal exception we have set  `ecause02: 9`.
## Error Found:
- During the "make" process, it has been noticed that the test sometimes passes with ten exceptions, while other times it gets stuck. After examining the trace file, it was discovered that the test becomes stuck on the same instruction exception, same as the level1 illegal instruction challenge, because it keeps jumping to the same MEPC (Machine Exception Program Counter).
- Additional Point trap_handler has a way of configuring MEPC for 16/32 bit instruction.
- After looking more throughly It is found that the illegal instruction that are in infinite loop is 16 bit instuctions(From Spec INSTR[1:0] != 3). According to RV32I implementations that support only IALIGN=32, the lower two bits of mepc[1:0] are always zero, that way adding 2 (In case of 16-bit instr.) doesnt make any change in MEPC.
## Remedie: 
To resolve this problem and avoid the test from getting stuck in an endless loop of handling the same exception repeatedly, we need to constraint the exception instruction generation. By making this adjustment, we can ensure proper termination control and prevent the test from being trapped in an infinite loop.
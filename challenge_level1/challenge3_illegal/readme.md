# Challenge3_illegal 

After executing the "make" command, the compilation process became stuck, and upon analyzing the spike dump, it became evident that the program was trapped in an infinite loop.

## Observations:
- The purpose of the "test.S" file is to perform an illegal instruction trap handling test.
- Within the "test.S" file, the "mtvec_handler" is implemented to handle the illegal instruction trap.
- Upon reviewing the spike dump, it was observed that the trap handler always returned to the same Program Counter (PC) value, which corresponds to the illegal instruction PC, after resolving the trap.
- As a result, the program was caught in an infinite loop of handling the illegal instruction.

## Solution:
To resolve this issue, certain modifications were implemented, specifically concerning the "MEPC" (Machine Exception Program Counter) in the "mtvec_handler." The goal was to ensure that after executing the "mret" instruction, the PC would jump to the next instruction (or "exception_PC + 4").

In the "test.S" file, the next instruction after the illegal instruction is a "j fail," which would lead to test failure. However, to achieve successful illegal instruction handling, instead of jumping to the next instruction, the PC should jump to "TEST_PASSFAIL," which will be "MEPC + 8."

The following instructions were added to achieve this behavior:

```
csrr t0, mepc        # Read the value of MEPC
add t0, t0, 8        # Add the destination gap after the mret
csrw mepc, t0        # Update the MEPC with the new value
```

By making these adjustments, proper termination control was ensured in the program.
.data
newline: .asciiz "\n"
calc: .word 0
val1: .word 3
val2: .word 6
val3: .word 2

.text
.globl main

main:

    lw $t0, val1

    lw $t1, val2

L1:

    blt $t1, $t0, while_end_L2

    li $v0, 1
    move $a0, $t0
    syscall

    li $v0, 4
    la $a0, newline
    syscall
    lw $t2, val3

    add $t0, $t0, $t2

    j L1

while_end_L2:

    li $v0, 10
    syscall
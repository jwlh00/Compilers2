.data
newline: .asciiz "\n"
calc: .word 0
val1: .word 3
val2: .word 6
val3: .word 2
result: .word 0

.text
.globl main

main:

    lw $a0, val1

    lw $a1, val2

    jal equation
    move $t0, $v0

    blt $a0, $a1, if_part_L1
    li $v0, 1
    move $a0, $a1
    syscall
    li $v0, 4
    la $a0, newline
    syscall

    j L2

if_part_L1:
    li $v0, 1
    move $a0, $a0
    syscall
    li $v0, 4
    la $a0, newline
    syscall

    j L2

L2:

    li $v0, 10
    syscall

equation:

    add $v0, $a0, $a1
    sw $t0, result

    jr $ra


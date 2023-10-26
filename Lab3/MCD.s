.data
prompt1: .asciiz "Enter the first number: "
prompt2: .asciiz "Enter the second number: "

.text
.globl main
main:
    # Prompt and read the first number
    li $v0, 4          # syscall for print_string
    la $a0, prompt1
    syscall
    li $v0, 5          # syscall for read_int
    syscall
    move $s0, $v0      # store the read integer in $s0

    # Prompt and read the second number
    li $v0, 4
    la $a0, prompt2
    syscall
    li $v0, 5
    syscall
    move $s1, $v0      # store the read integer in $s1

    # Move values to argument registers and call the GCD function
    move $a0, $s0
    move $a1, $s1
    jal GCD

    # Print the result
    move $a0, $v0
    li $v0, 1          # syscall for print_int
    syscall

    # Exit
    li $v0, 10         # syscall for exit
    syscall

GCD:
    # Check if $a1 (n2) is zero
    beq $a1, $zero, returnn0  # if $a1 is zero, the GCD is $a0 (n1)

    # Save context
    addi $sp, $sp, -12
    sw $ra, 0($sp)    # save return address

    # Recursive call preparation
    rem $t0, $a0, $a1 # $t0 = $a0 mod $a1
    move $a0, $a1     # make $a0 = $a1
    move $a1, $t0     # make $a1 = $t0 (remainder)

    # Recursive call
    jal GCD

    # Restore context and return
    lw $ra, 0($sp)
    addi $sp, $sp, 12
    jr $ra

returnn0:
    move $v0, $a0     # return $v0 = $a0
    j exitGCD

exitGCD:
    jr $ra

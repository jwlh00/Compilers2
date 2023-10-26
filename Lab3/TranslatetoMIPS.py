def generate_mips_from_tac_final(tac_instructions):
    # Segregate .data and .text sections
    data_section = ".data\n"
    text_section = ".text\nmain:\n"

    # Dictionary to hold mapping between TAC variables and MIPS registers
    register_map = {}
    next_register = 0

    # Dictionary to keep track of declared variables to avoid duplicates
    declared_vars = set()

    # Helper function to get or assign a register
    def get_or_assign_register(var):
        nonlocal next_register
        if var not in register_map:
            register_map[var] = f"$t{next_register}"
            next_register += 1
        return register_map[var]

    for instruction in tac_instructions:
        operation, operand1, operator, operand2 = instruction

        # Handling class declaration
        if operation == "class":
            data_section += f"\n# Beginning of class {operand1}\n"

        # Handling parameter and variable declarations
        elif operation in ["param", "declare"]:
            if operand1 not in declared_vars:
                # If the operand is numeric, use it directly. Otherwise, initialize to 0.
                init_value = operand1 if operand1.isdigit() else "0"
                data_section += f"{operand1}:      .word {init_value}\n"
                declared_vars.add(operand1)

        # Handling method calls
        elif operation == "call":
            text_section += f"    jal  {operand1}\n"

        # Generating MIPS code based on TAC operators
        else:
            if operator == "+":
                text_section += f"    add  {get_or_assign_register(operation)}, {get_or_assign_register(operand1)}, {get_or_assign_register(operand2)}\n"
            elif operator == "/":
                text_section += f"    div  {get_or_assign_register(operand1)}, {operand2}\n"
                text_section += f"    mflo {get_or_assign_register(operation)}\n"
            elif operator == "":
                text_section += f"    move {get_or_assign_register(operation)}, {get_or_assign_register(operand1)}\n"

    return data_section + "\n" + text_section


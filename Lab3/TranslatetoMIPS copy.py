def tac_to_mips_qtspim_complete(tac):
    data_segment = ['.data']
    text_segment = ['.text']
    
    var_address = {}
    temp_register_map = {}
    string_literals = {}
    
    param_regs = ['$a0', '$a1', '$a2', '$a3']
    temp_regs = ['$t' + str(i) for i in range(10)]
    current_temp_reg_index = 0
    
    def handle_string_literal(s):
        if s not in string_literals:
            label = f'str_{len(string_literals)}'
            string_literals[s] = label
            data_segment.append(f"{label}: .asciiz \"{s}\"")
        return string_literals[s]
    
    def get_temp_register():
        nonlocal current_temp_reg_index
        reg = temp_regs[current_temp_reg_index]
        current_temp_reg_index = (current_temp_reg_index + 1) % len(temp_regs)
        return reg
    
    param_count = 0
    for code in tac:
        op, arg1, arg2, result = code
        
        if op == 'declare':
            var_address[arg1] = arg1
            data_segment.append(f"{arg1}: .word 0")
        
        elif op == 'param':
            if param_count < 4:
                reg = param_regs[param_count]
                text_segment.append(f"lw {reg}, {arg1}")
            else:
                # Push extra parameters to the stack
                text_segment.append(f"sub $sp, $sp, 4")
                text_segment.append(f"sw {arg1}, 0($sp)")
            param_count += 1
        
        elif op == '+':
            reg = get_temp_register()
            temp_register_map[result] = reg
            text_segment.append(f"lw $t0, {arg1}")
            text_segment.append(f"lw $t1, {arg2}")
            text_segment.append(f"add {reg}, $t0, $t1")
            text_segment.append(f"sw {reg}, {result}")
        
        elif op == '/':
            reg = get_temp_register()
            temp_register_map[result] = reg
            text_segment.append(f"lw $t0, {arg1}")
            text_segment.append(f"lw $t1, {arg2}")
            text_segment.append(f"div $t0, $t1")
            text_segment.append(f"mflo {reg}")
            text_segment.append(f"sw {reg}, {result}")
        
        elif result and not arg2:
            if arg1 in temp_register_map:
                text_segment.append(f"sw {temp_register_map[arg1]}, {result}")
            else:
                text_segment.append(f"lw $t0, {arg1}")
                text_segment.append(f"sw $t0, {result}")
        
        elif op == 'call':
            if arg1 == 'out_string':
                if arg2.startswith('The'):
                    label = handle_string_literal(arg2)
                    text_segment.append(f"la $a0, {label}")
                else:
                    text_segment.append(f"lw $a0, {arg2}")
                text_segment.append(f"li $v0, 4")
                text_segment.append(f"syscall")
            
            elif arg1 == 'out_int':
                text_segment.append(f"lw $a0, {arg2}")
                text_segment.append(f"li $v0, 1")
                text_segment.append(f"syscall")
            
            else:
                text_segment.append(f"# Placeholder for {arg1} method call")
        
        # Reset param count after a call
        if op == 'call':
            param_count = 0
    
    mips_code = '\n'.join(data_segment + text_segment)
    return mips_code
import re

class TranslatetoMIPSFunc:
    def __init__(self, cuadruplas):

        self.cuadruplas_iniciales = cuadruplas
        self.data_section = ".data\nnewline: .asciiz \"\\n\"\n"
        self.text_section = "\n.text\n.globl main\n"
        self.variables = set()
        self.methods = []
        self.stack = []
        self.variables_cargadas = {}
        self.argumentos = {}
        self.resultados = {}
        self.temp_counter = 0
        self.a_counter = 0
        self.v_counter = 0
        self.indentation = 0

        self.cuadruplas_procesadas = set()

        self.parametros_metodos = {}

        self.estructura_return = {}

        self.recorrer_cuadruplas(self.cuadruplas_iniciales)

        if self.methods[-1] == 'main':
            self.text_section += f"\n{'    ' * self.indentation}li $v0, 10\n{'    ' * self.indentation}syscall\n"


    # def get_temp(self):
    #     temp = f"t{self.temp_counter}"
    #     self.temp_counter += 1
    #     return temp

    # def get_temp(self):
    #     # Using a different naming convention for temporary registers
    #     temp = f"$temp{self.temp_counter}"
    #     self.temp_counter += 1
    #     return temp

    def get_temp(self):
        # Using a correct naming convention for temporary registers
        temp = f"$t{self.temp_counter}"  # Single $ sign and using 't' for temporary registers
        self.temp_counter += 1
        return temp

    
    def get_a(self):
        a = f"a{self.a_counter}"
        self.a_counter += 1
        return a
    
    def get_v(self):
        v = f"v{self.v_counter}"
        self.v_counter += 1
        return v
    
    def recorrer_cuadruplas(self,cuadruplas_actuales, cuadrupla_exit_label = None):

        for indice, quadruple in enumerate(cuadruplas_actuales):
            self.generar_codigo_mips(quadruple) 

    def generar_codigo_mips(self, cuadrupla_actual):


        if cuadrupla_actual in self.cuadruplas_procesadas:
            return
        
        self.cuadruplas_procesadas.add(cuadrupla_actual)


        if cuadrupla_actual.op == '<-':
            self.mips_asignacion(cuadrupla_actual)
        

        if cuadrupla_actual.op == 'CreateMethod':
            self.mips_metodos(cuadrupla_actual)
    

        if cuadrupla_actual.op in ['+', '-', '*', '/']:
            self.mips_aritmetica(cuadrupla_actual)


        if cuadrupla_actual.op == 'PROCEDURE':
            self.mips_procedure(cuadrupla_actual)
        

        if cuadrupla_actual.op == 'IfHandler':
            self.mips_ifs(cuadrupla_actual)
        

        if cuadrupla_actual.op == 'GotoHandler':
            self.mips_jump(cuadrupla_actual)


        if cuadrupla_actual.op == 'WhileHandler':
            self.mips_while(cuadrupla_actual)


        if cuadrupla_actual.op == 'PrepareParam':
            self.mips_pre_param(cuadrupla_actual)  


        if cuadrupla_actual.op == 'MethodHandler':
            self.mips_method_call(cuadrupla_actual) 


        if cuadrupla_actual.op == 'ReturnHandler':
            self.mips_return(cuadrupla_actual)

        self.cleanup_mips_code()
        self.correct_register_syntax()
               
                
    def mips_jump(self, quadruple):
        self.text_section += f"\n{'    ' * self.indentation}j {quadruple.result}\n"

    def mips_pre_param(self, quadruple):

        address_temporal = self.get_a()

        self.text_section += f"\n{'    ' * self.indentation}lw ${address_temporal}, {quadruple.arg1}\n"

        self.variables_cargadas[quadruple.arg1] = address_temporal

        if quadruple.result not in self.parametros_metodos:

            self.parametros_metodos[quadruple.result] = [(quadruple.arg1, address_temporal)]

        else:

            self.parametros_metodos[quadruple.result].append((quadruple.arg1, address_temporal))
        
    def mips_method_call(self, quadruple):

        self.text_section += f"\n{'    ' * self.indentation}jal {quadruple.arg1}\n"

    def mips_return(self, quadruple):

        self.text_section += f"\n{'    ' * self.indentation}jr $ra\n"


    def mips_while(self, quadruple):

        cuadrupla_siguiente = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(quadruple) + 1]
        cuadrupla_comparacion = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_siguiente) + 1]
        instruccion_comparacion = ""
        cuadrupla_jump_if_false = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_comparacion) + 1]

        match cuadrupla_comparacion.op:

            case '<':
                instruccion_comparacion = "blt"
            case '>':
                instruccion_comparacion = "bgt"
            case '<=':
                instruccion_comparacion = "ble"
            case '>=':
                instruccion_comparacion = "bge"
            case '==':
                instruccion_comparacion = "beq"
            case '!=':
                instruccion_comparacion = "bne"
        
        arg1 = ""


        if cuadrupla_comparacion.arg1 not in self.variables:
            self.text_section += f"\n{'    ' * self.indentation}li $t{self.temp_counter}, {cuadrupla_comparacion.arg1}\n"
            self.variables_cargadas[cuadrupla_comparacion.arg1] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg1 = self.variables_cargadas[cuadrupla_comparacion.arg1]

        elif cuadrupla_comparacion.arg1 in self.variables_cargadas:
            arg1 = self.variables_cargadas[cuadrupla_comparacion.arg1]
        else:

            self.text_section += f"\n{'    ' * self.indentation}lw $t{self.temp_counter}, {cuadrupla_comparacion.arg1}\n"
            self.variables_cargadas[cuadrupla_comparacion.arg1] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg1 = self.variables_cargadas[cuadrupla_comparacion.arg1]
        
        arg2 = ""

        if cuadrupla_comparacion.arg2 not in self.variables:
            self.text_section += f"\n{'    ' * self.indentation}li $t{self.temp_counter}, {cuadrupla_comparacion.arg2}\n"
            self.variables_cargadas[cuadrupla_comparacion.arg2] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg2 = self.variables_cargadas[cuadrupla_comparacion.arg2]
        elif cuadrupla_comparacion.arg2 in self.variables_cargadas:
            arg2 = self.variables_cargadas[cuadrupla_comparacion.arg2]
        else:
            self.text_section += f"\n{'    ' * self.indentation}lw $t{self.temp_counter}, {cuadrupla_comparacion.arg2}\n"
            self.variables_cargadas[cuadrupla_comparacion.arg2] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg2 = self.variables_cargadas[cuadrupla_comparacion.arg2]

        self.text_section += f"\n{cuadrupla_siguiente.result}:\n"

        cuadrupla_end_while = None

        for quadruple in self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_comparacion):]:
            if quadruple.op == 'LabelFinish':
                cuadrupla_end_while = quadruple
                break
        
        etiqueta_salto_end_while = "while_end_" + cuadrupla_end_while.result # while_end_L1

        self.text_section += f"\n{'    ' * self.indentation}{instruccion_comparacion} ${arg2}, ${arg1}, {etiqueta_salto_end_while}\n"

        lista_cuadruplas_in_between = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_jump_if_false) + 1: self.cuadruplas_iniciales.index(cuadrupla_end_while)]

        self.recorrer_cuadruplas(lista_cuadruplas_in_between)

        self.text_section += f"\nwhile_end_{cuadrupla_end_while.result}:\n"


    def mips_ifs(self, quadruple):
        indice_cuadrupla_actual = self.cuadruplas_iniciales.index(quadruple)
        cuadrupla_siguiente = self.cuadruplas_iniciales[indice_cuadrupla_actual + 1]
        # print(f"Handling IF: quadruple actual {quadruple}, quadruple siguiente {cuadrupla_siguiente}")
        instruccion_comparacion = ""

        match cuadrupla_siguiente.op:

            case '<':
                instruccion_comparacion = "blt"
            case '>':
                instruccion_comparacion = "bgt"
            case '<=':
                instruccion_comparacion = "ble"
            case '>=':
                instruccion_comparacion = "bge"
            case '==':
                instruccion_comparacion = "beq"
            case '!=':
                instruccion_comparacion = "bne"
        

        arg1 = ""

        if cuadrupla_siguiente.arg1 not in self.variables:
            self.text_section += f"\n{'    ' * self.indentation}li $t{self.temp_counter}, {cuadrupla_siguiente.arg1}\n"
            self.variables_cargadas[cuadrupla_siguiente.arg1] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg1 = self.variables_cargadas[cuadrupla_siguiente.arg1]
        
        elif cuadrupla_siguiente.arg1 in self.variables_cargadas:
            arg1 = self.variables_cargadas[cuadrupla_siguiente.arg1]
        else:
            self.text_section += f"\n{'    ' * self.indentation}lw $t{self.temp_counter}, {cuadrupla_siguiente.arg1}\n"
            self.variables_cargadas[cuadrupla_siguiente.arg1] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg1 = self.variables_cargadas[cuadrupla_siguiente.arg1]
        
        arg2 = ""

        if cuadrupla_siguiente.arg2 not in self.variables:
            self.text_section += f"\n{'    ' * self.indentation}li $t{self.temp_counter}, {cuadrupla_siguiente.arg2}\n"
            self.variables_cargadas[cuadrupla_siguiente.arg2] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg2 = self.variables_cargadas[cuadrupla_siguiente.arg2]
        
        elif cuadrupla_siguiente.arg2 in self.variables_cargadas:
            arg2 = self.variables_cargadas[cuadrupla_siguiente.arg2]
        else:
            self.text_section += f"\n{'    ' * self.indentation}lw $t{self.temp_counter}, {cuadrupla_siguiente.arg2}\n"
            self.variables_cargadas[cuadrupla_siguiente.arg2] = f"t{self.temp_counter}"
            self.temp_counter += 1
            arg2 = self.variables_cargadas[cuadrupla_siguiente.arg2]

        # print(f"Comparing {arg1} and {arg2} with operation {instruccion_comparacion}")
        cuadrupla_jump_if_false = self.cuadruplas_iniciales[indice_cuadrupla_actual + 2]

        etiqueta_salto = "if_part_" + cuadrupla_jump_if_false.result # if_part_L1

        self.text_section += f"\n{'    ' * self.indentation}{instruccion_comparacion} ${arg1}, ${arg2}, {etiqueta_salto}\n"


        cuadrupla_exit_label = None


        for quadruple in self.cuadruplas_iniciales[indice_cuadrupla_actual:]:
            if quadruple.op == 'LabelFinish':
                cuadrupla_exit_label = quadruple
                break

        Cuadrupla_LABEL = None
        cuadrupla_EXIT_LABEL = None

        etiqueta_salto_final = "else_part_" + cuadrupla_jump_if_false.result

        for cuadrupla_iteradora in self.cuadruplas_iniciales[indice_cuadrupla_actual:]:

            if cuadrupla_iteradora.op == "LabelHandler":
                Cuadrupla_LABEL = cuadrupla_iteradora
                break
        
        for cuadrupla_iteradora in self.cuadruplas_iniciales[indice_cuadrupla_actual:]:

            if cuadrupla_iteradora.op == "LabelFinish":
                cuadrupla_EXIT_LABEL = cuadrupla_iteradora
                break


        # print(f"Label Finish: {cuadrupla_EXIT_LABEL}, Label Handler: {Cuadrupla_LABEL}")
       



        lista_cuadruplas_in_between = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(Cuadrupla_LABEL) + 1: self.cuadruplas_iniciales.index(cuadrupla_EXIT_LABEL)]

        self.recorrer_cuadruplas(lista_cuadruplas_in_between)
        self.text_section += f"\n{etiqueta_salto}:\n"

        lista_cuadruplas_in_between = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_jump_if_false) + 1: self.cuadruplas_iniciales.index(Cuadrupla_LABEL)]

        self.recorrer_cuadruplas(lista_cuadruplas_in_between)

        self.text_section += f"\n{cuadrupla_EXIT_LABEL.result}:\n"

        # print(f"Completed IF handling for quadruple {quadruple}")

    

    def mips_aritmetica(self, quadruple):
        lista_parametros = []
        nombre_metodo = ""
        for cuadrupla_iteradora in reversed(self.cuadruplas_iniciales[:self.cuadruplas_iniciales.index(quadruple)]):
            if cuadrupla_iteradora.op == 'Param':
                if cuadrupla_iteradora.arg1 == quadruple.arg1 or cuadrupla_iteradora.arg1 == quadruple.arg2:
                    if cuadrupla_iteradora.result in self.parametros_metodos:
                        nombre_metodo = cuadrupla_iteradora.result
                        lista_parametros.append(self.parametros_metodos[cuadrupla_iteradora.result].pop(0))

            if cuadrupla_iteradora.op == 'CreateMethod':
                break

        if lista_parametros:
            valor_retorno = "v0"
            self.estructura_return[nombre_metodo] = valor_retorno
            if quadruple.op == "+":
                self.text_section += f"\n{'    ' * self.indentation}add ${valor_retorno}, ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"
                return 
       
            elif quadruple.op == "-":
                self.text_section += f"\n{'    ' * self.indentation}sub ${valor_retorno}, ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"
                return
            
            elif quadruple.op == "*":
                self.text_section += f"\n{'    ' * self.indentation}mul ${valor_retorno}, ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"
                return
            
            elif quadruple.op == "/":
                self.text_section += f"\n{'    ' * self.indentation}div ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"
                self.text_section += f"{'    ' * self.indentation}mflo ${valor_retorno}\n"
                temp4 = self.get_temp()
                self.text_section += f"{'    ' * self.indentation}mfhi ${temp4}\n"
                self.temp_counter -= 1
                return


        cuadrupla_siguiente = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(quadruple) + 1]
        if quadruple.arg1 not in self.variables:
            temp1 = self.get_temp()
            self.text_section += f"\n{'    ' * self.indentation}li ${temp1}, {quadruple.arg1}\n"
            self.variables_cargadas[quadruple.arg1] = temp1

        if quadruple.arg2 not in self.variables:
            temp2 = self.get_temp()
            self.text_section += f"{'    ' * self.indentation}li ${temp2}, {quadruple.arg2}\n"
            self.variables_cargadas[quadruple.arg2] = temp2

        if quadruple.arg1 not in self.variables_cargadas:
            temp1 = self.get_temp()
            self.text_section += f"\n{'    ' * self.indentation}lw ${temp1}, {quadruple.arg1}\n"
            self.variables_cargadas[quadruple.arg1] = temp1
            
        if quadruple.arg2 not in self.variables_cargadas:
            temp2 = self.get_temp()
            self.text_section += f"{'    ' * self.indentation}lw ${temp2}, {quadruple.arg2}\n"
            self.variables_cargadas[quadruple.arg2] = temp2

        if quadruple.arg1 == cuadrupla_siguiente.result or quadruple.arg2 == cuadrupla_siguiente.result:
            if quadruple.op == '+':
                self.text_section += f"\n{'    ' * self.indentation}add ${self.variables_cargadas[cuadrupla_siguiente.result]}, ${self.variables_cargadas[quadruple.arg1]}, ${self.variables_cargadas[quadruple.arg2]}\n"
                self.cuadruplas_procesadas.add(cuadrupla_siguiente)
                return
            elif quadruple.op == '-':
                self.text_section += f"\n{'    ' * self.indentation}sub ${self.variables_cargadas[cuadrupla_siguiente.result]}, ${self.variables_cargadas[quadruple.arg1]}, ${self.variables_cargadas[quadruple.arg2]}\n"
                self.cuadruplas_procesadas.add(cuadrupla_siguiente)
                return

        temp3 = self.get_temp()

        if quadruple.op == '+':
            self.text_section += f"\n{'    ' * self.indentation}add ${temp3}, ${self.variables_cargadas[quadruple.arg1]}, ${self.variables_cargadas[quadruple.arg2]}\n"
        elif quadruple.op == '-':
            self.text_section += f"\n{'    ' * self.indentation}sub ${temp3}, ${self.variables_cargadas[quadruple.arg1]}, ${self.variables_cargadas[quadruple.arg2]}\n"
        elif quadruple.op == '*':
            self.text_section += f"\n{'    ' * self.indentation}mul ${temp3}, ${self.variables_cargadas[quadruple.arg1]}, ${self.variables_cargadas[quadruple.arg2]}\n"
        elif quadruple.op == '/':
            self.text_section += f"\n{'    ' * self.indentation}div ${self.variables_cargadas[quadruple.arg1]}, ${self.variables_cargadas[quadruple.arg2]}\n"
            self.text_section += f"{'    ' * self.indentation}mflo ${temp3}\n"
            temp4 = self.get_temp()
            self.text_section += f"{'    ' * self.indentation}mfhi ${temp4}\n"
            self.temp_counter -= 1

    # def mips_aritmetica(self, quadruple):
    #     # Simplifying arithmetic operations
    #     temp1 = self.variables_cargadas.get(quadruple.arg1, quadruple.arg1)
    #     temp2 = self.variables_cargadas.get(quadruple.arg2, quadruple.arg2)

    #     result_reg = self.get_temp()
    #     if quadruple.op == '+':
    #         self.text_section += f"{self.indent('')}add {result_reg}, {temp1}, {temp2}\n"
    #     elif quadruple.op == '-':
    #         self.text_section += f"{self.indent('')}sub {result_reg}, {temp1}, {temp2}\n"
    #     elif quadruple.op == '*':
    #         self.text_section += f"{self.indent('')}mul {result_reg}, {temp1}, {temp2}\n"
    #     elif quadruple.op == '/':
    #         self.text_section += f"{self.indent('')}div {temp1}, {temp2}\n{self.indent('')}mflo {result_reg}\n"

    #     # Store the result in a variable if needed
    #     if quadruple.result:
    #         self.text_section += f"{self.indent('')}sw {result_reg}, {quadruple.result}\n"


    def mips_metodos(self, quadruple):
        
        self.indentation = 0
        if len(self.methods) >= 1 and quadruple.arg1 not in self.methods and self.methods[-1] == 'main':
            self.text_section += f"\n{'    '}li $v0, 10\n{'    '}syscall\n"

        self.text_section += f"\n{quadruple.arg1}:\n"
        self.methods.append(quadruple.arg1)
        self.indentation += 1

    def mips_asignacion(self, quadruple):

        if quadruple.result not in self.variables:
            if quadruple.arg2 == 'String':
                self.data_section += f"{quadruple.result}: .asciiz {quadruple.arg1}\n"
                self.variables.add(quadruple.result)
            elif quadruple.arg2 == 'Int':
                self.data_section += f"{quadruple.result}: .word {quadruple.arg1}\n"
                self.variables.add(quadruple.result) 
            elif quadruple.arg2 == 'Bool':
                self.data_section += f"{quadruple.result}: .word {1 if quadruple.arg1 == 'true' else 0}\n"
                self.variables.add(quadruple.result)
        else:
            operador_temporal = quadruple.arg1

            for cuadrupla_iteradora in reversed(self.cuadruplas_iniciales[:self.cuadruplas_iniciales.index(quadruple)]):

                if cuadrupla_iteradora.op == 'CreateMethod':

                    break

                if cuadrupla_iteradora.result == operador_temporal and cuadrupla_iteradora.op == 'MethodHandler':
                    nuevo_temporal = self.get_temp()
                    self.text_section += f"{'    ' * self.indentation}move ${nuevo_temporal}, $v0\n"
                    self.variables_cargadas[quadruple.result] = nuevo_temporal
                    return

            self.text_section += f"{'    ' * self.indentation}sw $t{self.temp_counter-1}, {quadruple.result}\n"
            self.variables_cargadas[quadruple.result] = f"t{self.temp_counter-1}"
    
    # def mips_procedure(self, quadruple):
    #     if quadruple.arg2 in self.variables_cargadas:
    #         if quadruple.arg1 == 'out_int':
    #                     self.text_section += f"\n{'    ' * self.indentation}li $v0, 1\n"
    #                     self.text_section += f"{'    ' * self.indentation}move $a0, ${self.variables_cargadas[quadruple.arg2]}\n"
    #                     self.text_section += f"{'    ' * self.indentation}syscall\n"
    #         elif quadruple.arg1 == 'out_string':
    #             self.text_section += f"\n{'    ' * self.indentation}li $v0, 4\n"
    #             self.text_section += f"{'    ' * self.indentation}move $a0, ${self.variables_cargadas[quadruple.arg2]}\n"
    #             self.text_section += f"{'    ' * self.indentation}syscall\n"
    #     else:
    #         if quadruple.arg1 == 'out_int':
    #                     self.text_section += f"\n{'    ' * self.indentation}li $v0, 1\n"
    #                     self.text_section += f"{'    ' * self.indentation}move $a0, ${quadruple.arg2}\n"
    #                     self.text_section += f"{'    ' * self.indentation}syscall\n"
    #         elif quadruple.arg1 == 'out_string':
    #             self.text_section += f"\n{'    ' * self.indentation}li $v0, 4\n"
    #             self.text_section += f"{'    ' * self.indentation}move $a0, ${quadruple.arg2}\n"
    #             self.text_section += f"{'    ' * self.indentation}syscall\n"
    #     self.text_section += f"\n{'    ' * self.indentation}li $v0, 4\n"
    #     self.text_section += f"{'    ' * self.indentation}la $a0, newline\n"
    #     self.text_section += f"{'    ' * self.indentation}syscall\n"

    def mips_procedure(self, quadruple):
        # Dynamically determine the syscall based on procedure type
        if quadruple.arg1 == 'out_int':
            syscall_code = '1'  # Print integer
            arg = self.variables_cargadas.get(quadruple.arg2, f"${quadruple.arg2}")
            self.text_section += f"{self.indent('')}li $v0, {syscall_code}\n"
            self.text_section += f"{self.indent('')}move $a0, {arg}\n"
        elif quadruple.arg1 == 'out_string':
            syscall_code = '4'  # Print string
            arg = self.variables_cargadas.get(quadruple.arg2, f"${quadruple.arg2}")
            self.text_section += f"{self.indent('')}li $v0, {syscall_code}\n"
            self.text_section += f"{self.indent('')}la $a0, {arg}\n"
        # Execute syscall and print newline
        self.text_section += f"{self.indent('')}syscall\n"
        self.text_section += f"{self.indent('')}li $v0, 4\n"
        self.text_section += f"{self.indent('')}la $a0, newline\n"
        self.text_section += f"{self.indent('')}syscall\n"

    def cleanup_mips_code(self):
        self.text_section = self.text_section.replace('$$', '$')
        self.data_section = self.data_section.replace('$$', '$')

    def indent(self, code):
        return '    ' * self.indentation + code

    def correct_register_syntax(self):
        patternA = r'(?<!\$)(a\d+)'
        patternT = r'(?<!\$)(t\d+)'

        self.text_section = re.sub(patternA, r'$\1', self.text_section)
        self.data_section = re.sub(patternA, r'$\1', self.data_section)

        self.text_section = re.sub(patternT, r'$\1', self.text_section)
        self.data_section = re.sub(patternT, r'$\1', self.data_section)
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


    def get_temp(self):
        temp = f"t{self.temp_counter}"
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

        for indice, cuadrupla in enumerate(cuadruplas_actuales):
            self.generar_codigo_mips(cuadrupla) 

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
               
                
    def mips_jump(self, cuadrupla):
        self.text_section += f"\n{'    ' * self.indentation}j {cuadrupla.result}\n"

    def mips_pre_param(self, cuadrupla):

        address_temporal = self.get_a()

        self.text_section += f"\n{'    ' * self.indentation}lw ${address_temporal}, {cuadrupla.arg1}\n"

        self.variables_cargadas[cuadrupla.arg1] = address_temporal

        if cuadrupla.result not in self.parametros_metodos:

            self.parametros_metodos[cuadrupla.result] = [(cuadrupla.arg1, address_temporal)]

        else:

            self.parametros_metodos[cuadrupla.result].append((cuadrupla.arg1, address_temporal))
        
    def mips_method_call(self, cuadrupla):

        self.text_section += f"\n{'    ' * self.indentation}jal {cuadrupla.arg1}\n"

    def mips_return(self, cuadrupla):

        self.text_section += f"\n{'    ' * self.indentation}jr $ra\n"


    def mips_while(self, cuadrupla):

        cuadrupla_siguiente = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla) + 1]
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

        for cuadrupla in self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_comparacion):]:
            if cuadrupla.op == 'LabelFinish':
                cuadrupla_end_while = cuadrupla
                break
        
        etiqueta_salto_end_while = "while_end_" + cuadrupla_end_while.result # while_end_L1

        self.text_section += f"\n{'    ' * self.indentation}{instruccion_comparacion} ${arg2}, ${arg1}, {etiqueta_salto_end_while}\n"

        lista_cuadruplas_in_between = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla_jump_if_false) + 1: self.cuadruplas_iniciales.index(cuadrupla_end_while)]

        self.recorrer_cuadruplas(lista_cuadruplas_in_between)

        self.text_section += f"\nwhile_end_{cuadrupla_end_while.result}:\n"


    def mips_ifs(self, cuadrupla):
        indice_cuadrupla_actual = self.cuadruplas_iniciales.index(cuadrupla)
        cuadrupla_siguiente = self.cuadruplas_iniciales[indice_cuadrupla_actual + 1]
        print(f"Handling IF: cuadrupla actual {cuadrupla}, cuadrupla siguiente {cuadrupla_siguiente}")
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

        print(f"Comparing {arg1} and {arg2} with operation {instruccion_comparacion}")
        cuadrupla_jump_if_false = self.cuadruplas_iniciales[indice_cuadrupla_actual + 2]

        etiqueta_salto = "if_part_" + cuadrupla_jump_if_false.result # if_part_L1

        self.text_section += f"\n{'    ' * self.indentation}{instruccion_comparacion} ${arg1}, ${arg2}, {etiqueta_salto}\n"


        cuadrupla_exit_label = None


        for cuadrupla in self.cuadruplas_iniciales[indice_cuadrupla_actual:]:
            if cuadrupla.op == 'LabelFinish':
                cuadrupla_exit_label = cuadrupla
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

        # print(f"Completed IF handling for cuadrupla {cuadrupla}")


    def mips_aritmetica(self, cuadrupla):

        lista_parametros = []

        nombre_metodo = ""

        for cuadrupla_iteradora in reversed(self.cuadruplas_iniciales[:self.cuadruplas_iniciales.index(cuadrupla)]):

            if cuadrupla_iteradora.op == 'Param':

                if cuadrupla_iteradora.arg1 == cuadrupla.arg1 or cuadrupla_iteradora.arg1 == cuadrupla.arg2:
                    if cuadrupla_iteradora.result in self.parametros_metodos:

                        nombre_metodo = cuadrupla_iteradora.result

                        lista_parametros.append(self.parametros_metodos[cuadrupla_iteradora.result].pop(0))

            if cuadrupla_iteradora.op == 'CreateMethod':

                break


        if lista_parametros:

            valor_retorno = "v0"

            self.estructura_return[nombre_metodo] = valor_retorno

            if cuadrupla.op == "+":

                self.text_section += f"\n{'    ' * self.indentation}add ${valor_retorno}, ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"

                return 
        
            elif cuadrupla.op == "-":

                self.text_section += f"\n{'    ' * self.indentation}sub ${valor_retorno}, ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"

                return
            
            elif cuadrupla.op == "*":

                self.text_section += f"\n{'    ' * self.indentation}mul ${valor_retorno}, ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"

                return
            
            elif cuadrupla.op == "/":

                self.text_section += f"\n{'    ' * self.indentation}div ${lista_parametros[0][1]}, ${lista_parametros[1][1]}\n"
                self.text_section += f"{'    ' * self.indentation}mflo ${valor_retorno}\n"
                temp4 = self.get_temp()
                self.text_section += f"{'    ' * self.indentation}mfhi ${temp4}\n"
                self.temp_counter -= 1

                return


        cuadrupla_siguiente = self.cuadruplas_iniciales[self.cuadruplas_iniciales.index(cuadrupla) + 1]

        if cuadrupla.arg1 not in self.variables:
            temp1 = self.get_temp()
            self.text_section += f"\n{'    ' * self.indentation}li ${temp1}, {cuadrupla.arg1}\n"
            self.variables_cargadas[cuadrupla.arg1] = temp1

        if cuadrupla.arg2 not in self.variables:
            temp2 = self.get_temp()
            self.text_section += f"{'    ' * self.indentation}li ${temp2}, {cuadrupla.arg2}\n"
            self.variables_cargadas[cuadrupla.arg2] = temp2

        if cuadrupla.arg1 not in self.variables_cargadas:
            temp1 = self.get_temp()
            self.text_section += f"\n{'    ' * self.indentation}lw ${temp1}, {cuadrupla.arg1}\n"
            self.variables_cargadas[cuadrupla.arg1] = temp1
        if cuadrupla.arg2 not in self.variables_cargadas:
            temp2 = self.get_temp()
            self.text_section += f"{'    ' * self.indentation}lw ${temp2}, {cuadrupla.arg2}\n"
            self.variables_cargadas[cuadrupla.arg2] = temp2

        if cuadrupla.arg1 == cuadrupla_siguiente.result or cuadrupla.arg2 == cuadrupla_siguiente.result:
            if cuadrupla.op == '+':
                self.text_section += f"\n{'    ' * self.indentation}add ${self.variables_cargadas[cuadrupla_siguiente.result]}, ${self.variables_cargadas[cuadrupla.arg1]}, ${self.variables_cargadas[cuadrupla.arg2]}\n"
                self.cuadruplas_procesadas.add(cuadrupla_siguiente)
                return
            elif cuadrupla.op == '-':
                self.text_section += f"\n{'    ' * self.indentation}sub ${self.variables_cargadas[cuadrupla_siguiente.result]}, ${self.variables_cargadas[cuadrupla.arg1]}, ${self.variables_cargadas[cuadrupla.arg2]}\n"
                self.cuadruplas_procesadas.add(cuadrupla_siguiente)
                return

        temp3 = self.get_temp()

        if cuadrupla.op == '+':
            self.text_section += f"\n{'    ' * self.indentation}add ${temp3}, ${self.variables_cargadas[cuadrupla.arg1]}, ${self.variables_cargadas[cuadrupla.arg2]}\n"
        elif cuadrupla.op == '-':
            self.text_section += f"\n{'    ' * self.indentation}sub ${temp3}, ${self.variables_cargadas[cuadrupla.arg1]}, ${self.variables_cargadas[cuadrupla.arg2]}\n"
        elif cuadrupla.op == '*':
            self.text_section += f"\n{'    ' * self.indentation}mul ${temp3}, ${self.variables_cargadas[cuadrupla.arg1]}, ${self.variables_cargadas[cuadrupla.arg2]}\n"
        elif cuadrupla.op == '/':
            self.text_section += f"\n{'    ' * self.indentation}div ${self.variables_cargadas[cuadrupla.arg1]}, ${self.variables_cargadas[cuadrupla.arg2]}\n"
            self.text_section += f"{'    ' * self.indentation}mflo ${temp3}\n"
            temp4 = self.get_temp()
            self.text_section += f"{'    ' * self.indentation}mfhi ${temp4}\n"
            self.temp_counter -= 1

    def mips_metodos(self, cuadrupla):
        
        self.indentation = 0
        if len(self.methods) >= 1 and cuadrupla.arg1 not in self.methods and self.methods[-1] == 'main':
            self.text_section += f"\n{'    '}li $v0, 10\n{'    '}syscall\n"

        self.text_section += f"\n{cuadrupla.arg1}:\n"
        self.methods.append(cuadrupla.arg1)
        self.indentation += 1

    def mips_asignacion(self, cuadrupla):

        if cuadrupla.result not in self.variables:
            if cuadrupla.arg2 == 'String':
                self.data_section += f"{cuadrupla.result}: .asciiz {cuadrupla.arg1}\n"
                self.variables.add(cuadrupla.result)
            elif cuadrupla.arg2 == 'Int':
                self.data_section += f"{cuadrupla.result}: .word {cuadrupla.arg1}\n"
                self.variables.add(cuadrupla.result) 
            elif cuadrupla.arg2 == 'Bool':
                self.data_section += f"{cuadrupla.result}: .word {1 if cuadrupla.arg1 == 'true' else 0}\n"
                self.variables.add(cuadrupla.result)
        else:
            operador_temporal = cuadrupla.arg1

            for cuadrupla_iteradora in reversed(self.cuadruplas_iniciales[:self.cuadruplas_iniciales.index(cuadrupla)]):

                if cuadrupla_iteradora.op == 'CreateMethod':

                    break

                if cuadrupla_iteradora.result == operador_temporal and cuadrupla_iteradora.op == 'MethodHandler':
                    nuevo_temporal = self.get_temp()
                    self.text_section += f"{'    ' * self.indentation}move ${nuevo_temporal}, $v0\n"
                    self.variables_cargadas[cuadrupla.result] = nuevo_temporal
                    return

            self.text_section += f"{'    ' * self.indentation}sw $t{self.temp_counter-1}, {cuadrupla.result}\n"
            self.variables_cargadas[cuadrupla.result] = f"t{self.temp_counter-1}"
    
    def mips_procedure(self, cuadrupla):
        if cuadrupla.arg2 in self.variables_cargadas:
            if cuadrupla.arg1 == 'out_int':
                        self.text_section += f"\n{'    ' * self.indentation}li $v0, 1\n"
                        self.text_section += f"{'    ' * self.indentation}move $a0, ${self.variables_cargadas[cuadrupla.arg2]}\n"
                        self.text_section += f"{'    ' * self.indentation}syscall\n"
            elif cuadrupla.arg1 == 'out_string':
                self.text_section += f"\n{'    ' * self.indentation}li $v0, 4\n"
                self.text_section += f"{'    ' * self.indentation}move $a0, ${self.variables_cargadas[cuadrupla.arg2]}\n"
                self.text_section += f"{'    ' * self.indentation}syscall\n"
        else:
            if cuadrupla.arg1 == 'out_int':
                        self.text_section += f"\n{'    ' * self.indentation}li $v0, 1\n"
                        self.text_section += f"{'    ' * self.indentation}move $a0, ${cuadrupla.arg2}\n"
                        self.text_section += f"{'    ' * self.indentation}syscall\n"
            elif cuadrupla.arg1 == 'out_string':
                self.text_section += f"\n{'    ' * self.indentation}li $v0, 4\n"
                self.text_section += f"{'    ' * self.indentation}move $a0, ${cuadrupla.arg2}\n"
                self.text_section += f"{'    ' * self.indentation}syscall\n"
        self.text_section += f"\n{'    ' * self.indentation}li $v0, 4\n"
        self.text_section += f"{'    ' * self.indentation}la $a0, newline\n"
        self.text_section += f"{'    ' * self.indentation}syscall\n"
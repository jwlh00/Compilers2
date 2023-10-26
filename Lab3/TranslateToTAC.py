from antlr4 import ParseTreeWalker
from YAPLListener import YAPLListener
from YAPLParser import YAPLParser
import re


class Quadruple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __repr__(self):
        if self.op == "class":
            return f"{self.op} {self.arg1} {{"
        elif self.op.endswith(":"):  # for methods like "getAvg:"
            return f"    {self.arg1}:"
        elif self.op in ["declare", "param", "return", "call"]:
            return f"        {self.op} {self.arg1}"
        elif not self.arg2 and self.result:  # For operations with only one argument
            return f"        {self.result} = {self.op} {self.arg1}"
        elif not self.arg2:  # For operations like "return avg"
            return f"        {self.op} {self.arg1}"
        else:  # For binary operations
            return f"        {self.result} = {self.arg1} {self.op} {self.arg2}"
class TACTranslator(YAPLListener):
    def __init__(self):
        self.tac_code = []
        self.temp_counter = 0
        self.label_counter = 0
        self.indent_level = 0
        self.free_temps = []
        self.current_class = None  # Track the current class
        self.class_hierarchy = {}  # Dictionary to store class inheritance relationships
        self.methods = {}  # Dictionary to store methods in each class

    def new_temp(self):
        if self.free_temps:
            return self.free_temps.pop()
        else:
            temp = f"t{self.temp_counter}"
            self.temp_counter += 1
            return temp

    def free_temp(self, temp_name):
        self.free_temps.append(temp_name)

    def add_line(self, line):
        indentation = '    ' * self.indent_level
        operation, *operands = re.split(r"\s+", line.replace("=", ""))
        if len(operands) == 1:
            self.tac_code.append(Quadruple(operation, operands[0], "", ""))
        elif len(operands) == 2:
            self.tac_code.append(Quadruple(operation, "", operands[0], operands[1]))
        elif len(operands) == 3:
            self.tac_code.append(Quadruple(operation, operands[0], operands[1], operands[2]))

    
    def quadruples_to_string(self):
        output = []
        for quad in self.tac_code:
            output.append(str(quad))
        return "\n".join(output)

    def handle_expression(self, expr):
        tokens = re.findall(r"[\w]+|[+*-/]", expr)
        while len(tokens) > 2:  # Ensure there's enough tokens for a valid expression
            left = tokens.pop(0)
            op = tokens.pop(0)
            right = tokens.pop(0)
            temp = self.new_temp()
            self.add_line(f"{temp} = {left} {op} {right}")
            tokens.insert(0, temp)
        return tokens[0] if tokens else None

    def enterClas_list(self, ctx):
        class_name = ctx.type_(0).getText()
        inherits_clause = ""
        if ctx.getChildCount() > 3 and ctx.getChild(2).getText() == "inherits":
            parent_class = ctx.type_(1).getText()
            inherits_clause = f" inherits {parent_class}"
            # Store the class inheritance relationship
            self.class_hierarchy[class_name] = parent_class
        self.current_class = class_name  # Set the current class
        self.methods[class_name] = set()  # Initialize the set of methods for this class
        self.add_line(f"class {class_name}{inherits_clause} {{")
        self.indent_level += 1


    def exitClas_list(self, ctx):
        self.current_class = None  # Reset the current class
        self.indent_level -= 1
        self.add_line("};")

    def handle_inherited_method(self, method_name):
        # Check if the method exists in the current class
        if method_name in self.methods.get(self.current_class, []):
            return method_name
        # Check if the method exists in the parent class
        parent_class = self.class_hierarchy.get(self.current_class)
        while parent_class:
            if method_name in self.methods.get(parent_class, []):
                return f"{parent_class}.{method_name}"
            parent_class = self.class_hierarchy.get(parent_class)
        return None

    def exitAttribute_definition(self, ctx):
        var = ctx.ID().getText()
        if ctx.expr():
            expr = self.handle_expression(ctx.expr()[0].getText())
            self.add_line(f"{var} = {expr}")
        else:
            self.add_line(f"declare {var}")

    def exitVar_assign(self, ctx):
        var = ctx.ID().getText()
        expr = self.handle_expression(ctx.expr().getText())
        self.add_line(f"{var} = {expr}")


    def exitSimple_method_definition(self, ctx):
        # Check if there's a dot indicating it's a method call on an object
        if ctx.getChild(1).getText() == ".":
            object_name = ctx.getChild(0).getText()
            method_name = ctx.getChild(2).getText()
        else:
            object_name = None
            method_name = ctx.ID(0).getText()

        # Extract parameters for the method and generate TAC
        if ctx.expr():
            for e in ctx.expr():
                expr = self.handle_expression(e.getText())
                self.add_line(f"param {expr}")

        # Generate the TAC for the method call. Differentiate between object method call and standalone function call.
        if object_name:
            # Check if the method is inherited or overridden
            method_ref = self.handle_inherited_method(method_name)
            if method_ref:
                self.add_line(f"call {object_name}.{method_ref}")
            else:
                self.add_line(f"call {object_name}.{method_name}")
        else:
            self.add_line(f"call {method_name}")

    def enterMethod_definition(self, ctx):
        method_name = ctx.ID().getText()
        self.add_line(f"{method_name}:")
        self.indent_level += 1
        if ctx.parameter_list():
            for param in ctx.parameter_list().formal():
                param_name = param.ID().getText()
                self.add_line(f"param {param_name}")

    def exitMethod_definition(self, ctx):
        method_name = ctx.ID().getText()
        self.methods[self.current_class].add(method_name)  # Add the method to the current class
        return_val = ctx.return_statement().expr().getText()
        self.add_line(f"{method_name}:")
        self.indent_level += 1
        if ctx.parameter_list():
            for param in ctx.parameter_list().formal():
                param_name = param.ID().getText()
                self.add_line(f"param {param_name}")
        self.handle_expression(return_val)  # Handle the method's return expression
        self.indent_level -= 1

    def enterMain_method(self, ctx):
        self.add_line("class main {")
        self.indent_level += 1
        self.add_line("main:")

    def enterIf_statement(self, ctx):
        self.end_label = f"L{self.label_counter}"
        self.label_counter += 1
        self.start_label = f"L{self.label_counter}"
        self.label_counter += 1
        condition = ctx.expr().getText().replace("=", "==")
        self.add_line(f"if not {condition} goto {self.start_label}")
        self.add_line(f"goto {self.end_label}")
        self.add_line(f"{self.start_label}:")

    def exitIf_statement(self, ctx):
        self.add_line(f"{self.end_label}:")



    def enterWhile_statement(self, ctx):
        self.start_while_label = f"L{self.label_counter}"
        self.label_counter += 1
        self.end_while_label = f"L{self.label_counter}"
        self.label_counter += 1
        self.add_line(f"{self.start_while_label}:")
        self.loop_condition_label = f"L{self.label_counter}"
        self.label_counter += 1
        self.loop_exit_label = f"L{self.label_counter}"
        self.label_counter += 1
        condition = ctx.expr().getText().replace("=", "==")
        self.add_line(f"if not {condition} goto {self.loop_exit_label}")

    def exitWhile_statement(self, ctx):
        self.add_line(f"goto {self.start_while_label}")
        self.add_line(f"{self.loop_exit_label}:")



    def exitMain_method(self, ctx):
        self.add_line("end_main")
        self.indent_level -= 1
        self.add_line("};")

    def translate(self, tree):
        walker = ParseTreeWalker()
        walker.walk(self, tree)
        

    def get_quadruples(self):
        quadruples = []
        for quad in self.tac_code:
            quadruples.append((quad.op, quad.arg1, quad.arg2, quad.result))
        return quadruples


    
    def get_TAC(self):
        current_class = None  # Track the current class name
        current_method = None  # Track the current method name
        debug_output = []  # List to store the debug information
        for quad in self.tac_code:
            if quad.op == "class":
                if current_class is not None:
                    debug_output.append("};")
                current_class = quad.arg2  # Class name is in arg2
                current_method = None  # Reset the current method
                debug_output.append(f"class {current_class} {{")
            elif quad.op.endswith(":"):
                if current_method is not None:
                    debug_output.append("    return void")
                current_method = quad.arg1  # Method label is in arg1
                debug_output.append(f"    {quad.arg1}:")
            elif quad.op in ["declare", "param", "return"]:
                debug_output.append(f"    {quad.op} {quad.arg1}")
            elif not quad.arg2 and quad.result:
                debug_output.append(f"    {quad.result} = {quad.arg1} {quad.op}")
            elif not quad.arg2:
                debug_output.append(f"    {quad.op} {quad.arg1} {quad.arg2} {quad.result}")
            else:
                debug_output.append(f"    {quad.op} {quad.arg1} {quad.arg2} {quad.result}")
        if current_class is not None:
            debug_output.append("};")
        return "\n".join(debug_output)

    def get_TACDebug(self):
        current_class = None  # Track the current class name
        current_method = None  # Track the current method name
        debug_output = []  # List to store the debug information
        for quad in self.tac_code:
            debug_line = f"D|EBUG: op={quad.op}, arg1={quad.arg1}, arg2={quad.arg2}, result={quad.result}"
            debug_output.append(debug_line)
            if quad.op == "class":
                current_class = quad.arg2  # Class name is in arg2
                current_method = None  # Reset the current method
                debug_output.append(f"class {current_class} {{")
            elif quad.op.endswith(":"):
                current_method = quad.arg1  # Method label is in arg1
                debug_output.append(f"    {quad.op} {current_method}:")
            elif quad.op in ["declare", "param", "return", "call"]:
                debug_output.append(f"        {quad.op} {quad.arg1}")
            elif not quad.arg2 and quad.result:
                debug_output.append(f"        {quad.result} = {quad.op} {quad.arg1} {quad.arg2}")
            elif not quad.arg2:
                debug_output.append(f"        {quad.op} {quad.arg1} {quad.arg2} {quad.result}")
            else:
                debug_output.append(f"        {quad.op} {quad.arg1} {quad.arg2} {quad.result}")
        debug_output.append("};")
        return "\n".join(debug_output)  # Convert the list to a string with newlines








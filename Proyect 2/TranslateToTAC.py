from antlr4 import ParseTreeWalker
from YAPLListener import YAPLListener
from YAPLParser import YAPLParser
import re

class TACTranslator(YAPLListener):
    def __init__(self):
        self.tac_code = []
        self.temp_counter = 0
        self.label_counter = 0
        self.indent_level = 0
        self.free_temps = []
        

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
        self.tac_code.append(indentation + line)

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
            inherits_clause = f" inherits {ctx.type_(1).getText()}"
        self.add_line(f"class {class_name}{inherits_clause} {{")
        self.indent_level += 1

    def exitClas_list(self, ctx):
        self.indent_level -= 1
        self.add_line("};")

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
        return_val = ctx.return_statement().expr().getText()
        self.add_line(f"return {return_val}")
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
        return "\n".join(self.tac_code)

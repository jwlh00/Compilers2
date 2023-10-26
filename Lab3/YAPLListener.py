# Generated from YAPL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#class.
    def enterClass(self, ctx:YAPLParser.ClassContext):
        pass

    # Exit a parse tree produced by YAPLParser#class.
    def exitClass(self, ctx:YAPLParser.ClassContext):
        pass


    # Enter a parse tree produced by YAPLParser#inherits.
    def enterInherits(self, ctx:YAPLParser.InheritsContext):
        pass

    # Exit a parse tree produced by YAPLParser#inherits.
    def exitInherits(self, ctx:YAPLParser.InheritsContext):
        pass


    # Enter a parse tree produced by YAPLParser#type.
    def enterType(self, ctx:YAPLParser.TypeContext):
        pass

    # Exit a parse tree produced by YAPLParser#type.
    def exitType(self, ctx:YAPLParser.TypeContext):
        pass


    # Enter a parse tree produced by YAPLParser#binary_op.
    def enterBinary_op(self, ctx:YAPLParser.Binary_opContext):
        pass

    # Exit a parse tree produced by YAPLParser#binary_op.
    def exitBinary_op(self, ctx:YAPLParser.Binary_opContext):
        pass


    # Enter a parse tree produced by YAPLParser#unary_op.
    def enterUnary_op(self, ctx:YAPLParser.Unary_opContext):
        pass

    # Exit a parse tree produced by YAPLParser#unary_op.
    def exitUnary_op(self, ctx:YAPLParser.Unary_opContext):
        pass


    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#clas_list.
    def enterClas_list(self, ctx:YAPLParser.Clas_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#clas_list.
    def exitClas_list(self, ctx:YAPLParser.Clas_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature_list.
    def enterFeature_list(self, ctx:YAPLParser.Feature_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature_list.
    def exitFeature_list(self, ctx:YAPLParser.Feature_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#feature.
    def enterFeature(self, ctx:YAPLParser.FeatureContext):
        pass

    # Exit a parse tree produced by YAPLParser#feature.
    def exitFeature(self, ctx:YAPLParser.FeatureContext):
        pass


    # Enter a parse tree produced by YAPLParser#attribute_definition.
    def enterAttribute_definition(self, ctx:YAPLParser.Attribute_definitionContext):
        pass

    # Exit a parse tree produced by YAPLParser#attribute_definition.
    def exitAttribute_definition(self, ctx:YAPLParser.Attribute_definitionContext):
        pass


    # Enter a parse tree produced by YAPLParser#var_assign.
    def enterVar_assign(self, ctx:YAPLParser.Var_assignContext):
        pass

    # Exit a parse tree produced by YAPLParser#var_assign.
    def exitVar_assign(self, ctx:YAPLParser.Var_assignContext):
        pass


    # Enter a parse tree produced by YAPLParser#method_definition.
    def enterMethod_definition(self, ctx:YAPLParser.Method_definitionContext):
        pass

    # Exit a parse tree produced by YAPLParser#method_definition.
    def exitMethod_definition(self, ctx:YAPLParser.Method_definitionContext):
        pass


    # Enter a parse tree produced by YAPLParser#return_statement.
    def enterReturn_statement(self, ctx:YAPLParser.Return_statementContext):
        pass

    # Exit a parse tree produced by YAPLParser#return_statement.
    def exitReturn_statement(self, ctx:YAPLParser.Return_statementContext):
        pass


    # Enter a parse tree produced by YAPLParser#let_declaration.
    def enterLet_declaration(self, ctx:YAPLParser.Let_declarationContext):
        pass

    # Exit a parse tree produced by YAPLParser#let_declaration.
    def exitLet_declaration(self, ctx:YAPLParser.Let_declarationContext):
        pass


    # Enter a parse tree produced by YAPLParser#let_binding.
    def enterLet_binding(self, ctx:YAPLParser.Let_bindingContext):
        pass

    # Exit a parse tree produced by YAPLParser#let_binding.
    def exitLet_binding(self, ctx:YAPLParser.Let_bindingContext):
        pass


    # Enter a parse tree produced by YAPLParser#if_statement.
    def enterIf_statement(self, ctx:YAPLParser.If_statementContext):
        pass

    # Exit a parse tree produced by YAPLParser#if_statement.
    def exitIf_statement(self, ctx:YAPLParser.If_statementContext):
        pass


    # Enter a parse tree produced by YAPLParser#while_statement.
    def enterWhile_statement(self, ctx:YAPLParser.While_statementContext):
        pass

    # Exit a parse tree produced by YAPLParser#while_statement.
    def exitWhile_statement(self, ctx:YAPLParser.While_statementContext):
        pass


    # Enter a parse tree produced by YAPLParser#block.
    def enterBlock(self, ctx:YAPLParser.BlockContext):
        pass

    # Exit a parse tree produced by YAPLParser#block.
    def exitBlock(self, ctx:YAPLParser.BlockContext):
        pass


    # Enter a parse tree produced by YAPLParser#simple_method_definition.
    def enterSimple_method_definition(self, ctx:YAPLParser.Simple_method_definitionContext):
        pass

    # Exit a parse tree produced by YAPLParser#simple_method_definition.
    def exitSimple_method_definition(self, ctx:YAPLParser.Simple_method_definitionContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#parameter_list.
    def enterParameter_list(self, ctx:YAPLParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#parameter_list.
    def exitParameter_list(self, ctx:YAPLParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#expr.
    def enterExpr(self, ctx:YAPLParser.ExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#expr.
    def exitExpr(self, ctx:YAPLParser.ExprContext):
        pass



del YAPLParser
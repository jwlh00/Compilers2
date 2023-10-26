grammar YAPL;

/* Lexer rules */
CLASS: 'class';
INHERITS: 'inherits';
BOOL: 'Bool';
INT: 'Int';
STRING: 'String';
IO: 'IO';
OBJECT: 'Object';
SELF_TYPE: 'SELF_TYPE';
IF: 'if';
THEN: 'then';
ELSE: 'else';
FI: 'fi';
WHILE: 'while';
LOOP: 'loop';
POOL: 'pool';
LET: 'let';
IN: 'in';
CASE: 'case';
OF: 'of';
ESAC: 'esac';
NEW: 'new';
ISVOID: 'isvoid';
NOT: 'not';

ID: [a-zA-Z][a-zA-Z0-9_]*;
INT_CONST: [0-9]+;
STR_CONST: '"' (~["\r\n\\] | '\\' [\\"'\r\n]) '"';
WS: [ \t\r\n]+ -> skip;

/* Parser rules */
program: class_list;

class_list: class_item+;

class_item: 'class' TYPE (INHERITS TYPE)? '{' feature_list '}';

feature_list: feature_item*;

feature_item: attribute | method;

attribute: ID ':' TYPE (ASSIGN expr)?;

method: ID '(' param_list? ')' ':' TYPE '{' expr '}';

param_list: formal_param (',' formal_param)*;

formal_param: ID ':' TYPE;

expr: if_expr;

if_expr: if_expr_tail;

if_expr_tail: while_expr (THEN expr ELSE if_expr_tail)?;

while_expr: block_expr;

block_expr: block_expr_tail;

block_expr_tail: let_expr;

let_expr: let_expr_tail;

let_expr_tail: case_expr;

case_expr: case_expr_tail;

case_expr_tail: new_expr;

new_expr: new_expr_tail;

new_expr_tail: isvoid_expr;

isvoid_expr: isvoid_expr_tail;

isvoid_expr_tail: binary_expr;

binary_expr: unary_expr (binary_op unary_expr)*;

unary_expr: primary_expr;

primary_expr:
	ID
	| INT_CONST
	| STR_CONST
	| BOOL
	| '(' expr ')'
	| ID '(' arg_list? ')'
	| SELF_TYPE '.' ID '(' arg_list? ')';

arg_list: expr (',' expr)*;

binary_op: '+' | '-' | '*' | '/' | '<' | '<=' | '=' | '@';

TYPE: [A-Z][a-zA-Z0-9_]*;

ASSIGN: '<-';

ARROW: '=>';

SEMI: ';';

COLON: ':';

COMMA: ',';

DOT: '.';

LPAREN: '(';

RPAREN: ')';

LBRACE: '{';

RBRACE: '}';

/* Ignored tokens */
COMMENT: '--' ~[\r\n]* -> skip;

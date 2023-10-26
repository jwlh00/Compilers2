// Generated from c:\Users\Andre\OneDrive\Universidad\Cuarto año\Segundo Semestre\Compiladores\Laboratorios\Lab 2\YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, ID=29, INT_CONST=30, STR_CONST=31, 
		WS=32, BOOL=33, INT=34, STRING=35, IO=36, OBJECT=37, SELF_TYPE=38, CASE=39, 
		OF=40, ESAC=41, NEW=42, ISVOID=43, NOT=44, ASSIGN=45, ARROW=46, SEMI=47, 
		COLON=48, COMMA=49, DOT=50, LPAREN=51, RPAREN=52, LBRACE=53, RBRACE=54, 
		LINE_COMMENT=55, COMMENT=56, ErrorChar=57;
	public static final int
		RULE_class = 0, RULE_inherits = 1, RULE_type = 2, RULE_binary_op = 3, 
		RULE_unary_op = 4, RULE_program = 5, RULE_clas_list = 6, RULE_feature_list = 7, 
		RULE_feature = 8, RULE_attribute_definition = 9, RULE_var_assign = 10, 
		RULE_method_definition = 11, RULE_return_statement = 12, RULE_let_declaration = 13, 
		RULE_let_binding = 14, RULE_if_statement = 15, RULE_while_statement = 16, 
		RULE_block = 17, RULE_simple_method_definition = 18, RULE_formal = 19, 
		RULE_parameter_list = 20, RULE_expr = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"class", "inherits", "type", "binary_op", "unary_op", "program", "clas_list", 
			"feature_list", "feature", "attribute_definition", "var_assign", "method_definition", 
			"return_statement", "let_declaration", "let_binding", "if_statement", 
			"while_statement", "block", "simple_method_definition", "formal", "parameter_list", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'inherits'", "'+'", "'-'", "'*'", "'/'", "'<'", "'<='", 
			"'='", "'@'", "'~'", "'return'", "'let'", "'in'", "'if'", "'then'", "'else'", 
			"'fi'", "'while'", "'loop'", "'pool'", "'self'", "'true'", "'false'", 
			"'v'", "'>'", "'%'", "'^'", null, null, null, null, "'Bool'", "'Int'", 
			"'String'", "'IO'", "'Object'", "'SELF_TYPE'", "'case'", "'of'", "'esac'", 
			"'new'", "'isvoid'", "'not'", "'<-'", "'=>'", "';'", "':'", "','", "'.'", 
			"'('", "')'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "ID", "INT_CONST", "STR_CONST", "WS", "BOOL", 
			"INT", "STRING", "IO", "OBJECT", "SELF_TYPE", "CASE", "OF", "ESAC", "NEW", 
			"ISVOID", "NOT", "ASSIGN", "ARROW", "SEMI", "COLON", "COMMA", "DOT", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "LINE_COMMENT", "COMMENT", "ErrorChar"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ClassContext extends ParserRuleContext {
		public ClassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class; }
	}

	public final ClassContext class() throws RecognitionException {
		ClassContext _localctx = new ClassContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_class);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InheritsContext extends ParserRuleContext {
		public InheritsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inherits; }
	}

	public final InheritsContext inherits() throws RecognitionException {
		InheritsContext _localctx = new InheritsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_inherits);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode BOOL() { return getToken(YAPLParser.BOOL, 0); }
		public TerminalNode INT() { return getToken(YAPLParser.INT, 0); }
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public TerminalNode IO() { return getToken(YAPLParser.IO, 0); }
		public TerminalNode OBJECT() { return getToken(YAPLParser.OBJECT, 0); }
		public TerminalNode SELF_TYPE() { return getToken(YAPLParser.SELF_TYPE, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << BOOL) | (1L << INT) | (1L << STRING) | (1L << IO) | (1L << OBJECT) | (1L << SELF_TYPE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Binary_opContext extends ParserRuleContext {
		public Binary_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binary_op; }
	}

	public final Binary_opContext binary_op() throws RecognitionException {
		Binary_opContext _localctx = new Binary_opContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_binary_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Unary_opContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public Unary_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary_op; }
	}

	public final Unary_opContext unary_op() throws RecognitionException {
		Unary_opContext _localctx = new Unary_opContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_unary_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !(_la==T__10 || _la==NOT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<Clas_listContext> clas_list() {
			return getRuleContexts(Clas_listContext.class);
		}
		public Clas_listContext clas_list(int i) {
			return getRuleContext(Clas_listContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(54);
				clas_list();
				}
				}
				setState(57); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__0 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Clas_listContext extends ParserRuleContext {
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public TerminalNode LBRACE() { return getToken(YAPLParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(YAPLParser.RBRACE, 0); }
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public Feature_listContext feature_list() {
			return getRuleContext(Feature_listContext.class,0);
		}
		public Clas_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clas_list; }
	}

	public final Clas_listContext clas_list() throws RecognitionException {
		Clas_listContext _localctx = new Clas_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_clas_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__0);
			setState(60);
			type();
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(61);
				match(T__1);
				setState(62);
				type();
				}
			}

			setState(65);
			match(LBRACE);
			{
			setState(66);
			feature_list();
			}
			setState(67);
			match(RBRACE);
			setState(68);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Feature_listContext extends ParserRuleContext {
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public Feature_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature_list; }
	}

	public final Feature_listContext feature_list() throws RecognitionException {
		Feature_listContext _localctx = new Feature_listContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_feature_list);
		int _la;
		try {
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==ID) {
					{
					{
					setState(70);
					feature();
					}
					}
					setState(75);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==ID) {
					{
					{
					setState(76);
					formal();
					}
					}
					setState(81);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public Attribute_definitionContext attribute_definition() {
			return getRuleContext(Attribute_definitionContext.class,0);
		}
		public Method_definitionContext method_definition() {
			return getRuleContext(Method_definitionContext.class,0);
		}
		public Simple_method_definitionContext simple_method_definition() {
			return getRuleContext(Simple_method_definitionContext.class,0);
		}
		public Var_assignContext var_assign() {
			return getRuleContext(Var_assignContext.class,0);
		}
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_feature);
		try {
			setState(88);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				attribute_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				method_definition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(86);
				simple_method_definition();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(87);
				var_assign();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attribute_definitionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public List<TerminalNode> SEMI() { return getTokens(YAPLParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(YAPLParser.SEMI, i);
		}
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LPAREN() { return getToken(YAPLParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLParser.RPAREN, 0); }
		public Attribute_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute_definition; }
	}

	public final Attribute_definitionContext attribute_definition() throws RecognitionException {
		Attribute_definitionContext _localctx = new Attribute_definitionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_attribute_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(ID);
			setState(91);
			match(COLON);
			setState(92);
			type();
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(93);
				match(ASSIGN);
				setState(94);
				expr(0);
				}
			}

			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LPAREN) {
				{
				setState(97);
				match(LPAREN);
				setState(98);
				expr(0);
				setState(99);
				match(SEMI);
				setState(100);
				match(RPAREN);
				}
			}

			setState(104);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_assignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Simple_method_definitionContext simple_method_definition() {
			return getRuleContext(Simple_method_definitionContext.class,0);
		}
		public Var_assignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_assign; }
	}

	public final Var_assignContext var_assign() throws RecognitionException {
		Var_assignContext _localctx = new Var_assignContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_var_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(ID);
			setState(107);
			match(ASSIGN);
			setState(110);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(108);
				expr(0);
				}
				break;
			case 2:
				{
				setState(109);
				simple_method_definition();
				}
				break;
			}
			setState(112);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_definitionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(YAPLParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(YAPLParser.LBRACE, 0); }
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(YAPLParser.RBRACE, 0); }
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public Parameter_listContext parameter_list() {
			return getRuleContext(Parameter_listContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<Method_definitionContext> method_definition() {
			return getRuleContexts(Method_definitionContext.class);
		}
		public Method_definitionContext method_definition(int i) {
			return getRuleContext(Method_definitionContext.class,i);
		}
		public List<Simple_method_definitionContext> simple_method_definition() {
			return getRuleContexts(Simple_method_definitionContext.class);
		}
		public Simple_method_definitionContext simple_method_definition(int i) {
			return getRuleContext(Simple_method_definitionContext.class,i);
		}
		public Method_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_definition; }
	}

	public final Method_definitionContext method_definition() throws RecognitionException {
		Method_definitionContext _localctx = new Method_definitionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_method_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(ID);
			setState(115);
			match(LPAREN);
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(116);
				parameter_list();
				}
			}

			setState(119);
			match(RPAREN);
			setState(120);
			match(COLON);
			setState(121);
			type();
			setState(122);
			match(LBRACE);
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__14) | (1L << T__18) | (1L << ID))) != 0)) {
				{
				setState(126);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(123);
					block();
					}
					break;
				case 2:
					{
					setState(124);
					method_definition();
					}
					break;
				case 3:
					{
					setState(125);
					simple_method_definition();
					}
					break;
				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(131);
			return_statement();
			setState(132);
			match(RBRACE);
			setState(133);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(T__11);
			setState(136);
			expr(0);
			setState(137);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Let_declarationContext extends ParserRuleContext {
		public List<Let_bindingContext> let_binding() {
			return getRuleContexts(Let_bindingContext.class);
		}
		public Let_bindingContext let_binding(int i) {
			return getRuleContext(Let_bindingContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public TerminalNode LBRACE() { return getToken(YAPLParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(YAPLParser.RBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(YAPLParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(YAPLParser.SEMI, i);
		}
		public Let_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_declaration; }
	}

	public final Let_declarationContext let_declaration() throws RecognitionException {
		Let_declarationContext _localctx = new Let_declarationContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_let_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(T__12);
			setState(140);
			let_binding();
			setState(145);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(141);
				match(COMMA);
				setState(142);
				let_binding();
				}
				}
				setState(147);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__13) {
				{
				setState(148);
				match(T__13);
				setState(149);
				match(LBRACE);
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << ID) | (1L << INT_CONST) | (1L << STR_CONST) | (1L << NEW) | (1L << ISVOID) | (1L << NOT) | (1L << LPAREN))) != 0)) {
					{
					{
					setState(150);
					expr(0);
					setState(151);
					match(SEMI);
					}
					}
					setState(157);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(158);
				match(RBRACE);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Let_bindingContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Let_bindingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_let_binding; }
	}

	public final Let_bindingContext let_binding() throws RecognitionException {
		Let_bindingContext _localctx = new Let_bindingContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_let_binding);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(ID);
			setState(162);
			match(COLON);
			setState(163);
			type();
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN) {
				{
				setState(164);
				match(ASSIGN);
				setState(165);
				expr(0);
				}
			}

			setState(169);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(168);
				type();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public List<Simple_method_definitionContext> simple_method_definition() {
			return getRuleContexts(Simple_method_definitionContext.class);
		}
		public Simple_method_definitionContext simple_method_definition(int i) {
			return getRuleContext(Simple_method_definitionContext.class,i);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(T__14);
			setState(172);
			expr(0);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(173);
				match(T__15);
				setState(178);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__14) | (1L << T__18) | (1L << ID))) != 0)) {
					{
					setState(176);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						setState(174);
						simple_method_definition();
						}
						break;
					case 2:
						{
						setState(175);
						block();
						}
						break;
					}
					}
					setState(180);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(185);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(186);
				match(T__16);
				setState(191);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__14) | (1L << T__18) | (1L << ID))) != 0)) {
					{
					setState(189);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						setState(187);
						simple_method_definition();
						}
						break;
					case 2:
						{
						setState(188);
						block();
						}
						break;
					}
					}
					setState(193);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(196);
				return_statement();
				}
			}

			setState(199);
			match(T__17);
			setState(200);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_statementContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public List<Simple_method_definitionContext> simple_method_definition() {
			return getRuleContexts(Simple_method_definitionContext.class);
		}
		public Simple_method_definitionContext simple_method_definition(int i) {
			return getRuleContext(Simple_method_definitionContext.class,i);
		}
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_while_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(T__18);
			setState(203);
			expr(0);
			setState(204);
			match(T__19);
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__14) | (1L << T__18) | (1L << ID))) != 0)) {
				{
				setState(207);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
				case 1:
					{
					setState(205);
					block();
					}
					break;
				case 2:
					{
					setState(206);
					simple_method_definition();
					}
					break;
				}
				}
				setState(211);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(212);
			match(T__20);
			setState(213);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public Let_declarationContext let_declaration() {
			return getRuleContext(Let_declarationContext.class,0);
		}
		public Var_assignContext var_assign() {
			return getRuleContext(Var_assignContext.class,0);
		}
		public Attribute_definitionContext attribute_definition() {
			return getRuleContext(Attribute_definitionContext.class,0);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_block);
		try {
			setState(220);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				if_statement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(216);
				while_statement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(217);
				let_declaration();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(218);
				var_assign();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(219);
				attribute_definition();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Simple_method_definitionContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(YAPLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(YAPLParser.ID, i);
		}
		public TerminalNode LPAREN() { return getToken(YAPLParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(YAPLParser.SEMI, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public TerminalNode DOT() { return getToken(YAPLParser.DOT, 0); }
		public Simple_method_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simple_method_definition; }
	}

	public final Simple_method_definitionContext simple_method_definition() throws RecognitionException {
		Simple_method_definitionContext _localctx = new Simple_method_definitionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_simple_method_definition);
		int _la;
		try {
			setState(252);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				match(ID);
				setState(223);
				match(LPAREN);
				setState(225);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << ID) | (1L << INT_CONST) | (1L << STR_CONST) | (1L << NEW) | (1L << ISVOID) | (1L << NOT) | (1L << LPAREN))) != 0)) {
					{
					setState(224);
					expr(0);
					}
				}

				setState(231);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(227);
					match(COMMA);
					setState(228);
					expr(0);
					}
					}
					setState(233);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(234);
				match(RPAREN);
				setState(235);
				match(SEMI);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				match(ID);
				setState(237);
				match(DOT);
				setState(238);
				match(ID);
				setState(239);
				match(LPAREN);
				setState(241);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24) | (1L << ID) | (1L << INT_CONST) | (1L << STR_CONST) | (1L << NEW) | (1L << ISVOID) | (1L << NOT) | (1L << LPAREN))) != 0)) {
					{
					setState(240);
					expr(0);
					}
				}

				setState(247);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(243);
					match(COMMA);
					setState(244);
					expr(0);
					}
					}
					setState(249);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(250);
				match(RPAREN);
				setState(251);
				match(SEMI);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode COLON() { return getToken(YAPLParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(254);
			match(ID);
			setState(255);
			match(COLON);
			setState(256);
			type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parameter_listContext extends ParserRuleContext {
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(YAPLParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(YAPLParser.COMMA, i);
		}
		public Parameter_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter_list; }
	}

	public final Parameter_listContext parameter_list() throws RecognitionException {
		Parameter_listContext _localctx = new Parameter_listContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_parameter_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			formal();
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(259);
				match(COMMA);
				setState(260);
				formal();
				}
				}
				setState(265);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(YAPLParser.ASSIGN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode STR_CONST() { return getToken(YAPLParser.STR_CONST, 0); }
		public TerminalNode INT_CONST() { return getToken(YAPLParser.INT_CONST, 0); }
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public TerminalNode LPAREN() { return getToken(YAPLParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(YAPLParser.RPAREN, 0); }
		public TerminalNode DOT() { return getToken(YAPLParser.DOT, 0); }
		public List<TerminalNode> SEMI() { return getTokens(YAPLParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(YAPLParser.SEMI, i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,34,_ctx) ) {
			case 1:
				{
				setState(267);
				match(ID);
				setState(268);
				match(ASSIGN);
				setState(269);
				expr(30);
				}
				break;
			case 2:
				{
				setState(270);
				match(STR_CONST);
				}
				break;
			case 3:
				{
				setState(271);
				match(INT_CONST);
				}
				break;
			case 4:
				{
				setState(272);
				match(NEW);
				setState(273);
				match(ID);
				}
				break;
			case 5:
				{
				setState(274);
				match(NEW);
				setState(275);
				type();
				}
				break;
			case 6:
				{
				setState(276);
				match(ISVOID);
				setState(277);
				expr(25);
				}
				break;
			case 7:
				{
				setState(278);
				match(INT_CONST);
				}
				break;
			case 8:
				{
				setState(279);
				match(STR_CONST);
				}
				break;
			case 9:
				{
				setState(280);
				match(NOT);
				setState(281);
				expr(22);
				}
				break;
			case 10:
				{
				setState(282);
				match(LPAREN);
				setState(284); 
				_errHandler.sync(this);
				_alt = 1+1;
				do {
					switch (_alt) {
					case 1+1:
						{
						{
						setState(283);
						expr(0);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(286); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
				} while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(288);
				match(RPAREN);
				}
				break;
			case 11:
				{
				setState(290);
				match(ISVOID);
				setState(291);
				expr(20);
				}
				break;
			case 12:
				{
				setState(292);
				match(T__21);
				}
				break;
			case 13:
				{
				setState(293);
				match(T__22);
				}
				break;
			case 14:
				{
				setState(294);
				match(T__23);
				}
				break;
			case 15:
				{
				setState(295);
				match(T__24);
				}
				break;
			case 16:
				{
				setState(296);
				match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(391);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(389);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(299);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(300);
						match(T__8);
						setState(301);
						expr(10);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(302);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(303);
						match(T__27);
						setState(304);
						expr(4);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(305);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(306);
						match(T__7);
						setState(307);
						expr(3);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(308);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(309);
						match(T__9);
						setState(310);
						type();
						setState(311);
						match(DOT);
						setState(312);
						match(ID);
						setState(313);
						match(LPAREN);
						setState(314);
						expr(0);
						setState(319);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==SEMI) {
							{
							{
							setState(315);
							match(SEMI);
							setState(316);
							expr(0);
							}
							}
							setState(321);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						setState(322);
						match(RPAREN);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(324);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(325);
						match(T__10);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(326);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(329); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(327);
								match(T__3);
								setState(328);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(331); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(333);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(336); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(334);
								match(T__2);
								setState(335);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(338); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(340);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(343); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(341);
								match(T__6);
								setState(342);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(345); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 9:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(347);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(350); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(348);
								match(T__25);
								setState(349);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(352); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 10:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(354);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(357); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(355);
								match(T__2);
								setState(356);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(359); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,40,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 11:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(361);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(364); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(362);
								match(T__3);
								setState(363);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(366); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 12:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(368);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(371); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(369);
								match(T__4);
								setState(370);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(373); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,42,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 13:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(375);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(378); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(376);
								match(T__5);
								setState(377);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(380); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,43,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					case 14:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(382);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(385); 
						_errHandler.sync(this);
						_alt = 1;
						do {
							switch (_alt) {
							case 1:
								{
								{
								setState(383);
								match(T__26);
								setState(384);
								expr(0);
								}
								}
								break;
							default:
								throw new NoViableAltException(this);
							}
							setState(387); 
							_errHandler.sync(this);
							_alt = getInterpreter().adaptivePredict(_input,44,_ctx);
						} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
						}
						break;
					}
					} 
				}
				setState(393);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,46,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 21:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 9);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		case 3:
			return precpred(_ctx, 15);
		case 4:
			return precpred(_ctx, 14);
		case 5:
			return precpred(_ctx, 13);
		case 6:
			return precpred(_ctx, 12);
		case 7:
			return precpred(_ctx, 11);
		case 8:
			return precpred(_ctx, 10);
		case 9:
			return precpred(_ctx, 8);
		case 10:
			return precpred(_ctx, 7);
		case 11:
			return precpred(_ctx, 6);
		case 12:
			return precpred(_ctx, 5);
		case 13:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;\u018d\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\3\3\3\3\4"+
		"\3\4\3\5\3\5\3\6\3\6\3\7\6\7:\n\7\r\7\16\7;\3\b\3\b\3\b\3\b\5\bB\n\b\3"+
		"\b\3\b\3\b\3\b\3\b\3\t\7\tJ\n\t\f\t\16\tM\13\t\3\t\7\tP\n\t\f\t\16\tS"+
		"\13\t\5\tU\n\t\3\n\3\n\3\n\3\n\5\n[\n\n\3\13\3\13\3\13\3\13\3\13\5\13"+
		"b\n\13\3\13\3\13\3\13\3\13\3\13\5\13i\n\13\3\13\3\13\3\f\3\f\3\f\3\f\5"+
		"\fq\n\f\3\f\3\f\3\r\3\r\3\r\5\rx\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0081"+
		"\n\r\f\r\16\r\u0084\13\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\7\17\u0092\n\17\f\17\16\17\u0095\13\17\3\17\3\17\3\17\3\17"+
		"\3\17\7\17\u009c\n\17\f\17\16\17\u009f\13\17\3\17\5\17\u00a2\n\17\3\20"+
		"\3\20\3\20\3\20\3\20\5\20\u00a9\n\20\3\20\5\20\u00ac\n\20\3\21\3\21\3"+
		"\21\3\21\3\21\7\21\u00b3\n\21\f\21\16\21\u00b6\13\21\7\21\u00b8\n\21\f"+
		"\21\16\21\u00bb\13\21\3\21\3\21\3\21\7\21\u00c0\n\21\f\21\16\21\u00c3"+
		"\13\21\5\21\u00c5\n\21\3\21\5\21\u00c8\n\21\3\21\3\21\3\21\3\22\3\22\3"+
		"\22\3\22\3\22\7\22\u00d2\n\22\f\22\16\22\u00d5\13\22\3\22\3\22\3\22\3"+
		"\23\3\23\3\23\3\23\3\23\5\23\u00df\n\23\3\24\3\24\3\24\5\24\u00e4\n\24"+
		"\3\24\3\24\7\24\u00e8\n\24\f\24\16\24\u00eb\13\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\5\24\u00f4\n\24\3\24\3\24\7\24\u00f8\n\24\f\24\16\24\u00fb"+
		"\13\24\3\24\3\24\5\24\u00ff\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\7"+
		"\26\u0108\n\26\f\26\16\26\u010b\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3"+
		"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\6\27\u011f"+
		"\n\27\r\27\16\27\u0120\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5"+
		"\27\u012c\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0140\n\27\f\27\16\27\u0143\13"+
		"\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\6\27\u014c\n\27\r\27\16\27\u014d"+
		"\3\27\3\27\3\27\6\27\u0153\n\27\r\27\16\27\u0154\3\27\3\27\3\27\6\27\u015a"+
		"\n\27\r\27\16\27\u015b\3\27\3\27\3\27\6\27\u0161\n\27\r\27\16\27\u0162"+
		"\3\27\3\27\3\27\6\27\u0168\n\27\r\27\16\27\u0169\3\27\3\27\3\27\6\27\u016f"+
		"\n\27\r\27\16\27\u0170\3\27\3\27\3\27\6\27\u0176\n\27\r\27\16\27\u0177"+
		"\3\27\3\27\3\27\6\27\u017d\n\27\r\27\16\27\u017e\3\27\3\27\3\27\6\27\u0184"+
		"\n\27\r\27\16\27\u0185\7\27\u0188\n\27\f\27\16\27\u018b\13\27\3\27\3\u0120"+
		"\3,\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\5\4\2\37\37#("+
		"\3\2\5\f\4\2\r\r..\2\u01c5\2.\3\2\2\2\4\60\3\2\2\2\6\62\3\2\2\2\b\64\3"+
		"\2\2\2\n\66\3\2\2\2\f9\3\2\2\2\16=\3\2\2\2\20T\3\2\2\2\22Z\3\2\2\2\24"+
		"\\\3\2\2\2\26l\3\2\2\2\30t\3\2\2\2\32\u0089\3\2\2\2\34\u008d\3\2\2\2\36"+
		"\u00a3\3\2\2\2 \u00ad\3\2\2\2\"\u00cc\3\2\2\2$\u00de\3\2\2\2&\u00fe\3"+
		"\2\2\2(\u0100\3\2\2\2*\u0104\3\2\2\2,\u012b\3\2\2\2./\7\3\2\2/\3\3\2\2"+
		"\2\60\61\7\4\2\2\61\5\3\2\2\2\62\63\t\2\2\2\63\7\3\2\2\2\64\65\t\3\2\2"+
		"\65\t\3\2\2\2\66\67\t\4\2\2\67\13\3\2\2\28:\5\16\b\298\3\2\2\2:;\3\2\2"+
		"\2;9\3\2\2\2;<\3\2\2\2<\r\3\2\2\2=>\7\3\2\2>A\5\6\4\2?@\7\4\2\2@B\5\6"+
		"\4\2A?\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\67\2\2DE\5\20\t\2EF\78\2\2FG\7"+
		"\61\2\2G\17\3\2\2\2HJ\5\22\n\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2"+
		"LU\3\2\2\2MK\3\2\2\2NP\5(\25\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2"+
		"RU\3\2\2\2SQ\3\2\2\2TK\3\2\2\2TQ\3\2\2\2U\21\3\2\2\2V[\5\24\13\2W[\5\30"+
		"\r\2X[\5&\24\2Y[\5\26\f\2ZV\3\2\2\2ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[\23"+
		"\3\2\2\2\\]\7\37\2\2]^\7\62\2\2^a\5\6\4\2_`\7/\2\2`b\5,\27\2a_\3\2\2\2"+
		"ab\3\2\2\2bh\3\2\2\2cd\7\65\2\2de\5,\27\2ef\7\61\2\2fg\7\66\2\2gi\3\2"+
		"\2\2hc\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\7\61\2\2k\25\3\2\2\2lm\7\37\2\2m"+
		"p\7/\2\2nq\5,\27\2oq\5&\24\2pn\3\2\2\2po\3\2\2\2qr\3\2\2\2rs\7\61\2\2"+
		"s\27\3\2\2\2tu\7\37\2\2uw\7\65\2\2vx\5*\26\2wv\3\2\2\2wx\3\2\2\2xy\3\2"+
		"\2\2yz\7\66\2\2z{\7\62\2\2{|\5\6\4\2|\u0082\7\67\2\2}\u0081\5$\23\2~\u0081"+
		"\5\30\r\2\177\u0081\5&\24\2\u0080}\3\2\2\2\u0080~\3\2\2\2\u0080\177\3"+
		"\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083"+
		"\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\5\32\16\2\u0086\u0087\7"+
		"8\2\2\u0087\u0088\7\61\2\2\u0088\31\3\2\2\2\u0089\u008a\7\16\2\2\u008a"+
		"\u008b\5,\27\2\u008b\u008c\7\61\2\2\u008c\33\3\2\2\2\u008d\u008e\7\17"+
		"\2\2\u008e\u0093\5\36\20\2\u008f\u0090\7\63\2\2\u0090\u0092\5\36\20\2"+
		"\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094"+
		"\3\2\2\2\u0094\u00a1\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7\20\2\2"+
		"\u0097\u009d\7\67\2\2\u0098\u0099\5,\27\2\u0099\u009a\7\61\2\2\u009a\u009c"+
		"\3\2\2\2\u009b\u0098\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d"+
		"\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2\78"+
		"\2\2\u00a1\u0096\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\35\3\2\2\2\u00a3\u00a4"+
		"\7\37\2\2\u00a4\u00a5\7\62\2\2\u00a5\u00a8\5\6\4\2\u00a6\u00a7\7/\2\2"+
		"\u00a7\u00a9\5,\27\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00ab"+
		"\3\2\2\2\u00aa\u00ac\5\6\4\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac"+
		"\37\3\2\2\2\u00ad\u00ae\7\21\2\2\u00ae\u00b9\5,\27\2\u00af\u00b4\7\22"+
		"\2\2\u00b0\u00b3\5&\24\2\u00b1\u00b3\5$\23\2\u00b2\u00b0\3\2\2\2\u00b2"+
		"\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2"+
		"\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00af\3\2\2\2\u00b8"+
		"\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00c4\3\2"+
		"\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00c1\7\23\2\2\u00bd\u00c0\5&\24\2\u00be"+
		"\u00c0\5$\23\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\u00c3\3\2"+
		"\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3"+
		"\u00c1\3\2\2\2\u00c4\u00bc\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2"+
		"\2\2\u00c6\u00c8\5\32\16\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8"+
		"\u00c9\3\2\2\2\u00c9\u00ca\7\24\2\2\u00ca\u00cb\7\61\2\2\u00cb!\3\2\2"+
		"\2\u00cc\u00cd\7\25\2\2\u00cd\u00ce\5,\27\2\u00ce\u00d3\7\26\2\2\u00cf"+
		"\u00d2\5$\23\2\u00d0\u00d2\5&\24\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2"+
		"\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4"+
		"\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\7\27\2\2\u00d7\u00d8\7"+
		"\61\2\2\u00d8#\3\2\2\2\u00d9\u00df\5 \21\2\u00da\u00df\5\"\22\2\u00db"+
		"\u00df\5\34\17\2\u00dc\u00df\5\26\f\2\u00dd\u00df\5\24\13\2\u00de\u00d9"+
		"\3\2\2\2\u00de\u00da\3\2\2\2\u00de\u00db\3\2\2\2\u00de\u00dc\3\2\2\2\u00de"+
		"\u00dd\3\2\2\2\u00df%\3\2\2\2\u00e0\u00e1\7\37\2\2\u00e1\u00e3\7\65\2"+
		"\2\u00e2\u00e4\5,\27\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e9"+
		"\3\2\2\2\u00e5\u00e6\7\63\2\2\u00e6\u00e8\5,\27\2\u00e7\u00e5\3\2\2\2"+
		"\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec"+
		"\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\7\66\2\2\u00ed\u00ff\7\61\2\2"+
		"\u00ee\u00ef\7\37\2\2\u00ef\u00f0\7\64\2\2\u00f0\u00f1\7\37\2\2\u00f1"+
		"\u00f3\7\65\2\2\u00f2\u00f4\5,\27\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3"+
		"\2\2\2\u00f4\u00f9\3\2\2\2\u00f5\u00f6\7\63\2\2\u00f6\u00f8\5,\27\2\u00f7"+
		"\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2"+
		"\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7\66\2\2\u00fd"+
		"\u00ff\7\61\2\2\u00fe\u00e0\3\2\2\2\u00fe\u00ee\3\2\2\2\u00ff\'\3\2\2"+
		"\2\u0100\u0101\7\37\2\2\u0101\u0102\7\62\2\2\u0102\u0103\5\6\4\2\u0103"+
		")\3\2\2\2\u0104\u0109\5(\25\2\u0105\u0106\7\63\2\2\u0106\u0108\5(\25\2"+
		"\u0107\u0105\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a"+
		"\3\2\2\2\u010a+\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d\b\27\1\2\u010d"+
		"\u010e\7\37\2\2\u010e\u010f\7/\2\2\u010f\u012c\5,\27 \u0110\u012c\7!\2"+
		"\2\u0111\u012c\7 \2\2\u0112\u0113\7,\2\2\u0113\u012c\7\37\2\2\u0114\u0115"+
		"\7,\2\2\u0115\u012c\5\6\4\2\u0116\u0117\7-\2\2\u0117\u012c\5,\27\33\u0118"+
		"\u012c\7 \2\2\u0119\u012c\7!\2\2\u011a\u011b\7.\2\2\u011b\u012c\5,\27"+
		"\30\u011c\u011e\7\65\2\2\u011d\u011f\5,\27\2\u011e\u011d\3\2\2\2\u011f"+
		"\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\3\2"+
		"\2\2\u0122\u0123\7\66\2\2\u0123\u012c\3\2\2\2\u0124\u0125\7-\2\2\u0125"+
		"\u012c\5,\27\26\u0126\u012c\7\30\2\2\u0127\u012c\7\31\2\2\u0128\u012c"+
		"\7\32\2\2\u0129\u012c\7\33\2\2\u012a\u012c\7\37\2\2\u012b\u010c\3\2\2"+
		"\2\u012b\u0110\3\2\2\2\u012b\u0111\3\2\2\2\u012b\u0112\3\2\2\2\u012b\u0114"+
		"\3\2\2\2\u012b\u0116\3\2\2\2\u012b\u0118\3\2\2\2\u012b\u0119\3\2\2\2\u012b"+
		"\u011a\3\2\2\2\u012b\u011c\3\2\2\2\u012b\u0124\3\2\2\2\u012b\u0126\3\2"+
		"\2\2\u012b\u0127\3\2\2\2\u012b\u0128\3\2\2\2\u012b\u0129\3\2\2\2\u012b"+
		"\u012a\3\2\2\2\u012c\u0189\3\2\2\2\u012d\u012e\f\13\2\2\u012e\u012f\7"+
		"\13\2\2\u012f\u0188\5,\27\f\u0130\u0131\f\5\2\2\u0131\u0132\7\36\2\2\u0132"+
		"\u0188\5,\27\6\u0133\u0134\f\4\2\2\u0134\u0135\7\n\2\2\u0135\u0188\5,"+
		"\27\5\u0136\u0137\f\21\2\2\u0137\u0138\7\f\2\2\u0138\u0139\5\6\4\2\u0139"+
		"\u013a\7\64\2\2\u013a\u013b\7\37\2\2\u013b\u013c\7\65\2\2\u013c\u0141"+
		"\5,\27\2\u013d\u013e\7\61\2\2\u013e\u0140\5,\27\2\u013f\u013d\3\2\2\2"+
		"\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144"+
		"\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7\66\2\2\u0145\u0188\3\2\2\2"+
		"\u0146\u0147\f\20\2\2\u0147\u0188\7\r\2\2\u0148\u014b\f\17\2\2\u0149\u014a"+
		"\7\6\2\2\u014a\u014c\5,\27\2\u014b\u0149\3\2\2\2\u014c\u014d\3\2\2\2\u014d"+
		"\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0188\3\2\2\2\u014f\u0152\f\16"+
		"\2\2\u0150\u0151\7\5\2\2\u0151\u0153\5,\27\2\u0152\u0150\3\2\2\2\u0153"+
		"\u0154\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0188\3\2"+
		"\2\2\u0156\u0159\f\r\2\2\u0157\u0158\7\t\2\2\u0158\u015a\5,\27\2\u0159"+
		"\u0157\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2"+
		"\2\2\u015c\u0188\3\2\2\2\u015d\u0160\f\f\2\2\u015e\u015f\7\34\2\2\u015f"+
		"\u0161\5,\27\2\u0160\u015e\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0160\3\2"+
		"\2\2\u0162\u0163\3\2\2\2\u0163\u0188\3\2\2\2\u0164\u0167\f\n\2\2\u0165"+
		"\u0166\7\5\2\2\u0166\u0168\5,\27\2\u0167\u0165\3\2\2\2\u0168\u0169\3\2"+
		"\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0188\3\2\2\2\u016b"+
		"\u016e\f\t\2\2\u016c\u016d\7\6\2\2\u016d\u016f\5,\27\2\u016e\u016c\3\2"+
		"\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171"+
		"\u0188\3\2\2\2\u0172\u0175\f\b\2\2\u0173\u0174\7\7\2\2\u0174\u0176\5,"+
		"\27\2\u0175\u0173\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177"+
		"\u0178\3\2\2\2\u0178\u0188\3\2\2\2\u0179\u017c\f\7\2\2\u017a\u017b\7\b"+
		"\2\2\u017b\u017d\5,\27\2\u017c\u017a\3\2\2\2\u017d\u017e\3\2\2\2\u017e"+
		"\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0188\3\2\2\2\u0180\u0183\f\6"+
		"\2\2\u0181\u0182\7\35\2\2\u0182\u0184\5,\27\2\u0183\u0181\3\2\2\2\u0184"+
		"\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188\3\2"+
		"\2\2\u0187\u012d\3\2\2\2\u0187\u0130\3\2\2\2\u0187\u0133\3\2\2\2\u0187"+
		"\u0136\3\2\2\2\u0187\u0146\3\2\2\2\u0187\u0148\3\2\2\2\u0187\u014f\3\2"+
		"\2\2\u0187\u0156\3\2\2\2\u0187\u015d\3\2\2\2\u0187\u0164\3\2\2\2\u0187"+
		"\u016b\3\2\2\2\u0187\u0172\3\2\2\2\u0187\u0179\3\2\2\2\u0187\u0180\3\2"+
		"\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a"+
		"-\3\2\2\2\u018b\u0189\3\2\2\2\61;AKQTZahpw\u0080\u0082\u0093\u009d\u00a1"+
		"\u00a8\u00ab\u00b2\u00b4\u00b9\u00bf\u00c1\u00c4\u00c7\u00d1\u00d3\u00de"+
		"\u00e3\u00e9\u00f3\u00f9\u00fe\u0109\u0120\u012b\u0141\u014d\u0154\u015b"+
		"\u0162\u0169\u0170\u0177\u017e\u0185\u0187\u0189";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
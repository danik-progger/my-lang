// Generated from /home/dan/Desktop/dev/mipt/my-lang/antlr/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		SPACES=10, FUN=11, MAIN=12, NEWLINE=13, INT=14, PRINT=15, IF=16, ELSE=17, 
		WHILE=18, IDENT=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"SPACES", "FUN", "MAIN", "NEWLINE", "INT", "PRINT", "IF", "ELSE", "WHILE", 
			"IDENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'='", "'*'", "'/'", "'+'", "'-'", 
			null, "'fun'", "'main'", null, null, "'print '", "'if '", "'else'", "'while'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "SPACES", 
			"FUN", "MAIN", "NEWLINE", "INT", "PRINT", "IF", "ELSE", "WHILE", "IDENT"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0013k\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f"+
		"\u0004\fH\b\f\u000b\f\f\fI\u0001\r\u0004\rM\b\r\u000b\r\f\rN\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0004\u0012h\b\u0012"+
		"\u000b\u0012\f\u0012i\u0000\u0000\u0013\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\u0001\u0000\u0004\u0002\u0000\t\t  \u0002\u0000\n\n\r\r"+
		"\u0001\u000009\u0002\u0000AZazm\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000"+
		"\u0000\u0000%\u0001\u0000\u0000\u0000\u0001\'\u0001\u0000\u0000\u0000"+
		"\u0003)\u0001\u0000\u0000\u0000\u0005+\u0001\u0000\u0000\u0000\u0007-"+
		"\u0001\u0000\u0000\u0000\t/\u0001\u0000\u0000\u0000\u000b1\u0001\u0000"+
		"\u0000\u0000\r3\u0001\u0000\u0000\u0000\u000f5\u0001\u0000\u0000\u0000"+
		"\u00117\u0001\u0000\u0000\u0000\u00139\u0001\u0000\u0000\u0000\u0015="+
		"\u0001\u0000\u0000\u0000\u0017A\u0001\u0000\u0000\u0000\u0019G\u0001\u0000"+
		"\u0000\u0000\u001bL\u0001\u0000\u0000\u0000\u001dP\u0001\u0000\u0000\u0000"+
		"\u001fW\u0001\u0000\u0000\u0000![\u0001\u0000\u0000\u0000#`\u0001\u0000"+
		"\u0000\u0000%g\u0001\u0000\u0000\u0000\'(\u0005(\u0000\u0000(\u0002\u0001"+
		"\u0000\u0000\u0000)*\u0005)\u0000\u0000*\u0004\u0001\u0000\u0000\u0000"+
		"+,\u0005{\u0000\u0000,\u0006\u0001\u0000\u0000\u0000-.\u0005}\u0000\u0000"+
		".\b\u0001\u0000\u0000\u0000/0\u0005=\u0000\u00000\n\u0001\u0000\u0000"+
		"\u000012\u0005*\u0000\u00002\f\u0001\u0000\u0000\u000034\u0005/\u0000"+
		"\u00004\u000e\u0001\u0000\u0000\u000056\u0005+\u0000\u00006\u0010\u0001"+
		"\u0000\u0000\u000078\u0005-\u0000\u00008\u0012\u0001\u0000\u0000\u0000"+
		"9:\u0007\u0000\u0000\u0000:;\u0001\u0000\u0000\u0000;<\u0006\t\u0000\u0000"+
		"<\u0014\u0001\u0000\u0000\u0000=>\u0005f\u0000\u0000>?\u0005u\u0000\u0000"+
		"?@\u0005n\u0000\u0000@\u0016\u0001\u0000\u0000\u0000AB\u0005m\u0000\u0000"+
		"BC\u0005a\u0000\u0000CD\u0005i\u0000\u0000DE\u0005n\u0000\u0000E\u0018"+
		"\u0001\u0000\u0000\u0000FH\u0007\u0001\u0000\u0000GF\u0001\u0000\u0000"+
		"\u0000HI\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000"+
		"\u0000\u0000J\u001a\u0001\u0000\u0000\u0000KM\u0007\u0002\u0000\u0000"+
		"LK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000O\u001c\u0001\u0000\u0000\u0000PQ\u0005"+
		"p\u0000\u0000QR\u0005r\u0000\u0000RS\u0005i\u0000\u0000ST\u0005n\u0000"+
		"\u0000TU\u0005t\u0000\u0000UV\u0005 \u0000\u0000V\u001e\u0001\u0000\u0000"+
		"\u0000WX\u0005i\u0000\u0000XY\u0005f\u0000\u0000YZ\u0005 \u0000\u0000"+
		"Z \u0001\u0000\u0000\u0000[\\\u0005e\u0000\u0000\\]\u0005l\u0000\u0000"+
		"]^\u0005s\u0000\u0000^_\u0005e\u0000\u0000_\"\u0001\u0000\u0000\u0000"+
		"`a\u0005w\u0000\u0000ab\u0005h\u0000\u0000bc\u0005i\u0000\u0000cd\u0005"+
		"l\u0000\u0000de\u0005e\u0000\u0000e$\u0001\u0000\u0000\u0000fh\u0007\u0003"+
		"\u0000\u0000gf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ig\u0001"+
		"\u0000\u0000\u0000ij\u0001\u0000\u0000\u0000j&\u0001\u0000\u0000\u0000"+
		"\u0004\u0000INi\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
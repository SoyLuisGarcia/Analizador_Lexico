import ply.lex as lex

# Resultado del análisis
resultado_lexema = []

counts = {
    'RESERVADO': 0,
    'IDENTIFICADOR': 0,
    'DELIMITADOR': 0,
    'OPERADOR': 0,
    'NUMERO': 0,
    'SIMBOLO': 0
}

reservada = (
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'GET',
    'RETURN',
    'VOID',
    'INT',
    'ENDL',
    'FOR',  # Agregar 'FOR' como palabra reservada
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNAR',
    'SYSTEM',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

    'MINUSMINUS',
    'PLUSPLUS',

    # Condiciones
    'SI',
    'SINO',
    # Ciclos
    'MIENTRAS',
    'RESERVADA',
    # Lógica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DISTINTO',
    # Símbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',

    # Otros
    'PUNTOCOMA',
    'PUNTO',
    'DOSPUNTO',

    'COMDOB',
    'MAYORDER',  
    'MAYORIZQ', 
)

# Reglas de Expresiones Regulares para token de Contexto simple

t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
# t_PUNTO = r'\.'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*\*|\^)'

t_ASIGNAR = r'='
# Expresiones Lógicas
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = r';'
t_PUNTO = r'\.'
t_DOSPUNTO = r'\:'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMDOB = r'\"'


def t_INCLUDE(t):
    r'include'
    return t


def t_USING(t):
    r'using'
    return t


def t_SYSTEM(t):
    r'System'
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_STD(t):
    r'std'
    return t


def t_GET(t):
    r'get'
    return t


def t_ENDL(t):
    r'endl'
    return t


def t_SINO(t):
    r'else'
    return t


def t_SI(t):
    r'if'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_VOID(t):
    r'void'
    return t


def t_MIENTRAS(t):
    r'while'
    return t


def t_RESERVADA(t):
    r'for'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t


def t_NUMERAL(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUAL(t):
    r'=='
    return t


def t_MAYORDER(t):
    r'<<'
    return t


def t_MAYORIZQ(t):
    r'>>'
    return t


def t_DISTINTO(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de múltiple línea")


def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una línea")


t_ignore = ' \t'


def t_error(t):
    global resultado_lexema
    estado = "** Token no válido en la Línea {:4} Valor {:16} Posición {:4}".format(str(t.lineno), str(t.value),
                                                                                    str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


    # Contador de categorías
def categorizar_token(tipo):
    if tipo in reservada:
        counts['RESERVADO'] += 1
    elif tipo == 'IDENTIFICADOR':
        counts['IDENTIFICADOR'] += 1
    elif tipo in ('SUMA', 'RESTA', 'MULT', 'DIV', 'POTENCIA', 'MODULO', 'ASIGNAR'):
        counts['OPERADOR'] += 1
    elif tipo in ('PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER', 'PUNTOCOMA'):
        counts['DELIMITADOR'] += 1
    elif tipo == 'ENTERO':
        counts['NUMERO'] += 1
    elif tipo == 'PUNTO':
        counts['SIMBOLO'] += 1

   # Inicializar contadores
counts = {
    'RESERVADO': 0,
    'IDENTIFICADOR': 0,
    'DELIMITADOR': 0,
    'OPERADOR': 0,
    'NUMERO': 0,
    'SIMBOLO': 0  # Contador para el token de símbolos (punto)
}


# Prueba de ingreso
def prueba(data):
    global resultado_lexema,counts


    # Reiniciar los contadores
    counts = {key: 0 for key in counts}

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Línea {:1} Tipo {:15} Valor {:4} Posición {:2}".format(str(tok.lineno), str(tok.type),
                                                                          str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema, counts 


# Instanciamos el analizador léxico
analizador = lex.lex()

if __name__ == '__main__':
    while True:
        data = input('''for(int i = 1; i <= 10; i++) {
  System.out.println("Número:" + i);
} ''')
        prueba(data)
        print(resultado_lexema)
        print (counts)
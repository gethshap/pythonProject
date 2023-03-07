# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import graphviz
debug = True
def print_hi(name):
    fo = open("foo.txt", "w")
    print("文件名: ", fo.name)
    print("是否已关闭 : ", fo.closed)
    print("访问模式 : ", fo.mode)
    print("末尾是否强制加空格 : ", fo.softspace)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class fileReader:

    def __init__(self, fn):
        self.file = None
        self.file_open(fn)

    def file_open(self, fn):
        self.file = open(fn, "r+")

    def getNext(self):
        char = self.file.read(1)
        if char is None:
            self.err("EOF")
        return char

    def err(self, err_message):
        print(err_message)


class token:

    def __init__(self, v, txt, tt, nv):
        self.value = v
        self.text = txt
        self.tokentype = tt
        self.number_vale = nv


class tokenizer:
    value2else = {1: ("timesToken", "*"),
                  2: ("divToken", "/"),
                  11: ("plusToken", "+"),
                  12: ("minusToken", "-"),
                  20: ("eqlToken", "=="),
                  21: ("neqToken", "!="),
                  22: ("lssToken", "!="),
                  23: ("geqToken", "!="),
                  24: ("leqToken", "!="),
                  25: ("gtrToken", "!="),
                  30: ("periodToken", "!="),
                  31: ("commaToken", "!="),
                  32: ("openbracketToken ", "!="),
                  34: ("closebracketToken ", "!="),
                  35: ("closeparenToken", "!="),
                  40: ("becomesToken", "!="),
                  41: ("thenToken", "!="),
                  42: ("doToken", "!="),
                  50: ("doToken", "!="),
                  60: ("number", "!="),
                  }

    def __init__(self, fn):
        self.fr = fileReader(fn)
        self.inputSystem = self.fr.getNext()

    def next(self):
        next_char = self.fr.getNext()
        self.inputSystem = next_char
        return next_char

    def error(self, msg):
        print(msg)

    def getNext(self):
        while self.inputSystem == ' ' or self.inputSystem=='\n':
            self.next()

        str = self.inputSystem
        if str == '':
            self.next()
            return token(255, '', 'eofToken', None)
        elif str == '*':
            self.next()
            return token(1, '*', 'timesToken', None)
        elif str == '/':
            self.next()
            return token(2, '/', 'divToken', None)
        elif str == '-':
            self.next()
            return token(12, '-', 'minusToken', None)
        elif str == '+':
            self.next()
            return token(11, '+', 'plusToken', None)
        elif str == '=':
            self.next()
            if self.inputSystem == '=':
                self.next()
                return token(20, '==', 'eqlToken', None)
            else:
                self.next()
                return token(0, '', 'errorToken', None)
        elif str == '!':
            self.next()
            if self.inputSystem == '=':
                self.next()
                return token(21, '!=', 'neqToken', None)
            else:
                self.next()
                return token(0, '', 'errorToken', None)
        elif str == '<':
            self.next()
            if self.inputSystem == '=':
                self.next()
                return token(24, '<=', 'leqToken', None)
            elif self.inputSystem == '-':
                self.next()
                return token(40, '<-', 'becomesToken', None)
            elif self.inputSystem == ' ':
                self.next()
                return token(22, '<', 'lssToken', None)

            else:
                return token(0, '', 'errorToken', None)

        elif str == '>':
            self.next()
            if self.inputSystem == '=':
                self.next()
                return token(23, '>=', 'geqToken', None)
            elif self.inputSystem == ' ':
                self.next()
                return token(25, '>', 'gtrToken', None)
            else:
                self.next()
                return token(0, '', 'errorToken', None)
        elif str == '.':
            self.next()
            return token(30, '.', 'periodToken', None)
        elif str == ',':
            self.next()
            return token(31, ',', 'commaToken', None)
        elif str == '[':
            self.next()
            return token(32, '[', 'openbracketToken', None)
        elif str == ']':
            self.next()
            return token(34, ']', 'closebracketToken', None)
        elif str == ')':
            self.next()
            return token(35, ')', 'closeparenToken', None)
        elif str == '(':
            self.next()
            return token(50, '(', 'openparenToken', None)
        elif str == ';':
            self.next()
            return token(70, ';', 'semiToken', None)
        elif str == '}':
            self.next()
            return token(80, '}', 'endToken', None)
        elif str == '{':
            self.next()
            return token(150, '{', 'beginToken', None)


        while str.isdigit():
            self.next()
            str += self.inputSystem
        if self.inputSystem == ' ':
            return token(60, str, 'number', int(str))

        if str.isalpha():
            self.next()
            while self.inputSystem.isalpha() or self.inputSystem.isdigit():
                str += self.inputSystem
                self.next()
        if self.inputSystem == ' ' or self.inputSystem == '\n':

                if str == 'then':
                    return token(41, 'then', 'thenToken', None)
                elif str == 'do':
                    return token(42, 'do', 'doToken', None)
                elif str == 'od':
                    return token(81, 'od', 'odToken', None)
                elif str == 'fi':
                    return token(82, 'fi', 'fiToken', None)
                elif str == 'else':
                    return token(90, 'else', 'elseToken', None)
                elif str == 'let':
                    return token(100, 'let', 'letToken', None)
                elif str == 'call':
                    return token(101, 'call', 'callToken', None)
                elif str == 'if':
                    return token(102, 'if', 'ifToken', None)
                elif str == 'while':
                    return token(103, 'while', 'whileToken', None)
                elif str == 'return':
                    return token(104, 'return', 'returnToken', None)
                elif str == 'var':
                    return token(110, 'var', 'varToken', None)
                elif str == 'array':
                    return token(111, 'array', 'arrToken', None)
                elif str == 'void':
                    return token(112, 'void', 'voidToken', None)
                elif str == 'function':
                    return token(113, 'function', 'funcToken', None)
                elif str =='procedure':
                    return token(114, 'procedure', 'procToken', None)
                elif str == 'main':
                    return token(200, 'main', 'mainToken', None)

        if str == '':
            return token(255, '', 'eofToken', None)
        return token(61, str, 'ident', None)


class Parser:
    def __init__(self, fn):
        self.mytk = tokenizer(fn)
        self.inputSym = self.mytk.getNext()

    def next(self):
        self.inputSym = self.mytk.getNext()

    self.ssa_space = []
    self.var_space = []
    self.constant_space = []

    def ir_create(self):
        None

    def checkFor(self, tkt, test=False, debug=True):
        if tkt == self.inputSym.tokentype:
            if debug == True and test == False:
                print(tkt +"  "+ str(self.inputSym.value)+"  "+ str(self.inputSym.number_vale)+"    "+self.inputSym.text)
            if test == False:
                self.next()
            return True

        else:
            if test == False:
                self.mytk.error("syntaxError")
                return False
            else:
                return False


    def number(self):
        self.checkFor('number')

    def assignment(self):
        self.checkFor('letToken')
        self.designator()
        self.checkFor('becomesToken')
        self.expression()

    def relation(self):
        self.expression()
        self.relOp()
        self.expression()

    def relOp(self):
        if self.checkFor('eqlToken',test=True):
            self.checkFor('eqlToken')
        elif self.checkFor('neqToken',test=True):
            self.checkFor('neqToken')
        elif  self.checkFor('lssToken',test=True):
            self.checkFor('lssToken')
        elif self.checkFor('leqToken',test=True) :
            self.checkFor('leqToken')
        elif self.checkFor('gtrToken',test=True):
            self.checkFor('gtrToken')
        elif self.checkFor('geqToken',test=True):
            self.checkFor('geqToken')



    def funcCall(self):
        self.checkFor("callToken")
        self.checkFor('ident')
        if self.checkFor('openparenToken'):
            self.expression()
            while self.checkFor('commaToken',test=True):
                self.checkFor('commaToken')
                self.expression()
            self.checkFor('closeparenToken')



    def factor(self):
        if self.checkFor('ident',test=True):
            self.designator()
        elif  self.checkFor('number',test=True):
            self.number()
        elif self.checkFor('openparenToken',test=True):
            self.checkFor('openparenToken')
            self.expression()
            self.checkFor('closeparenToken')
        elif self.checkFor('callToken',test=True):
            self.funcCall()

    def statSequence(self):
        None

    def ifStatement(self):
        self.checkFor('ifToken')
        self.relation()
        self.checkFor('thenToken')
        self.statSequence()
        while self.checkFor("elseToken",test=True):
            self.checkFor("elseToken")
            self.statSequence()
        self.checkFor("fiToken")


    def whileStatement(self):
        self.checkFor('whileToken')
        self.relation()
        self.checkFor("doToken")
        self.statSequence()
        self.checkFor("odToken")





    def term(self):
        self.factor()
        while self.checkFor('timesToken',test=True) or self.checkFor('divToken',test=True):
            self.next()
            self.factor()

    def expression(self):
        self.term()
        while self.checkFor('plusToken',test=True) or self.checkFor('minusToken',test=True):
            self.next()
            self.term()


    def designator(self):
        self.checkFor('ident')
        while self.checkFor('openbracketToken',test=True):
            self.checkFor('openbracketToken')
            self.expression()
            self.checkFor('closebracketToken')



    def typeDecl(self):
        if self.checkFor("varToken"):
            return "var"
        elif self.checkFor("arrToken"):
            self.checkFor("openbracketToken")
            self.checkFor("number")
            self.checkFor("closebracketToken")
            while self.checkFor("openbracketToken", test=True):
                self.checkFor("openbracketToken")
                self.checkFor("number")
                self.checkFor("closebracketToken")
            return "array"

    def varDecl(self):
        if(self.typeDecl()=='var'):
            None
        self.checkFor("ident")
        while self.checkFor("commaToken", test=True):
            self.checkFor("commaToken")
            self.checkFor("ident")
        self.checkFor("semiToken")

    def returnStatement(self):
        self.checkFor("returnToken")
        if self.checkFor('ident',test=True) or self.checkFor('number',test=True) or self.checkFor('openparenToken',test=True) or self.checkFor('callToken',test=True):
            self.expression()




    def statement(self):
        if self.checkFor("letToken",test=True):
            self.assignment()
        elif self.checkFor("callToken",test=True):
            self.funcCall()
        elif self.checkFor("ifToken",test=True):
            self.ifStatement()
        elif self.checkFor("whileToken",test=True):
            self.whileStatement()
        elif self.checkFor("returnToken",test=True):
            self.returnStatement()

    def statSequence(self):
        self.statement()
        while self.checkFor('semiToken',test = True):
            self.checkFor('semiToken')
            self.statement()
        if self.checkFor('semiToken',test = True):
            self.checkFor('semiToken')

    def formalParam(self):
        self.checkFor('openparenToken')
        if self.checkFor("ident",test = True):
            self.checkFor("ident")
            while self.checkFor("commaToken",test = True):
                self.checkFor("commaToken")
                self.checkFor("ident")

    def funcBody(self):
        None

    def funcDecl(self):
        if self.checkFor("voidToken",test = True):
            self.checkFor("voidToken")
        self.checkFor("funcToken")
        self.checkFor("ident")
        None



    def Parse(self):
        self.checkFor('mainToken')  # main
        self.varDecl()
        self.checkFor('beginToken')
        self.checkFor('endToken')
        self.checkFor('periodToken')  # .


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myp = Parser('foo.txt')
    cp = Parser('foo.txt')
    a = []
    for i in range(9):
        a.append(cp.inputSym)
        cp.next()
    myp.Parse()

    b = 6

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

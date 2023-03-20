# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import graphviz
from graphviz import Digraph
import copy
debug = True
'''
s = Digraph('struct',filename="control_flow_graph",node_attr={'shape':'record'})
s.node('struct1', ' left| middle| right')
s.node('struct2', ' one| two')
s.node('struct3', r'hello\nworld |{ b |{c| d|e}| f}| g | h')
s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])
s.view()
'''




def print_graph(name):
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
        while self.inputSystem == ' ' or self.inputSystem == '\n':
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

        if (str.isdigit()):
            self.next()
            while self.inputSystem.isdigit():
                str += self.inputSystem
                self.next()
            return token(60, str, 'number', int(str))

        if str.isalpha():
            self.next()
            while self.inputSystem.isalpha() or self.inputSystem.isdigit():
                str += self.inputSystem
                self.next()
        if self.inputSystem == ' ' or self.inputSystem == '\n' or self.inputSystem == ';':

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
            elif str == 'procedure':
                return token(114, 'procedure', 'procToken', None)
            elif str == 'main':
                return token(200, 'main', 'mainToken', None)

        if str == '':
            return token(255, '', 'eofToken', None)
        return token(61, str, 'ident', None)


class ssa_line:
    const = None
    const_value = None

    ssa_line_source_1 = None
    ssa_line_source_2 = None
    op = None
    ssa_line_target = None

    def __init__(self, ssa_line_target, ssa_line_source_1, ssa_line_source_2, op):
        if op == None:
            self.const = True
            self.const_value = ssa_line_target
        else:
            self.ssa_line_source_1 = ssa_line_source_1
            self.ssa_line_source_2 = ssa_line_source_2
            self.op = op
            self.ssa_line_target = ssa_line_target

    def to_tuple(self):
        return (self.ssa_line_source_1, self.ssa_line_source_2, self.op)


class Basic_block:
    block_number = None
    dom_block_number = None
    fall_through = None
    branch = None
    next_block = None
    ssa_lines = []
    first_ssa_line_number = None
    ssa_lookup_table = {}
    var_space = {}
    previous = []

    def __init__(self, bn, dbn, ft, branch, next_block, slt,vs,var_space_db_end):
        self.block_number = bn
        self.dom_block_number = dbn
        self.fall_through = ft
        self.branch = branch
        self.next_block = next_block
        self.ssa_lookup_table = copy.deepcopy(slt)
        self.ssa_lookup_table_initial = copy.deepcopy(self.ssa_lookup_table)
        self.var_space = {}
        self.var_space_end = {}
        self.ssa_lines=[]


"""
s = Digraph('struct',filename="control_flow_graph",node_attr={'shape':'record'})
s.node('struct1', ' left| middle| right')
s.node('struct2', ' one| two')
s.node('struct3', r'hello\nworld |{ b |{c| d|e}| f}| g | h')
s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])
s.view()
"""




class Parser:
    def __init__(self, fn):
        self.mytk = tokenizer(fn)
        self.inputSym = self.mytk.getNext()

    def next(self):
        self.inputSym = self.mytk.getNext()

    block_count = 0
    block_collection = {}
    ssa_count = 1

    constant_space = {}

    current_block = None

    def dot_graph(self,name):
        s = Digraph('struct', filename=name, node_attr={'shape': 'record'})
        for block_number,block in self.block_collection.items():
            layout_text = "BB "+str(block_number) +" | {"
            for line in block.ssa_lines:
                if len(line) == 2:
                    layout_text =  layout_text  + str(line[0]) +": const" + " " + str(line [1]) +" |"
                else:
                    layout_text = layout_text + str(line[0])+ ": " + str(line [3]) + " "+str(line [1])+ " " +str(line [2]) + "    line_a: "  +str(line [6]) +"    line_b: "+ str(line [7])+" |"
            if layout_text[-1] == "|":
                layout_text = layout_text[:-1]
            layout_text = layout_text + "}"


            if block.var_space:
                layout_text = layout_text + "| {"
                for key, val in block.var_space.items():
                    layout_text = layout_text + str(key) + " : " + str(val) + '|'
            if layout_text[-1] == "|":
                layout_text = layout_text[:-1]
            layout_text = layout_text + "}"


            """
            if block.var_space:
                layout_text = layout_text + "| {"
                for key, val in block.var_space_begin.items():
                    layout_text = layout_text + str(key) + " : " + str(val) + '|'
            if layout_text[-1] == "|":
                layout_text = layout_text[:-1]
            layout_text = layout_text + "}"

            if block.var_space:
                layout_text = layout_text + "| {"
                for key, val in block.var_space_end.items():
                    layout_text = layout_text + str(key) + " : " + str(val) + '|'
            if layout_text[-1] == "|":
                layout_text = layout_text[:-1]
            layout_text = layout_text + "}"
            
            """


            if block.var_space:
                layout_text = layout_text + "| {"
                for key, val in block.var_space_end.items():
                    layout_text = layout_text + str(key) + " : " + str(val) + '|'
            if layout_text[-1] == "|":
                layout_text = layout_text[:-1]
            layout_text = layout_text + "}"





            s.node(str(block_number) ,layout_text)
        for block_number, block in self.block_collection.items():
            next_block = self.block_collection[block_number].next_block
            ft = self.block_collection[block_number].fall_through
            branch = self.block_collection[block_number].branch
            dbn = self.block_collection[block_number].dom_block_number
            if next_block != None:
                s.edge(str(block_number),str(next_block))
            if ft != None:
                s.edge(str(block_number),str(ft),label = "fall_through")
            if branch != None:
                s.edge(str(block_number),str(branch ),label = "branch")
            if dbn != None:
                s.edge(str(dbn), str(block_number), label="dom",color="blue")


        s.view()
        None






    def create_block(self, dbn, ft, branch, next_block, slt,vs):
        b = None
        if dbn == None:
            b = Basic_block(self.block_count, dbn, ft, branch, next_block, slt, vs,
                            {})
        else:
            b = Basic_block(self.block_count,dbn, ft, branch, next_block, slt,vs,var_space_db_end=self.block_collection[dbn].var_space_end)
        self.block_collection[self.block_count] = b
        r = self.block_count
        self.block_count = self.block_count + 1
        return r

    def update_line_to_block(self,bn):
        None
    def write_line_to_block(self,bn,ssa_line_const, ssa_line_source_1, ssa_line_source_2, op,front=False,replace=False,is_designator_1 =False,is_designator_2 =False,text_1=None,text_2=None):
        if ssa_line_const != None:
            r = ssa_line(ssa_line_const, ssa_line_source_1, ssa_line_source_2, op)
            r = r.to_tuple()

            self.block_collection[bn].ssa_lines.append((self.ssa_count, ssa_line_const))
            self.constant_space[ssa_line_const] = self.ssa_count
            r = self.ssa_count
            self.ssa_count = self.ssa_count + 1

            return r
        else:
            r = ssa_line(ssa_line_const, ssa_line_source_1, ssa_line_source_2, op)
            r = r.to_tuple()
            if front == False:
                self.block_collection[bn].ssa_lines.append((self.ssa_count,  ssa_line_source_1, ssa_line_source_2, op,is_designator_1,is_designator_2,text_1,text_2))
            else:
                self.block_collection[bn].ssa_lines.insert(0,(self.ssa_count, ssa_line_source_1, ssa_line_source_2, op,is_designator_1,is_designator_2,text_1,text_2))
            if op == "READ"  or op == None:
                r = self.ssa_count
                self.ssa_count = self.ssa_count + 1
                return r
            self.block_collection[bn].ssa_lookup_table[r] = self.ssa_count
            r = self.ssa_count
            self.ssa_count = self.ssa_count + 1

            return r


    def ssa_line(self, ssa_line_const, ssa_line_source_1, ssa_line_source_2, op):
        if op == None:
            r = ssa_line(ssa_line_const, ssa_line_source_1, ssa_line_source_2, op)
            r = r.to_tuple()
            self.ssa_lines.append(ssa_line_const)
            self.ssa_lookup_table[r] = self.ssa_count
            self.constant_space[ssa_line_const] = self.ssa_count
            r = self.ssa_count
            self.ssa_count = self.ssa_count + 1
            return r

        else:
            r = ssa_line(ssa_line_const, ssa_line_source_1, ssa_line_source_2, op)
            r = r.to_tuple()
            self.ssa_lines.append((op, ssa_line_source_1, ssa_line_source_2))
            self.ssa_lookup_table[r] = self.ssa_count
            self.constant_space[ssa_line_const] = self.ssa_count
            r = self.ssa_count
            self.ssa_count = self.ssa_count + 1
            return r

    def ssa_count_increase(self):
        cur = self.ssa_count
        self.ssa_count = self.ssa_count + 1
        return cur

    def ir_create(self, op2, get, ):
        self.ssa_space.append([])

    def checkFor(self, tkt, test=False, debug=True):

        if tkt == self.inputSym.tokentype:
            v, nv, t = self.inputSym.value, self.inputSym.number_vale, self.inputSym.text
            if debug == True and test == False:
                print(tkt + "  " + str(self.inputSym.value) + "  " + str(
                    self.inputSym.number_vale) + "    " + self.inputSym.text)
            if test == False:
                self.next()
            return True, v, nv, t


        else:
            if test == False:
                self.mytk.error("syntaxError" + "  expect " + tkt +" got " + self.inputSym.tokentype)
                return False
            else:
                return False

    def number(self):
        _, v, nv, t = self.checkFor('number')
        if nv in self.constant_space:
            return self.constant_space[nv]
        else:
            return self.write_line_to_block(0,nv,None,None,None)

    def assignment(self):
        self.checkFor('letToken')
        line_number_for_dst, text = self.designator()
        self.checkFor('becomesToken')
        line_number,is_d,text_1 = self.expression()
        self.block_collection[self.current_block].var_space[text] = line_number
        self.block_collection[self.current_block].var_space_end[text] = self.current_block

    def relation(self):
        line_a,is_d1,text_1 = self.expression()
        _, v, nv, t = self.relOp()
        line_b,is_d2,text_2 = self.expression()

        return v, self.write_line_to_block(self.current_block,None,line_a, line_b, "CMP",is_designator_1=is_d1,is_designator_2=is_d2,text_1=text_1,text_2=text_2)

    def relOp(self):
        if self.checkFor('eqlToken', test=True):
            return self.checkFor('eqlToken')
        elif self.checkFor('neqToken', test=True):
            return self.checkFor('neqToken')
        elif self.checkFor('lssToken', test=True):
            return self.checkFor('lssToken')
        elif self.checkFor('leqToken', test=True):
            return self.checkFor('leqToken')
        elif self.checkFor('gtrToken', test=True):
            return self.checkFor('gtrToken')
        elif self.checkFor('geqToken', test=True):
            return self.checkFor('geqToken')

    def funcCall(self):
        self.checkFor("callToken")
        bool0, value, number_value, text  = self.checkFor('ident')
        if text == "InputNum":
            if self.checkFor('openparenToken', test=True):
                self.checkFor('openparenToken')
                self.checkFor('closeparenToken')
            return self.write_line_to_block(self.current_block,None,None,None,"READ")


        if self.checkFor('openparenToken',test=True):
            self.checkFor('openparenToken')
            self.expression()
            while self.checkFor('commaToken', test=True):
                self.checkFor('commaToken')
                self.expression()
            self.checkFor('closeparenToken')

    def ifStatement(self):
        self.checkFor('ifToken')

        '''
        block_number = None
        dom_block_number = None
        fall_through = None
        branch = None
        next_block = None
        ssa_lines = []
        first_ssa_line_number = None
        ssa_lookup_table = {}
        var_space = {}
        '''
        dom_block = self.current_block
        ft_block_number = self.create_block(dom_block,None,None,None,self.block_collection[dom_block].ssa_lookup_table,
                                            self.block_collection[dom_block].var_space)
        self.block_collection[ft_block_number].previous.append(dom_block)
        branch_block_number = self.create_block(dom_block, None, None, None,
                                              self.block_collection[dom_block].ssa_lookup_table,
                                              self.block_collection[dom_block].var_space)
        self.block_collection[branch_block_number].previous.append(dom_block)
        exit_block_number = self.create_block(dom_block,None,None,None,self.block_collection[dom_block].ssa_lookup_table,
                                            self.block_collection[dom_block].var_space)
        self.block_collection[branch_block_number].previous.append(ft_block_number)
        self.block_collection[branch_block_number].previous.append(branch_block_number)
        front_block_number = None
        type, cmp_line = self.relation()

        self.checkFor('thenToken')
        branch_key = None

        if not self.block_collection[branch_block_number].ssa_lines:
            first_branch_line = self.write_line_to_block(branch_block_number, None, None, None, None)

        if type == 20:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BNE")
            branch_key = (cmp_line, first_branch_line, "BNE")
        if type == 21:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BEQ")
            branch_key = (cmp_line, first_branch_line, "BEQ")
        if type == 22:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BGE")
            branch_key = (cmp_line,first_branch_line, "BGE")
        if type == 23:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BLE")
            branch_key = (cmp_line, first_branch_line, "BLE")
        if type == 24:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BGT")
            branch_key = (cmp_line, first_branch_line, "BGE")
        if type == 25:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BLE")
            branch_key = (cmp_line, first_branch_line, "BLE")

        if self.block_collection[dom_block].branch != None:
            self.block_collection[exit_block_number].branch = self.block_collection[dom_block].branch
            self.block_collection[dom_block].branch = branch_block_number
        else:
            self.block_collection[dom_block].branch = branch_block_number

        if self.block_collection[dom_block].fall_through != None:
            self.block_collection[exit_block_number].fall_through = self.block_collection[dom_block].fall_through
            self.block_collection[dom_block].fall_through = ft_block_number
        else:
            self.block_collection[dom_block].fall_through = ft_block_number

        self.block_collection[branch_block_number].fall_through = exit_block_number
        self.block_collection[ft_block_number].branch = exit_block_number

        self.current_block = ft_block_number
        self.statSequence()
        if not self.block_collection[exit_block_number].ssa_lines:
            exit_first_line = self.write_line_to_block(exit_block_number,None,None,None,None)

        if not self.block_collection[ft_block_number].ssa_lines:
            self.write_line_to_block(ft_block_number,None,None,None,None)





        if  self.block_collection[exit_block_number].ssa_lines:
            branch_back = self.block_collection[exit_block_number]
            first_line_number =  self.block_collection[exit_block_number].ssa_lines[0][0]
            for key,val in self.block_collection.items():
                if  val.branch  == exit_block_number:
                    self.write_line_to_block(key, None, first_line_number, None, "BRA")






        if self.checkFor("elseToken", test=True):

            self.checkFor("elseToken")
            self.current_block = branch_block_number
            self.statSequence()
            if not self.block_collection[branch_block_number].ssa_lines:
                self.write_line_to_block(branch_block_number, None, None, None, None)
            first_line_number =  self.block_collection[branch_block_number].ssa_lines[0][0]
            branch_line_number = self.block_collection[dom_block].ssa_lines[-1][0]
            new_branch_line = (branch_line_number,cmp_line,first_line_number,branch_key[2],False,False)
            self.block_collection[dom_block].ssa_lines[-1] =new_branch_line



            self.block_collection[dom_block].ssa_lookup_table[(cmp_line,first_line_number,branch_key[2])] =branch_line_number
            self.block_collection[branch_block_number].ssa_lookup_table[(cmp_line,first_line_number,branch_key[2])] =branch_line_number
            self.block_collection[ft_block_number].ssa_lookup_table[(cmp_line,first_line_number,branch_key[2])] =branch_line_number
            self.block_collection[exit_block_number].ssa_lookup_table[(cmp_line,first_line_number,branch_key[2])] =branch_line_number



        self.current_block = exit_block_number
        ft_val =None
        branch_val = None

        for key, val in self.block_collection.items():
            if val.branch == exit_block_number:
                branch_before_exit = key
            elif val.fall_through == exit_block_number:
                ft_before_exit = key

        for key, val in self.block_collection[dom_block].var_space.items():
            ft_val = self.block_collection[ft_before_exit].var_space[key]
            branch_val = self.block_collection[branch_before_exit].var_space[key]
            if val != branch_val and val == ft_val:
                line_number = self.write_line_to_block(self.current_block, None,
                                                       branch_val, val,
                                                       'PHI')
                self.block_collection[exit_block_number].var_space[key] = line_number
                self.block_collection[exit_block_number].var_space_end[key]  = exit_block_number

            elif   val == branch_val and val != ft_val:
                line_number = self.write_line_to_block(self.current_block, None,
                                                       ft_val, val,
                                                       'PHI')
                self.block_collection[exit_block_number].var_space[key] = line_number
                self.block_collection[exit_block_number].var_space_end[key] = exit_block_number
            elif val != branch_val and val != ft_val:
                line_number = self.write_line_to_block(self.current_block, None,
                                                       branch_val, ft_val,
                                                       'PHI')
                self.block_collection[exit_block_number].var_space[key] = line_number
                self.block_collection[exit_block_number].var_space_end[key] = exit_block_number


        self.checkFor("fiToken")
        return exit_block_number


    def while_join_block_modifier(self,start_block,key_pairs,visited):


        if self.block_collection[start_block].next_block and self.block_collection[start_block].next_block not in visited:
            visited[start_block] = 1
            self.while_join_block_modifier(self.block_collection[start_block].next_block,key_pairs,visited)
        if self.block_collection[start_block].branch and self.block_collection[start_block].branch not in visited:
            visited[start_block] = 1
            self.while_join_block_modifier(self.block_collection[start_block].branch,key_pairs,visited)
        if self.block_collection[start_block].fall_through and self.block_collection[start_block].fall_through not in visited :
            visited[start_block] = 1
            self.while_join_block_modifier(self.block_collection[start_block].fall_through,key_pairs,visited)



        for key_pair in  key_pairs:
            ident = key_pair[0]
            source = key_pair[1]
            terget_line = key_pair[2]
            for i in range(len(self.block_collection[start_block].ssa_lines)):
                line_number = self.block_collection[start_block].ssa_lines[i][0]
                op = self.block_collection[start_block].ssa_lines[i][3]
                line_a = self.block_collection[start_block].ssa_lines[i][1]
                line_b = self.block_collection[start_block].ssa_lines[i][2]
                line_a_is_var = self.block_collection[start_block].ssa_lines[i][4]
                line_b_is_var = self.block_collection[start_block].ssa_lines[i][5]
                line_a_text = self.block_collection[start_block].ssa_lines[i][6]
                line_b_text = self.block_collection[start_block].ssa_lines[i][7]


                if op != None:
                    if op[0:3] != 'PHI':
                        if op != "READ":
                            del self.block_collection[start_block].ssa_lookup_table[(line_a, line_b, op)]
                if op != None and op != "READ":
                    if op[0:3] == 'PHI':
                        var_name = op[4:]
                        target = self.find_var_line_number_r(var_name, self.block_collection[start_block].dom_block_number)
                        line_a = target
                    else:
                        if line_a_text == ident:
                            if line_a_is_var:
                                line_a = self.find_var_line_number_r(ident,start_block)
                        if line_b_text == ident:
                            if line_b_is_var:
                                line_b = self.find_var_line_number_r(ident,start_block)







                if op != None and op != "READ":
                    self.block_collection[start_block].ssa_lines[i] = (
                        line_number, line_a, line_b, op, line_a_is_var, line_b_is_var, line_a_text, line_b_text)
                self.block_collection[start_block].ssa_lookup_table[(line_a, line_b, op)] = line_number







            #self.block_collection[start_block].var_space[ident] = line_number









    def whileStatement(self):
        dom_block = self.current_block

        join_block_number = self.create_block(dom_block, None, None, None,
                                              self.block_collection[dom_block].ssa_lookup_table,
                                              self.block_collection[dom_block].var_space)
        do_block_number = self.create_block(join_block_number, None, None, None,
                                            self.block_collection[dom_block].ssa_lookup_table,
                                            self.block_collection[dom_block].var_space)
        exit_block_number = self.create_block(join_block_number, None, None, None,
                                              self.block_collection[dom_block].ssa_lookup_table,
                                              self.block_collection[dom_block].var_space)

        if not self.block_collection[dom_block].ssa_lines:
            self.write_line_to_block(dom_block, None, None, None, None)

        self.block_collection[dom_block].next_block = join_block_number
        self.block_collection[join_block_number].fall_through = do_block_number
        self.block_collection[do_block_number].branch = join_block_number
        self.block_collection[join_block_number].branch = exit_block_number

        '''
        if self.block_collection[dom_block].branch != None:
            self.block_collection[exit_block_number].branch = self.block_collection[dom_block].branch
            self.block_collection[dom_block].branch = branch_block_number
        else:
            self.block_collection[dom_block].branch = branch_block_number
            
        if self.block_collection[dom_block].fall_through != None:
            self.block_collection[exit_block_number].fall_through = self.block_collection[dom_block].fall_through
            self.block_collection[dom_block].fall_through = ft_block_number
        else:
            self.block_collection[dom_block].fall_through = ft_block_number
        '''
        if self.block_collection[dom_block].branch:

            self.block_collection[exit_block_number].branch = self.block_collection[dom_block].branch
            self.block_collection[dom_block].branch = None

        if self.block_collection[dom_block].fall_through:

            self.block_collection[exit_block_number].fall_through = self.block_collection[dom_block].fall_through
            self.block_collection[dom_block].fall_through = None


        if not self.block_collection[exit_block_number].ssa_lines:
            self.write_line_to_block(exit_block_number,None,None,None,None)

        exit_first_line = self.block_collection[exit_block_number].ssa_lines[0][0]



        self.checkFor('whileToken')
        self.current_block = join_block_number
        type,cmp_line  = self.relation()



        branch_key = None
        if type == 20:
            self.write_line_to_block(self.current_block, None, cmp_line, exit_first_line, "BNE")
            branch_key = (cmp_line, exit_first_line, "BNE")
        if type == 21:
            self.write_line_to_block(self.current_block, None, cmp_line, exit_first_line, "BEQ")
            branch_key = (cmp_line, exit_first_line, "BEQ")
        if type == 22:
            self.write_line_to_block(self.current_block, None, cmp_line, exit_first_line, "BGE")
            branch_key = (cmp_line, exit_first_line, "BGE")
        if type == 23:
            self.write_line_to_block(self.current_block, None, cmp_line, exit_first_line, "BLE")
            branch_key = (cmp_line, exit_first_line, "BLE")
        if type == 24:
            self.write_line_to_block(self.current_block, None, cmp_line, exit_first_line, "BGT")
            branch_key = (cmp_line, exit_first_line, "BGE")
        if type == 25:
            self.write_line_to_block(self.current_block, None, cmp_line, exit_first_line, "BLE")
            branch_key = (cmp_line, exit_first_line, "BLE")



        self.checkFor("doToken")
        self.current_block = do_block_number

        key_need_to_update = []
        last_block = self.statSequence()

        modify_list = copy.deepcopy(self.block_collection[last_block].var_space)
        track_back = last_block
        while track_back != do_block_number:
            for key,line in self.block_collection[track_back].var_space.items():
                if key not in  modify_list:
                    modify_list[key]=line
            track_back = self.block_collection[track_back].dom_block_number
        for key,line in self.block_collection[do_block_number].var_space.items():
            if key not in  modify_list:
                modify_list[key]=line




        for key, val in modify_list.items():
            old_val = self.find_var_line_number_r(key,join_block_number)
            line_number = self.write_line_to_block(join_block_number, None,
                                                   old_val, val,
                                                   'PHI' + "-" + key, front=True)
            self.block_collection[join_block_number].var_space[key] = line_number
            self.block_collection[join_block_number].var_space_end[key] = join_block_number
            key_need_to_update.append((key, old_val, line_number))


        self.while_join_block_modifier(join_block_number,key_need_to_update, {})


        """
                for key,val in self.block_collection[join_block_number].var_space.items():
            do_val= self.block_collection[last_block].var_space[key]
            if val  != do_val:

                line_number = self.write_line_to_block(join_block_number, None,
                                                       do_val, val,
                                                       'PHI'+"-" +key, True)
                key_need_to_update.append((key,val,line_number))
                self.block_collection[join_block_number].var_space[key] = line_number
                self.block_collection[join_block_number].var_space_end[key] = join_block_number
        for pair in key_need_to_update:
            self.while_join_block_modifier(join_block_number,pair,{})
        
        """



        """
         for key_pair in key_need_to_update:
            ident = key_pair[0]
            source =  key_pair[1]
            terget_line = key_pair[2]
            

            for block_key,block in self.block_collection.items():
                for key,from_where in block.var_space_begin.items():
                    if  key  == ident:
                        to_replace = source
                        for i in range(len(self.block_collection[block_key].ssa_lines)):
                            line_numbr = self.block_collection[block_key].ssa_lines[i][0]
                            op = self.block_collection[block_key].ssa_lines[i][3]
                            line_a = self.block_collection[block_key].ssa_lines[i][1]
                            line_b = self.block_collection[block_key].ssa_lines[i][2]
                            line_a_is_var = self.block_collection[block_key].ssa_lines[i][4]
                            line_b_is_var = self.block_collection[block_key].ssa_lines[i][5]
                            if op != None and op !="READ":
                                del self.block_collection[block_key].ssa_lookup_table[(line_a,line_b,op)]
                            if line_a == to_replace and line_a_is_var:
                                line_a = terget_line
                                line_a_is_var = False
                            if line_b == to_replace and line_b_is_var:
                                line_b = terget_line
                                line_b_is_var = False
                            if op != None and op !="READ":
                                self.block_collection[block_key].ssa_lines[i] = (line_numbr,line_a,line_b,op,line_a_is_var,line_b_is_var)
                                self.block_collection[block_key].ssa_lookup_table[(line_a,line_b,op)] = line_number
                            self.block_collection[block_key].var_space[key]=line_number
        """









        self.checkFor("odToken")
        self.write_line_to_block(last_block, None, self.block_collection[join_block_number].ssa_lines[0][0], None, "BRA")
        self.block_collection[last_block].branch = join_block_number
        self.current_block = exit_block_number
        return exit_block_number


    def  find_var_line_number_r(self,var,bn):
        if var in self.block_collection[bn].var_space:
            return self.block_collection[bn].var_space[var]
        else:
            dbn = self.block_collection[bn].dom_block_number
            return self.find_var_line_number_r(var, dbn)


    def find_var_line_number(self,var):
        if var in self.block_collection[self.current_block].var_space:
            return self.block_collection[self.current_block].var_space[var]
        else:
            dbn = self.block_collection[self.current_block].dom_block_number
            return self.find_var_line_number_r(var,dbn)
    def factor(self):
        if self.checkFor('ident', test=True):
            line_number, text= self.designator()
            return line_number,True,text
        elif self.checkFor('number', test=True):
            line_number = self.number()
            return line_number,False,None
        elif self.checkFor('openparenToken', test=True):
            self.checkFor('openparenToken')
            line_numbr,is_de = self.expression()
            self.checkFor('closeparenToken')
            return line_numbr,is_de,None
        elif self.checkFor('callToken', test=True):
            return self.funcCall(),False,None

    def term(self):
        cur_line,is_designator_1,text_1 = self.factor()
        while self.checkFor('timesToken', test=True) or self.checkFor('divToken', test=True):

            if self.checkFor('timesToken'):
                op = 'MUL'
                next_line,is_designator_2,text_2= self.factor()
                r = ssa_line(None, cur_line, next_line, op)
                r = r.to_tuple()
                if r in self.block_collection[self.current_block].ssa_lookup_table:
                    cur_line = self.block_collection[self.current_block].ssa_lookup_table[r]
                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,is_designator_1=is_designator_1,is_designator_2=is_designator_2,text_1=text_1,text_2=text_2)

            elif self.checkFor('divToken'):
                op = 'DIV'
                next_line,is_designator_2,text_2 = self.factor()
                r = ssa_line(None, cur_line, next_line, op)
                r = r.to_tuple()
                if r in self.block_collection[self.current_block].ssa_lookup_table:
                    cur_line = self.block_collection[self.current_block].ssa_lookup_table[r]
                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,is_designator_1=is_designator_1,is_designator_2=is_designator_2,text_1=text_1,text_2=text_2)

        return cur_line,is_designator_1,text_1

    def expression(self):
        cur_line,is_designator_1,text_1 = self.term()
        while self.checkFor('plusToken', test=True) or self.checkFor('minusToken', test=True):

            if self.checkFor('plusToken'):
                op = "ADD"
                next_line,is_designator_2,text_2  = self.term()
                r = ssa_line(None, cur_line, next_line, op)
                r = r.to_tuple()
                if r in self.block_collection[self.current_block].ssa_lookup_table:
                    cur_line = self.block_collection[self.current_block].ssa_lookup_table[r]

                else:
                    cur_line = self.write_line_to_block(self.current_block,None,cur_line, next_line, op,is_designator_1=is_designator_1,is_designator_2=is_designator_2,text_1=text_1,text_2=text_2)


            elif self.checkFor('minusToken'):
                op = "SUB"
                next_line,is_designator_2,text_2  = self.term()
                r = ssa_line(None, cur_line, next_line, op)
                r = r.to_tuple()
                if r in self.block_collection[self.current_block].ssa_lookup_table:
                    cur_line = self.block_collection[self.current_block].ssa_lookup_table[r]
                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,is_designator_1=is_designator_1,is_designator_2=is_designator_2,text_1=text_1,text_2=text_2)


        return cur_line,is_designator_1,text_1

    def designator(self):
        bool0, value, number_value, text = self.checkFor('ident')
        arr = False
        while self.checkFor('openbracketToken', test=True):
            arr = True
            self.checkFor('openbracketToken')
            self.expression()
            self.checkFor('closebracketToken')
        if arr == True:
            None
        return self.find_var_line_number(text),text


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

        constant_blcok_0 = self.create_block(None,None,None,None,{},{})


        block_1 = self.create_block(None, None, None, None, {}, {})
        self.block_collection[constant_blcok_0].next_block = block_1
        self.current_block = block_1

        self.typeDecl()
        _, _, _, text = self.checkFor("ident")
        self.block_collection[block_1].var_space[text] = None
        while self.checkFor("commaToken", test=True):
            self.checkFor("commaToken")
            _, _, _, text = self.checkFor("ident")
            self.block_collection[block_1].var_space[text] = None
        self.checkFor("semiToken")
        return block_1

    def returnStatement(self):
        self.checkFor("returnToken")
        if self.checkFor('ident', test=True) or self.checkFor('number', test=True) or self.checkFor('openparenToken',
                                                                                                    test=True) or self.checkFor(
                'callToken', test=True):
            self.expression()

    def statement(self):
        if self.checkFor("letToken", test=True):
            self.assignment()
            return self.current_block
        elif self.checkFor("callToken", test=True):
            self.funcCall()
            return self.current_block
        elif self.checkFor("ifToken", test=True):
            return self.ifStatement()
        elif self.checkFor("whileToken", test=True):
            return self.whileStatement()
        elif self.checkFor("returnToken", test=True):
            self.returnStatement()
            return self.current_block
        return self.current_block

    def statSequence(self):
        r = self.statement()
        while self.checkFor('semiToken', test=True):
            self.checkFor('semiToken')
            r=self.statement()
        if self.checkFor('semiToken', test=True):
            self.checkFor('semiToken')
        return r

    def formalParam(self):
        self.checkFor('openparenToken')
        if self.checkFor("ident", test=True):
            self.checkFor("ident")
            while self.checkFor("commaToken", test=True):
                self.checkFor("commaToken")
                self.checkFor("ident")

    def funcBody(self):
        None

    def funcDecl(self):
        if self.checkFor("voidToken", test=True):
            self.checkFor("voidToken")
        self.checkFor("funcToken")
        self.checkFor("ident")
        None

    def Parse(self):
        self.checkFor('mainToken')  # main
        self.varDecl()
        self.checkFor("beginToken")
        self.statSequence()
        self.checkFor("endToken")
        self.dot_graph("test")
        self.checkFor('periodToken')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myp = Parser('foo.txt')
    cp = Parser('foo.txt')
    a = []
    for i in range(50):
        a.append(cp.inputSym)
        cp.next()
    myp.Parse()

    b = 6

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

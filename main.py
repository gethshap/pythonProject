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

class Node:
    #https://realpython.com/linked-lists-python/
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList_with_dict:
    #https://realpython.com/linked-lists-python/
    ln = {}

    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def add_first(self, node,ln):
        self.ln[node.data] = ln
        node.next = self.head
        self.head = node


a = LinkedList_with_dict()
b = Node((1,3,"ADD"))
c = Node((1,3,"MUL"))
d  = Node((1,3,"DIV"))
a.add_first(b,1)
a.add_first(c,2)


print(b in a)
print(d in a)

print(a)



class load_trace_back:
    def __init__(self):
        self.mul = LinkedList_with_dict()
        self.add = LinkedList_with_dict()
        self.adda = LinkedList_with_dict()
        self.load = LinkedList_with_dict()







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
        if self.inputSystem == ' ' or self.inputSystem == '\n' or self.inputSystem == ';' or self.inputSystem == "[":

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

    def __init__(self, ssa_line_number,ssa_line_target, ssa_line_source_1, ssa_line_source_2, op,is_designator_1,is_designaotor_2,var_target,var_1,var_2,active=True,const=False,a1=[],a2=[]):
        self.ln = ssa_line_number
        if const == True:
            self.const = True
            self.const_value = ssa_line_target

        else:
            self.const =False
        self.ssa_line_source_1 = ssa_line_source_1
        self.ssa_line_source_2 = ssa_line_source_2
        self.op = op
        self.ssa_line_target = ssa_line_target
        self.is_designator_1 = is_designator_1
        self.is_designator_2 = is_designaotor_2
        self.var_target = var_target
        self.var_1 = var_1
        self.var_2 = var_2




        if active == True:
            self.active  = True
        else:
            self.active = False

    def __repr__(self):
        if self.op == "READ":
            return str(self.ln) + ": " + "READ"
        if self.active:
            if self.const:
                return  str(self.ln) + ": "+ str(self.const_value);
            return str(self.ln) + ": " + str(self.op ) +" " + str(self.ssa_line_source_1) + "  " + str(self.ssa_line_source_2)
        else:
            return str(self.ln) + ": " + "None"




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
    arr_space = {}
    previous =[]
    phi = {}


    has_store  = False
    store_kill_switch = False

    def __init__(self, bn, dbn, ft, branch, next_block, slt, vs, var_space_db_end):
        self.block_number = bn
        self.dom_block_number = dbn
        self.fall_through = ft
        self.branch = branch
        self.next_block = next_block
        self.ssa_lookup_table = {}
        self.ssa_lookup_table_initial = {}
        self.var_space = {}
        self.var_space_end = {}
        self.arr_space = {}
        self.ssa_lines = []
        self.phi ={}
        self.load_store_trace = load_trace_back()

    def __repr__(self):
        return str(self.ssa_lines)


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
    arr_adress_space = {}
    constant_space = {}
    store_table = {}
    non_active_triger = {}

    """
    mul_line = self.write_line_to_block(self.current_block,None,arr_index[0],self.arr_size,"MUL")
    add_line = self.write_line_to_block(self.current_block,None,self.arr_adress_space[text],"BASE","ADD")
    adda_line = self.write_line_to_block(self.current_block,None,mul_line,add_line,"ADDA")
    load_line = self.write_line_to_block(self.current_block,None,adda_line,None,"LOAD")
    """
    load_store_trace = load_trace_back()
    current_block = None
    load_lookup_table  = {}

    def dot_graph(self, name):
        s = Digraph('struct', filename=name, node_attr={'shape': 'record'})
        for block_number, block in self.block_collection.items():
            layout_text = "BB " + str(block_number) + " | {"
            for line in block.ssa_lines:
                    layout_text = layout_text + str(line) + " |"
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

            s.node(str(block_number), layout_text)
        for block_number, block in self.block_collection.items():
            next_block = self.block_collection[block_number].next_block
            ft = self.block_collection[block_number].fall_through
            branch = self.block_collection[block_number].branch
            dbn = self.block_collection[block_number].dom_block_number
            if next_block != None:
                s.edge(str(block_number), str(next_block))
            if ft != None:
                s.edge(str(block_number), str(ft), label="fall_through")
            if branch != None:
                s.edge(str(block_number), str(branch), label="branch")
            if dbn != None:
                s.edge(str(dbn), str(block_number), label="dom", color="blue")

        s.view()
        None

    def create_block(self, dbn, ft, branch, next_block, slt, vs):
        b = None
        if dbn == None:
            b = Basic_block(self.block_count, dbn, ft, branch, next_block, slt, vs,
                            {})
        else:
            b = Basic_block(self.block_count, dbn, ft, branch, next_block, slt, vs,
                            var_space_db_end=self.block_collection[dbn].var_space_end)
        self.block_collection[self.block_count] = b
        r = self.block_count
        self.block_count = self.block_count + 1
        return r

    def update_line_to_block(self, bn):
        None

    def write_line_to_block(self, bn, ssa_line_const, ssa_line_source_1, ssa_line_source_2, op, front=False,
                            replace=False,var_target= None, is_designator_1=False, is_designator_2=False, text_1=None, text_2=None,
                            insert=False, insert_i=-1,active=True):
        if ssa_line_const != None and op != "WRITE":
            const_line = ssa_line(self.ssa_count,ssa_line_const,None,None,None,None,None,None,None,None,const=True)
            ssa_key = const_line.to_tuple()
            self.block_collection[bn].ssa_lines.append(const_line)
            self.constant_space[ssa_line_const] = self.ssa_count
            cur_ln = self.ssa_count
            self.ssa_count = self.ssa_count + 1
            return cur_ln
        else:
            line = ssa_line(self.ssa_count,ssa_line_const,ssa_line_source_1,ssa_line_source_2,op,is_designator_1=is_designator_1
                         ,is_designaotor_2=is_designator_2,var_target=var_target,var_1=text_1,var_2=text_2,active= active)
            ssa_key = line.to_tuple()
            if insert == True:
                self.block_collection[bn].ssa_lines.insert(insert_i,line)
                if op == "READ" or op == None:
                    r = self.ssa_count
                    self.ssa_count = self.ssa_count + 1
                    return r
                self.block_collection[bn].ssa_lookup_table[ssa_key] = self.ssa_count
                r = self.ssa_count
                self.ssa_count = self.ssa_count + 1
                return r
            if front == False:
                self.block_collection[bn].ssa_lines.append(
                    line)
                if op == "READ" or op == None:
                    r = self.ssa_count
                    self.ssa_count = self.ssa_count + 1
                    return r
                self.block_collection[bn].ssa_lookup_table[ssa_key] = self.ssa_count
                r = self.ssa_count
                self.ssa_count = self.ssa_count + 1
                return r
            else:
                self.block_collection[bn].ssa_lines.insert(0,line)


            if op == "READ" or op == None:
                r = self.ssa_count
                self.ssa_count = self.ssa_count + 1
                return r

            self.block_collection[bn].ssa_lookup_table[ssa_key] = self.ssa_count
            r = self.ssa_count
            self.ssa_count = self.ssa_count + 1

            return r



    def ssa_count_increase(self):
        cur = self.ssa_count
        self.ssa_count = self.ssa_count + 1
        return cur



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
                self.mytk.error("syntaxError" + "  expect " + tkt + " got " + self.inputSym.tokentype)
                return False
            else:
                return False

    def number(self):
        _, v, nv, t = self.checkFor('number')
        if nv in self.constant_space:
            return self.constant_space[nv],t
        else:
            return self.write_line_to_block(0, nv, None, None, None),str(nv)

    def assignment(self):
        self.checkFor('letToken')
        line_number_for_dst, text, store = self.designator(store=True)
        self.checkFor('becomesToken')
        line_number, is_d, text_1 = self.expression(target_val= text)

        if store == True:
            self.write_line_to_block(self.current_block,None,line_number,line_number_for_dst,"STORE")
        if not store:
            self.block_collection[self.current_block].var_space[text] = line_number
            self.block_collection[self.current_block].var_space_end[text] = self.current_block
        return store

    def relation(self):
        line_a, is_d1, text_1 = self.expression()
        _, v, nv, t = self.relOp()
        line_b, is_d2, text_2 = self.expression()

        return v, self.write_line_to_block(self.current_block, None, line_a, line_b, "CMP", is_designator_1=is_d1,
                                           is_designator_2=is_d2, text_1=text_1, text_2=text_2)

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
        bool0, value, number_value, text = self.checkFor('ident')
        if text == "InputNum":
            if self.checkFor('openparenToken', test=True):
                self.checkFor('openparenToken')
                self.checkFor('closeparenToken')
            return self.write_line_to_block(self.current_block, None, None, None, "READ")
        if text == "OutputNum":
            cur_line, is_designator_1, text_1 = None,None,None
            if self.checkFor('openparenToken', test=True):
                self.checkFor('openparenToken')
                cur_line, is_designator_1, text_1 = self.expression()
                self.checkFor('closeparenToken')
            return self.write_line_to_block(self.current_block, None, cur_line, None, "WRITE")



        if self.checkFor('openparenToken', test=True):
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
        ft_block_number = self.create_block(dom_block, None, None, None,
                                            self.block_collection[dom_block].ssa_lookup_table,
                                            self.block_collection[dom_block].var_space)
        self.block_collection[ft_block_number].previous.append(dom_block)
        branch_block_number = self.create_block(dom_block, None, None, None,
                                                self.block_collection[dom_block].ssa_lookup_table,
                                                self.block_collection[dom_block].var_space)
        self.block_collection[branch_block_number].previous.append(dom_block)
        exit_block_number = self.create_block(dom_block, None, None, None,
                                              self.block_collection[dom_block].ssa_lookup_table,
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
            branch_key = (cmp_line, first_branch_line, "BGE")
        if type == 23:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BLE")
            branch_key = (cmp_line, first_branch_line, "BLE")
        if type == 24:
            self.write_line_to_block(self.current_block, None, cmp_line, first_branch_line, "BGT")
            branch_key = (cmp_line, first_branch_line, "BGT")
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
            exit_first_line = self.write_line_to_block(exit_block_number, None, None, None, None)

        if not self.block_collection[ft_block_number].ssa_lines:
            self.write_line_to_block(ft_block_number, None, None, None, None)

        if self.block_collection[exit_block_number].ssa_lines:
            branch_back = self.block_collection[exit_block_number]
            first_line_number = self.block_collection[exit_block_number].ssa_lines[0].ln
            for key, val in self.block_collection.items():
                if val.branch == exit_block_number:
                    self.write_line_to_block(key, None, first_line_number, None, "BRA")

        if self.checkFor("elseToken", test=True):

            self.checkFor("elseToken")
            self.current_block = branch_block_number
            last_block = self.statSequence()
            if not self.block_collection[branch_block_number].ssa_lines:
                self.write_line_to_block(branch_block_number, None, None, None, None)
            first_line_number = self.block_collection[branch_block_number].ssa_lines[0].ln
            branch_line_number = self.block_collection[dom_block].ssa_lines[-1].ln


            self.block_collection[dom_block].ssa_lookup_table[
                (cmp_line, first_line_number, branch_key[2])] = branch_line_number
            self.block_collection[branch_block_number].ssa_lookup_table[
                (cmp_line, first_line_number, branch_key[2])] = branch_line_number
            self.block_collection[ft_block_number].ssa_lookup_table[
                (cmp_line, first_line_number, branch_key[2])] = branch_line_number
            self.block_collection[exit_block_number].ssa_lookup_table[
                (cmp_line, first_line_number, branch_key[2])] = branch_line_number

        self.current_block = exit_block_number
        ft_val = None
        branch_val = None

        for key, val in self.block_collection.items():
            if val.branch == exit_block_number:
                branch_before_exit = key
            elif val.fall_through == exit_block_number:
                ft_before_exit = key

        modify_list_1 = copy.deepcopy(self.block_collection[branch_before_exit].var_space)
        track_back = branch_before_exit
        while track_back != dom_block:
            for key, line in self.block_collection[track_back].var_space.items():
                if key not in modify_list_1:
                    modify_list_1[key] = line
            track_back = self.block_collection[track_back].dom_block_number

        modify_list_2 = copy.deepcopy(self.block_collection[ft_before_exit].var_space)
        track_back = ft_before_exit
        while track_back != dom_block:
            for key, line in self.block_collection[track_back].var_space.items():
                if key not in modify_list_2:
                    modify_list_2[key] = line
            track_back = self.block_collection[track_back].dom_block_number

        merged_keys = []
        for key_1, line_ in modify_list_1.items():
            if key_1 not in merged_keys:
                merged_keys.append(key_1)

        for key_2, line_ in modify_list_2.items():
            if key_2 not in merged_keys:
                merged_keys.append(key_2)
        for key,_ in self.store_table.items():
            if self.test_connect(key,exit_block_number):
                line_number = self.write_line_to_block(self.current_block, None,
                                                       None, None,
                                                       "KILL")
                self.block_collection[exit_block_number].store_kill_switch = True
        for key in merged_keys:
            line = self.find_var_line_number_r(key, dom_block)
            if key in modify_list_1 and key in modify_list_2:
                line_number = self.write_line_to_block(self.current_block, None,
                                                       modify_list_1[key], modify_list_2[key],
                                                       'PHI-' + key)
                self.block_collection[exit_block_number].phi[key] = 1
                self.block_collection[exit_block_number].var_space[key] = line_number
                self.block_collection[exit_block_number].var_space_end[key] = exit_block_number
            elif key in modify_list_1 and key not in modify_list_2:
                line_number = self.write_line_to_block(self.current_block, None,
                                                       modify_list_1[key], line,
                                                       'PHI-' + key)
                self.block_collection[exit_block_number].phi[key] = 1
                self.block_collection[exit_block_number].var_space[key] = line_number
                self.block_collection[exit_block_number].var_space_end[key] = exit_block_number

            elif key not in modify_list_1 and key in modify_list_2:
                line_number = self.write_line_to_block(self.current_block, None,
                                                       modify_list_2[key], line,
                                                       'PHI-' + key)
                self.block_collection[exit_block_number].phi[key] = 1
                self.block_collection[exit_block_number].var_space[key] = line_number
                self.block_collection[exit_block_number].var_space_end[key] = exit_block_number

        self.checkFor("fiToken")

        return exit_block_number

    def break_line(self):
        None

    def del_ssa(self,ssa_key,bn):
        if ssa_key in self.block_collection[bn].ssa_lookup_table:
            del self.block_collection[bn].ssa_lookup_table[ssa_key]
        else:
            dbn = self.block_collection[bn].dom_block_number
            if dbn == None:
                return None
            else:
                return self.del_ssa(ssa_key,dbn)


    def search_for_ssa(self,ssa_key,bn):
        if ssa_key in self.block_collection[bn].ssa_lookup_table:
            return self.block_collection[bn].ssa_lookup_table[ssa_key]
        else:
            dbn = self.block_collection[bn].dom_block_number
            if  dbn == None:
                return None
            else:
                return self.search_for_ssa(ssa_key,dbn)

    def non_active_line_modifier(self, start_block, modified_line,var_name, visited,source):


        for var_name,line in self.block_collection[start_block].var_space.items():
            if line == modified_line:
                for i in range(len(self.block_collection[start_block].ssa_lines)):
                    if self.block_collection[start_block].ssa_lines[i].var_target == var_name and self.block_collection[start_block].ssa_lines[i].active==False:
                        old_val = self.block_collection[start_block].var_space[var_name]
                        self.block_collection[start_block].var_space[var_name] =   self.block_collection[start_block].ssa_lines[i].ln
                        self.block_collection[start_block].ssa_lines[i].active = True
                        self.while_join_block_modifier(start_block,(var_name,source,self.block_collection[start_block].ssa_lines[i].ln),{},start_block)


        if self.block_collection[start_block].next_block and self.block_collection[
            start_block].next_block not in visited:
            visited[start_block] = 1
            self.non_active_line_modifier(self.block_collection[start_block].next_block, modified_line,var_name, visited,source)
        if self.block_collection[start_block].branch and self.block_collection[start_block].branch not in visited:
            visited[start_block] = 1
            self.non_active_line_modifier(self.block_collection[start_block].branch, modified_line,var_name, visited,source)
        if self.block_collection[start_block].fall_through and self.block_collection[
            start_block].fall_through not in visited:
            visited[start_block] = 1
            self.non_active_line_modifier(self.block_collection[start_block].fall_through, modified_line,var_name ,visited,source)



    def has_kill(self,bn,target):

        if bn == target:
            return False
        if self.block_collection[bn].store_kill_switch:
            return True
        else:
            dbn = self.block_collection[bn].dom_block_number
            return self.has_kill(dbn,target)

    def update_load_phase2(self,current_block,old,new,visited):
        for var,line in self.block_collection[current_block].var_space.items():
            if line == old:
                self.block_collection[current_block].var_space[var] = new
                self.non_active_line_modifier(current_block,old,var,{},current_block)




        for i in range(len(self.block_collection[current_block].ssa_lines)):
            line_number = self.block_collection[current_block].ssa_lines[i].ln
            op = self.block_collection[current_block].ssa_lines[i].op
            line_a = self.block_collection[current_block].ssa_lines[i].ssa_line_source_1
            line_b = self.block_collection[current_block].ssa_lines[i].ssa_line_source_2
            line_a_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_1
            line_b_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_2
            line_a_text = self.block_collection[current_block].ssa_lines[i].var_1
            line_b_text = self.block_collection[current_block].ssa_lines[i].var_2
            line_target  = self.block_collection[current_block].ssa_lines[i].var_target


            if line_a == old:
                self.block_collection[current_block].ssa_lines[i].ssa_line_source_1 = new
                if self.block_collection[current_block].ssa_lines[i].active == False:
                    self.block_collection[current_block].ssa_lines[i].active = True
                    CSE = self.non_active_triger[self.block_collection[current_block].ssa_lines[i].ln]
                    self.update_load_phase2( current_block, CSE, self.block_collection[current_block].ssa_lines[i].ln,
                                             {})


            if line_b == old:
                self.block_collection[current_block].ssa_lines[i].ssa_line_source_2 = new
                if self.block_collection[current_block].ssa_lines[i].active == False:
                    self.block_collection[current_block].ssa_lines[i].active = True
                    CSE = self.non_active_triger[self.block_collection[current_block].ssa_lines[i].ln]
                    self.update_load_phase2(current_block, CSE, self.block_collection[current_block].ssa_lines[i].ln,
                                            {})

            if self.block_collection[current_block].next_block and self.block_collection[
                current_block].next_block not in visited:
                visited[current_block] = 1
                self.update_load_phase2(self.block_collection[current_block].next_block, old,new,visited)
            if self.block_collection[current_block].branch and self.block_collection[
                current_block].branch not in visited:
                visited[current_block] = 1
                self.update_load_phase2(self.block_collection[current_block].branch,  old,new,visited)
            if self.block_collection[current_block].fall_through and self.block_collection[
                current_block].fall_through not in visited:
                visited[current_block] = 1
                self.update_load_phase2(self.block_collection[current_block].fall_through,   old,new,visited)




    def update_load(self,current_block,join_block_number,visited):



        for i in range(len(self.block_collection[current_block].ssa_lines)):
            line_number = self.block_collection[current_block].ssa_lines[i].ln
            op = self.block_collection[current_block].ssa_lines[i].op
            line_a = self.block_collection[current_block].ssa_lines[i].ssa_line_source_1
            line_b = self.block_collection[current_block].ssa_lines[i].ssa_line_source_2
            line_a_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_1
            line_b_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_2
            line_a_text = self.block_collection[current_block].ssa_lines[i].var_1
            line_b_text = self.block_collection[current_block].ssa_lines[i].var_2
            line_target  = self.block_collection[current_block].ssa_lines[i].var_target




            if line_a in self.load_lookup_table:
                tuple = self.load_lookup_table[line_a]
                target_bn = tuple[0]
                line = tuple[1]
                if self.has_kill(current_block,target_bn):
                    adda_line = self.write_line_to_block(current_block,None,line.ssa_line_source_1,
                                                         line.ssa_line_source_2,line.op,var_target=line.var_target
                                            ,is_designator_1=line.is_designator_1,is_designator_2=line.is_designator_2,text_1=
                                                         line.var_1,text_2=line.var_2,insert_i=i,insert=True)
                    load_line = self.write_line_to_block(current_block, None, adda_line, None, "LOAD", insert=True,
                                                         insert_i=i + 1)
                    old_val = self.block_collection[current_block].ssa_lines[i+2].ssa_line_source_1
                    new_val = load_line
                    self.block_collection[current_block].ssa_lines[i+2].ssa_line_source_1 = load_line
                    self.update_load_phase2(current_block,old_val,new_val,{})








            if line_b in self.load_lookup_table:
                tuple = self.load_lookup_table[line_b]
                bn = tuple[0]
                line = tuple[1]
                if self.has_kill(current_block, target_bn):
                    adda_line = self.write_line_to_block(current_block, None, line.ssa_line_source_1,
                                                         line.ssa_line_source_2, line.op, var_target=line.var_target
                                                         , is_designator_1=line.isdesignator_1,
                                                         is_designator_2=line.is_designator_2, text_1=
                                                         line.var_1, text_2=line.var_2, insert_i=i, insert=True)
                    load_line = self.write_line_to_block(current_block, None, adda_line, None, "LOAD", insert=True,
                                                         insert_i=i + 1)
                    old_val = self.block_collection[current_block].ssa_lines[i + 2].ssa_line_source_2
                    new_val = load_line
                    self.block_collection[current_block].ssa_lines[i+2].ssa_line_source_2 = load_line
                    self.update_load_phase2(current_block, old_val, new_val, {})

        if self.block_collection[current_block].next_block and self.block_collection[
            current_block].next_block not in visited:
            visited[current_block] = 1
            self.update_load(self.block_collection[current_block].next_block,join_block_number ,visited)
        if self.block_collection[current_block].branch and self.block_collection[current_block].branch not in visited:
            visited[current_block] = 1
            self.update_load(self.block_collection[current_block].branch,join_block_number, visited)
        if self.block_collection[current_block].fall_through and self.block_collection[
            current_block].fall_through not in visited:
            visited[current_block] = 1
            self.update_load(self.block_collection[current_block].fall_through ,join_block_number,visited)








    def while_join_block_modifier(self, current_block, key_pair, visited,source_block):

        '''
        :param current_block:
        :param key_pair:
        :param visited:
        :param source_block:
        :return:
        '''
        ident = key_pair[0]
        source = key_pair[1]
        target_line = key_pair[2]

        if key_pair[0] in self.block_collection[current_block].phi and current_block != source_block:

            for i in range(len(self.block_collection[current_block].ssa_lines)):
                line_number = self.block_collection[current_block].ssa_lines[i].ln
                op = self.block_collection[current_block].ssa_lines[i].op
                line_a = self.block_collection[current_block].ssa_lines[i].ssa_line_source_1
                line_b = self.block_collection[current_block].ssa_lines[i].ssa_line_source_2
                line_a_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_1
                line_b_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_2
                line_a_text = self.block_collection[current_block].ssa_lines[i].var_1
                line_b_text = self.block_collection[current_block].ssa_lines[i].var_2
                if op != None and op != "READ":
                    if op[0:3] == 'PHI':
                        var_name = op[4:]
                        if var_name == ident:
                            if line_a == source:
                                self.block_collection[current_block].ssa_lines[i].active = True
                                self.non_active_line_modifier(current_block, line_number, ident, {},source)
                                self.block_collection[current_block].ssa_lines[i].ssa_line_source_1 = target_line
                            if line_b == source:
                                self.block_collection[current_block].ssa_lines[i].active = True
                                self.non_active_line_modifier(current_block, line_number, ident, {},source)
                                self.block_collection[current_block].ssa_lines[i].ssa_line_source_2 = target_line
            return




        for i in range(len(self.block_collection[current_block].ssa_lines)):
            line_number = self.block_collection[current_block].ssa_lines[i].ln
            op = self.block_collection[current_block].ssa_lines[i].op
            line_a = self.block_collection[current_block].ssa_lines[i].ssa_line_source_1
            line_b = self.block_collection[current_block].ssa_lines[i].ssa_line_source_2
            line_a_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_1
            line_b_is_var = self.block_collection[current_block].ssa_lines[i].is_designator_2
            line_a_text = self.block_collection[current_block].ssa_lines[i].var_1
            line_b_text = self.block_collection[current_block].ssa_lines[i].var_2
            line_target  = self.block_collection[current_block].ssa_lines[i].var_target

            if op != None and op != "READ":
                if op[0:3] == 'PHI':
                    var_name = op[4:]
                    target = self.find_var_line_number_r(var_name,
                                                         self.block_collection[current_block].dom_block_number)

                else:
                    if ident == line_target and  self.block_collection[current_block].ssa_lines[i].active == False:
                        self.block_collection[current_block].ssa_lines[i].active = True
                        source = self.block_collection[current_block].var_space[ident]
                        self.block_collection[current_block].ssa_lookup_table[(target_line, line_b, op)] = source
                        self.block_collection[current_block].var_space[ident] = self.block_collection[current_block].ssa_lines[i].ln
                        self.non_active_line_modifier(current_block, line_number, ident, {}, source)
                        self.while_join_block_modifier(current_block,(ident,source,self.block_collection[current_block].ssa_lines[i].ln),{},current_block)



                    if ident == line_a_text:
                        if line_a_is_var:

                            #unfinished
                            self.block_collection[current_block].ssa_lines[i].active = True
                            self.non_active_line_modifier(current_block, line_number, ident, {},source)
                            self.block_collection[current_block].ssa_lines[i].ssa_line_source_1 = target_line
                            self.del_ssa((line_a, line_b, op),self.current_block)
                            self.block_collection[current_block].ssa_lookup_table[(target_line, line_b, op)] = line_number


                    if ident == line_b_text:
                        if line_b_is_var:
                            self.block_collection[current_block].ssa_lines[i].active = True
                            self.non_active_line_modifier(current_block, line_number, ident, {},source)
                            self.block_collection[current_block].ssa_lines[i].ssa_line_source_2 = target_line
                            self. del_ssa((line_a, line_b, op), self.current_block)
                            self.block_collection[current_block].ssa_lookup_table[(line_a, target_line, op)] = line_number
        if ident in  self.block_collection[current_block].var_space:
            return

        if self.block_collection[current_block].next_block and self.block_collection[
            current_block].next_block not in visited:
            visited[current_block] = 1
            self.while_join_block_modifier(self.block_collection[current_block].next_block, key_pair, visited, source_block)
        if self.block_collection[current_block].branch and self.block_collection[current_block].branch not in visited:
            visited[current_block] = 1
            self.while_join_block_modifier(self.block_collection[current_block].branch, key_pair, visited, source_block)
        if self.block_collection[current_block].fall_through and self.block_collection[
            current_block].fall_through not in visited:
            visited[current_block] = 1
            self.while_join_block_modifier(self.block_collection[current_block].fall_through, key_pair, visited, source_block)


        # self.block_collection[start_block].var_space[ident] = line_number


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




        if self.block_collection[dom_block].branch:
            self.block_collection[exit_block_number].branch = self.block_collection[dom_block].branch
            self.block_collection[dom_block].branch = None

        if self.block_collection[dom_block].fall_through:
            self.block_collection[exit_block_number].fall_through = self.block_collection[dom_block].fall_through
            self.block_collection[dom_block].fall_through = None

        if not self.block_collection[exit_block_number].ssa_lines:
            self.write_line_to_block(exit_block_number, None, None, None, None)

        exit_first_line = self.block_collection[exit_block_number].ssa_lines[0].ln

        self.checkFor('whileToken')
        self.current_block = join_block_number
        type, cmp_line = self.relation()

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
            branch_key = (cmp_line, exit_first_line, "BGT")
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
            for key, line in self.block_collection[track_back].var_space.items():
                if key not in modify_list:
                    modify_list[key] = line
            track_back = self.block_collection[track_back].dom_block_number
        for key, line in self.block_collection[do_block_number].var_space.items():
            if key not in modify_list:
                modify_list[key] = line
        for key,_ in self.store_table.items():
            if self.test_connect(key,join_block_number):
                line_number = self.write_line_to_block(join_block_number, None,
                                                       None, None,
                                                       "KILL",front=True)
                self.block_collection[join_block_number].store_kill_switch = True
                break

        self.update_load(join_block_number,join_block_number,{})











        #mul_node = Node((, self.word_size, "MUL"))
        #add_node = Node((self.arr_adress_space[text], "BASE", "ADD"))



        for key,_ in modify_list.items():
            old_val = self.find_var_line_number_r(key, join_block_number)
            self.while_join_block_modifier(join_block_number, (key, old_val, self.ssa_count), {}, join_block_number)
            val = self.find_var_line_number_r(key, last_block)
            line_number = self.write_line_to_block(join_block_number, None,
                                                   old_val, val,
                                                   'PHI' + "-" + key, front=True)
            self.block_collection[join_block_number].phi[key] = 1
            self.block_collection[join_block_number].var_space[key] = line_number
            self.block_collection[join_block_number].var_space_end[key] = join_block_number
            #self.while_join_block_modifier(join_block_number, (key, old_val, line_number), {},join_block_number)









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
                                self.del_ssa((line_a, line_b, op), self.current_block)
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


        self.checkFor("odToken")
        self.write_line_to_block(last_block, None, self.block_collection[join_block_number].ssa_lines[0].ln, None,
                                 "BRA")
        self.block_collection[last_block].branch = join_block_number
        self.current_block = exit_block_number
        return exit_block_number

    def find_var_line_number_r(self, var, bn):
        if var in self.block_collection[bn].var_space:
            return self.block_collection[bn].var_space[var]
        else:
            dbn = self.block_collection[bn].dom_block_number
            return self.find_var_line_number_r(var, dbn)

    def find_var_line_number(self, var):
        if var in self.block_collection[self.current_block].var_space:
            return self.block_collection[self.current_block].var_space[var]
        else:
            dbn = self.block_collection[self.current_block].dom_block_number
            return self.find_var_line_number_r(var, dbn)

    def factor(self):
        if self.checkFor('ident', test=True):
            line_number, text,_ = self.designator()
            return line_number, True, text
        elif self.checkFor('number', test=True):
            line_number,t = self.number()
            return line_number, False, None
        elif self.checkFor('openparenToken', test=True):
            self.checkFor('openparenToken')
            line_numbr, is_de,text = self.expression()
            self.checkFor('closeparenToken')
        elif self.checkFor('callToken', test=True):
            return self.funcCall(), False, None

    def term(self):
        cur_line, is_designator_1, text_1 = self.factor()
        while self.checkFor('timesToken', test=True) or self.checkFor('divToken', test=True):

            if self.checkFor('timesToken'):
                op = 'MUL'
                next_line, is_designator_2, text_2 = self.factor()
                r = ssa_line(None, cur_line, next_line, op)
                r = r.to_tuple()
                find_ssa = self.search_for_ssa(r,self.current_block)
                if find_ssa:
                    non_active_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                               is_designator_1=is_designator_1,
                                                               is_designator_2=is_designator_2, text_1=text_1,
                                                               text_2=text_2, active=False)
                    cur_line = find_ssa
                    self.non_active_triger[non_active_line]= find_ssa
                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                        is_designator_1=is_designator_1,
                                                        is_designator_2=is_designator_2, text_1=text_1, text_2=text_2)


            elif self.checkFor('divToken'):
                op = 'DIV'
                next_line, is_designator_2, text_2 = self.factor()
                r = ssa_line(None, cur_line, next_line, op)
                find_ssa = self.search_for_ssa(r, self.current_block)
                if find_ssa:

                    non_active_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                               is_designator_1=is_designator_1,
                                                               is_designator_2=is_designator_2, text_1=text_1,
                                                               text_2=text_2, active=False)
                    cur_line = find_ssa
                    self.non_active_triger[non_active_line] = find_ssa
                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                        is_designator_1=is_designator_1,
                                                        is_designator_2=is_designator_2, text_1=text_1, text_2=text_2)

        return cur_line, is_designator_1, text_1

    def find_line(self, bn, ln):
        for bn, block in self.block_collection.items():
            for i in range(len(block.ssa_lines)):
                if block.ssa_lines[i].ln == ln:
                    return block.ssa_lines[i], bn, i

    def expression(self,target_val= None):
        cur_line, is_designator_1, text_1 = self.term()
        cur_line_copy = cur_line
        while self.checkFor('plusToken', test=True) or self.checkFor('minusToken', test=True):

            if self.checkFor('plusToken'):
                op = "ADD"
                next_line, is_designator_2, text_2 = self.term()
                line = ssa_line(self.ssa_count,None, cur_line, next_line, op,is_designator_1=is_designator_1,is_designaotor_2= is_designator_2,var_1=text_1,var_2=text_2,var_target=target_val)
                ssa_key = line.to_tuple()
                find_ssa = self.search_for_ssa(ssa_key, self.current_block)


                if find_ssa:
                    non_active_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                               is_designator_1=is_designator_1,
                                                               is_designator_2=is_designator_2, text_1=text_1,
                                                               text_2=text_2, active=False, var_target=target_val)

                    cur_line = find_ssa
                    self.non_active_triger[non_active_line] = find_ssa






                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                        is_designator_1=is_designator_1,
                                                        is_designator_2=is_designator_2, text_1=text_1, text_2=text_2,var_target=target_val)


            elif self.checkFor('minusToken'):
                op = "SUB"
                next_line, is_designator_2, text_2 = self.term()
                r = ssa_line(self.ssa_count, None, cur_line, next_line, op, is_designator_1=is_designator_1,is_designaotor_2= is_designator_2
                             , var_1=text_1, var_2=text_2,var_target=None)
                find_ssa = self.search_for_ssa(ssa_key, self.current_block)
                if find_ssa:



                    non_active_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                               is_designator_1=is_designator_1,
                                                               is_designator_2=is_designator_2, text_1=text_1,
                                                               text_2=text_2, active=False,var_target=target_val)
                    cur_line = find_ssa
                    self.non_active_triger[non_active_line] = find_ssa
                    None
                else:
                    cur_line = self.write_line_to_block(self.current_block, None, cur_line, next_line, op,
                                                        is_designator_1=is_designator_1,
                                                        is_designator_2=is_designator_2, text_1=text_1, text_2=text_2,var_target=target_val)

        return cur_line, is_designator_1, text_1

    def trace_load_store(self,bn,node,flag=None):




        if flag == "mul":
            if node.data in self.block_collection[bn].load_store_trace.mul:
                return self.block_collection[bn].load_store_trace.mul.ln[node.data]
            else:
                if bn == 1 :
                    return None
                dbn = self.block_collection[bn].dom_block_number
                return  self.trace_load_store(dbn,node,flag)
        elif flag == "add":
            if node.data in self.block_collection[bn].load_store_trace.add:
                return  self.block_collection[bn].load_store_trace.add.ln[node.data]
            else:
                if bn == 1 :
                    return None
                dbn = self.block_collection[bn].dom_block_number
                return self.trace_load_store(dbn, node, flag)
        elif flag == "adda":
            if node.data in self.block_collection[bn].load_store_trace.adda:
                return  self.block_collection[bn].load_store_trace.adda.ln[node.data]
            else:
                if bn == 1 :
                    return None
                dbn = self.block_collection[bn].dom_block_number
                return self.trace_load_store(dbn, node, flag)

        elif flag == 'load' :
            if node.data in self.block_collection[bn].load_store_trace.load:
                return self.block_collection[bn].load_store_trace.load.ln[node.data]
            else:
                if bn == 1 or self.block_collection[bn].store_kill_switch == True:
                    return None
                dbn = self.block_collection[bn].dom_block_number
                return self.trace_load_store(dbn, node, flag)

    def find_ssa_line(self, ln):
        for k,v in self.block_collection.items():
            for line in v.ssa_lines:
                if line.ln == ln:
                    return (k,line)


    def designator(self,store=False):
        bool0, value, number_value, text = self.checkFor('ident')
        arr = False
        full_text = text

        arr_index = []
        while self.checkFor('openbracketToken', test=True):
            arr = True
            self.checkFor('openbracketToken')
            cur_line, is_designator_1, text_1 = self.expression()
            full_text = full_text +"-" + str(cur_line)

            arr_index.append(cur_line)
            self.checkFor('closebracketToken')

        if arr == True:
            """
            8 mul size i
            9 add address_of a base
            10 adda 8 9
            11 load 10
            """
            mul_line, add_line, adda_line, load_line = None, None, None, None

            mul_node = Node((arr_index[0], self.word_size, "MUL"))
            add_node = Node((self.arr_adress_space[text], "BASE","ADD"))

            mul_line =  self.trace_load_store(self.current_block,mul_node,flag="mul")
            if mul_line == None:
                mul_line = self.write_line_to_block(self.current_block, None, arr_index[0], self.word_size, "MUL")
                self.block_collection[self.current_block].load_store_trace.mul.add_first(mul_node,mul_line)

            add_line =  self.trace_load_store(self.current_block,add_node,flag="add")
            if add_line == None:
                add_line = self.write_line_to_block(self.current_block, None, self.arr_adress_space[text], "BASE",
                                                    "ADD")
                self.block_collection[self.current_block].load_store_trace.add.add_first(add_node,add_line)

            adda_node =Node((mul_line, add_line, "ADDA"))
            adda_line = self.trace_load_store(self.current_block, adda_node, flag="adda")
            if adda_line == None:
                adda_line = self.write_line_to_block(self.current_block, None, mul_line, add_line, "ADDA")
                self.block_collection[self.current_block].load_store_trace.adda.add_first(adda_node, adda_line)

            if store == False:
                load_node = Node((adda_line, None, "LOAD"))
                load_line = self.trace_load_store(self.current_block,load_node,flag="load")
                if load_line == None:
                    load_line = self.write_line_to_block(self.current_block, None, adda_line, None, "LOAD")
                    self.block_collection[self.current_block].load_store_trace.load.add_first(load_node, load_line)

                    self.load_lookup_table[load_line] = self.find_ssa_line(adda_line)

                return load_line, full_text, False
            else:
                if arr_index[0] not in self.constant_space.values():
                    self.block_collection[self.current_block].has_store = True
                    self.store_table[self.current_block ] = 1
                return adda_line, full_text, True
        else:
            return self.find_var_line_number(text), text, False



    def test_connect(self, bn_s,bn_t,visited={}):
        toDo = []
        Done = []
        toDo.append(bn_s)
        while toDo :
            e = toDo[0]
            toDo.pop(0)
            Done.append(e)
            ne = []
            if self.block_collection[e].next_block and self.block_collection[
                e].next_block not in Done:
                ne.append(self.block_collection[e].next_block)
            if self.block_collection[e].branch and self.block_collection[
                e].branch not in Done:
                ne.append(self.block_collection[e].branch)
            if self.block_collection[e].fall_through and self.block_collection[
                e].fall_through not in Done:
                ne.append(self.block_collection[e].fall_through)

            for n in ne:
                if n == bn_t:
                    return True
                if n  not in Done:
                    toDo.append(n)
        return False
















    def f(s):
        None

    def typeDecl(self):
        if self.checkFor("varToken", test=True):
            self.checkFor("varToken")
            return "var"
        elif self.checkFor("arrToken", test=True):
            self.checkFor("arrToken")
            self.checkFor("openbracketToken")
            self.checkFor("number")
            self.checkFor("closebracketToken")
            while self.checkFor("openbracketToken", test=True):
                self.checkFor("openbracketToken")
                self.checkFor("number")
                self.checkFor("closebracketToken")
            return "array"

    def varDecl(self):
        if not self.block_collection:
            constant_blcok_0 = self.create_block(None, None, None, None, {}, {})
            block_1 = self.create_block(None, None, None, None, {}, {})
            self.block_collection[constant_blcok_0].next_block = block_1
            self.current_block = block_1
            self.word_size = self.write_line_to_block(0, 4, None, None, None)

        type = self.typeDecl()
        if type == "var":
            _, _, _, text = self.checkFor("ident")
            self.block_collection[1].var_space[text] = None
            while self.checkFor("commaToken", test=True):
                self.checkFor("commaToken")
                _, _, _, text = self.checkFor("ident")
                self.block_collection[1].var_space[text] = None
            self.checkFor("semiToken")
            return 1
        else:
            _, _, _, text = self.checkFor("ident")
            self.block_collection[1].arr_space[text] = None
            line = self.write_line_to_block(0, "address of " + text, None, None, None)
            self.arr_adress_space[text] = line
            while self.checkFor("commaToken", test=True):
                self.checkFor("commaToken")
                _, _, _, text = self.checkFor("ident")
                line = self.write_line_to_block(0, "address of " + text, None, None, None)
                self.arr_adress_space[text] = line
                self.block_collection[1].arr_space[text] = None
            self.checkFor("semiToken")
            return 1

    def returnStatement(self):
        self.checkFor("returnToken")
        if self.checkFor('ident', test=True) or self.checkFor('number', test=True) or self.checkFor('openparenToken',
                                                                                                    test=True) or self.checkFor(
            'callToken', test=True):
            self.expression()

    def statement(self):
        if self.checkFor("letToken", test=True):
            store = self.assignment()
            self.block_collection[self.current_block].has_store = store
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
            r = self.statement()
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
        while self.checkFor('varToken', test=True) or self.checkFor('arrToken', test=True):
            self.varDecl()

        self.checkFor("beginToken")
        self.statSequence()
        self.checkFor("endToken")
        print(self.has_kill(4,2))
        print(self.has_kill(3, 2))
        print(self.has_kill(3, 1))

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm
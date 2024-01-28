# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if len(self) == 0:
            return True
        return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = 0
        if self.top == None:
            return 0
        current = self.top
        while current.next != None:
            count += 1
            current = current.next
        return count + 1

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return None
        else:
            top = self.top
            self.top = self.top.next
        return top.value

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return None
        top = self.top
        return top.value

#=============================================== Part II ==============================================

class Calculator:
    '''
        Required: _getPostfix must create and use a Stack object for expression processing

        >>> x=Calculator()
        >>> x._getPostfix('2 ^ 4')
        '2.0 4.0 ^'
        >>> x._getPostfix('2')
        '2.0'
        >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
        >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
        '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
        '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
        >>> x._getPostfix('( 2.5 )')
        '2.5'
        >>> x._getPostfix('( 2 { 5.0 } )')
        '2.0 5.0 *'
        >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
        '5.0 2.0 5.0 3.5 + + *'
        >>> x._getPostfix ('( { 2 } )')
        '2.0'
        >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
        '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x._getPostfix ('[ 2 * ( < 5 + 3 > ^ 2 + ( 1 + 4 ) ) ]')
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
        '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
        >>> x._getPostfix('2 * < -5 + 3 > ^ 2 + < 1 + 4 >')
        '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

        # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
        # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

        >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
        >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
        >>> x._getPostfix('2    5')
        >>> x._getPostfix('25 +')
        >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
        >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
        >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
        >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
        >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
    '''
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except:
            return False

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression processing

            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( < 5 + 3 > ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * < -5 + 3 > ^ 2 + < 1 + 4 >')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfix = ""

        tokens = txt.strip().split(' ')
        parenthesis = {')': '(' , '}' : '{' , ']':'[' , '>': '<'} #dictionary of parenthesis: closing are keys, opening are values

        if self.is_balanced(txt) == False: #Invalid checks
            return None
        if tokens[len(tokens) - 1] in ['+', '-', '/', '*', '^']: #Checks if last token is a operator
            #print('Last token is an operator')
            return None
        elif tokens[len(tokens) - 1] in parenthesis.values(): #Checks if last token is an open parenthesis
            #print('Last token is a open parenthesis')
            return None
        elif tokens[0] in parenthesis.keys(): #Checks if first token is closing parenthesis
            return None
        
        temp = []
        for token in range(len(tokens)-1): ## Implied multiplication
            if token not in ['+', '-', '/', '*', '^']:
                if self._isNumber(tokens[token]) and tokens[token+1] in parenthesis.values(): #for number (
                        temp.append(tokens[token])
                        temp.append('*') #might be wrong 
                elif tokens[token] in parenthesis.keys() and tokens[token+1] in parenthesis.values(): #for ) (
                        temp.append(tokens[token])
                        temp.append('*') ### for ) [ implied multiplication ##CHECK 
                elif tokens[token] in parenthesis.values() and self._isNumber(tokens[token]): # for ) number
                        temp.append(tokens[token])
                        temp.append('*')
                else:
                    temp.append(tokens[token])
            else:
                temp.append(tokens[token])
        temp.append(tokens[len(tokens)-1])
        tokens = temp
        
        for token in range(len(tokens)): #iterates through whole list 
            i = tokens[token]
            if i in parenthesis.values(): #Checks if opening parenthesis and pushes in stack                                    
                postfixStack.push(i)
            elif i in ['+', '-', '/', '*', '^']: #Checks if operator 
                if token != len(tokens) - 1 and tokens[token+1] in ['+', '-', '/', '*', '^']: #Checks if operator is next to another operator, returns None (invalid check)
                    return None
                if self.ishigherpres(i , postfixStack): #Checks precedence, calls helper function; if higher, pushes to stack
                    postfixStack.push(i)
                else:
                    while self.ishigherpres(i , postfixStack) == False: #While lower precedence, pops items from Stack and pushes operator at the end
                        postfix += postfixStack.pop() + " "
                    postfixStack.push(i)
            elif i in parenthesis.keys(): #Checks if closing parenthesis
                x = ''        
                while x.strip() != parenthesis[i] and postfixStack.isEmpty() == False: #Pops until matching parenthesis is found
                    x = postfixStack.pop() + " "
                    if x.strip() not in ['(' , '{' , '[' , '<']:
                        postfix += x
            elif self._isNumber(i): #Checks if it is a number, and adds it to postfix
                if token != len(tokens) - 1 and self._isNumber(tokens[token+1]):
                    return None
                postfix += str(float(i)) + " "
            else:
                return None

        while postfixStack.isEmpty() == False: #Pops out the rest of stack until empty
                postfix += postfixStack.pop() + " "

        return postfix.strip() #returns postfix
    
    def is_balanced(self, txt): #checks if parenthesis is balanced 
        s = Stack()
        is_open = {'(': 1, '[': 2, '{': 3}
        is_close = {')': 1, ']': 2, '}': 3}
        balanced = True
        size = len(txt)
        i = 0
        while balanced and i < size:
            current = txt[i]
            if current in is_open:
                s.push(current)
            elif current in is_close:
                if s.isEmpty():
                    balanced = False
                else:
                    top_parenthesis = s.pop()
                    balanced = is_open[top_parenthesis] == is_close[current]
            i += 1
        return s.isEmpty() and balanced
 
    def ishigherpres(self, i, pfstack): #PEMDAS, checks if higher precedence
        PEMDAS = {'-': 1, '+': 1, '/':2, '*':2, '^':3 , '(' : 0 , '{':0 , '[':0 , '<':0}
        if pfstack.isEmpty():
            return True
        elif PEMDAS[pfstack.peek()] >= PEMDAS[i]:
            return False
        else:
            return True

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack object to compute the final result as shown in the video lectures
            

            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * < 5 - 3 ^ 2 > + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * < 4 > ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None
        
        # YOUR CODE STARTS HERE

        calcStack = Stack()   # method must use calcStack to compute the  expression
        txt = self.getExpr
        if self._getPostfix(txt) == None: #If invalid, return None
            return None
        postfix = self._getPostfix(txt) 
        tokens = postfix.split()
        for i in tokens: #iterates through postfix expressions
            if self._isNumber(i): #Pushes numbers in stack
                calcStack.push(i)
            elif i == "+": #Does addition with two popped items and pushes to stack
                x = self.add(calcStack.pop() , calcStack.pop())
                calcStack.push(x)
            elif i == "-": #Does subtraction with two popped items and pushes to stack
                x = self.subtract(calcStack.pop() , calcStack.pop())
                calcStack.push(x)
            elif i == "/": #Does division with two popped items and pushes to stack
                x = self.divide(calcStack.pop() , calcStack.pop())
                if x == None: #Checks zero divison error
                    return None
                calcStack.push(x)
            elif i == "*": #Does multiplication with two popped items and pushes to stack
                x = self.multiply(calcStack.pop() , calcStack.pop())
                calcStack.push(x)
            elif i == "^": #Does exponentiation with two popped items and pushes to stack
                x = self.exponentiate(calcStack.pop() , calcStack.pop())
                calcStack.push(x)
        return float(calcStack.pop()) #returns float calculated value

    def add(self, num1, num2): #Helper methods to do math (addition, subtraction, division, multiplication, exponentiation)
        return str(float(num1) + float(num2))
    def subtract(self, num1, num2):
        return str(float(num2) - float(num1))
    def divide(self , num1, num2):
        if num1 == 0:
            return None
        return str(float(num2) / float(num1))
    def multiply(self, num1 , num2):
        return str(float(num1) * float(num2))
    def exponentiate(self, num1, num2):
        return str(float(num2) ** float(num1))


#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        bool = True
        if isinstance(word, str) == False: #Makes sure word is a string
            return False
        elif word == '': #Makes sure the string is not empty
            return False
        elif word.isalpha(): #If word is all alphabetical, returns True
            return True
        elif word.isalnum() == False: #If there are symbols, return False
            return False
        elif word[0].isalpha() == False: #If the first letter is a number, return False
            return False
        else:
            return True
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        lst = []
        tokens = expr.split()
        for i in tokens: #Iterates through tokens
            if self._isVariable(i) and i in self.states: #Checks if it is a valid variable in self.states
                value = self.states[i]
                lst.append(str(value)) # adds replaces value to lst
            elif self._isVariable(i) and i not in self.states: #If not valid, return None
                return None
            else:
                lst.append(str(i)) #Appends non-variables to list
        return ' '.join(lst).strip() #Returns spaced out lst as string

    def calculateExpressions(self):
        output = {}
        calcObj = Calculator()    # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        expressions = self.expressions.split(';')

        for i in expressions: #Takes every split expression ex. 'b = 4 + a'
            a = i.split('=') #Takes every left and right side of equation 'b' ; '4+a'
            x = []
            for z in a:
                x.append(z.strip())
            if len(x) == 2: #Checks if it has an equal sign
                if self._isVariable(x[0]) == False: #Returns None if it is not a valid variable
                    self.states = {}
                    return None
                calcObj.setExpr(self._replaceVariables(x[1])) #Changes variables
                self.states[x[0]] = calcObj.calculate
                output[i] = self.states.copy() #Adds to output dictionary
            else: #If it is the return statement, replace variables and calculate result, add to output
                a = x[0].split('return')[1].strip()
                calcObj.setExpr(self._replaceVariables(a))
                output['_return_'] = calcObj.calculate
        return output

def run_tests():
    import doctest

    #- Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    doctest.run_docstring_examples(Calculator, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()